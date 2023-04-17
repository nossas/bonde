import requests
import json

from django.contrib.contenttypes.models import ContentType
from django.contrib.admin.models import LogEntry, ADDITION
from django.contrib.auth.models import User
from django.db import models
from django.utils.timezone import now

# from django.contrib.postgres.fields import ArrayField
from .conf import settings
from .exceptions import (
    InvalidRequestAPIException,
    FieldException,
    InvalidInstanceModelException,
)


class CampaignManager(models.Manager):
    def create(self, **kwargs):
        title = kwargs.get("title")
        resource_name = kwargs.get("resource_name")
        action_group = kwargs.get("action_group")

        # Request for Action Network API
        response = requests.post(
            f"https://actionnetwork.org/api/v2/{resource_name}/",
            data={"title": title, "origin_system": "Bonde Actions API"},
            headers={"OSDI-API-Token": action_group.api_secret_key},
        )

        if response.status_code == 200:
            # Save on database Campaign model with response
            return super(CampaignManager, self).create(
                title=title,
                resource_name=resource_name,
                action_group=action_group,
                api_response_json=response.json(),
            )

        raise InvalidRequestAPIException(response.text)


class Campaign(models.Model):
    RESOURCES = (
        ("forms", "Forms"),
        ("fundraising_pages", "Donations"),
        ("petitions", "Petitions"),
    )

    title = models.CharField(verbose_name="Title of campaign", max_length=200)

    resource_name = models.CharField(
        verbose_name="API Resource name", max_length=50, choices=RESOURCES
    )

    api_response_json = models.JSONField(verbose_name="API Response JSON", blank=True)

    action_group = models.ForeignKey(settings.ACTIONNETWORK_GROUPMODEL, on_delete=models.CASCADE)

    objects = CampaignManager()

    def __str__(self):
        return self.title

    def get_endpoint(self):
        return self.api_response_json["_links"]["self"]["href"]

    # def an_request(self):
    #     response = requests.get(
    #         self.get_endpoint(),
    #         headers={"OSDI-API-Token": self.action_group.api_secret_key},
    #     )

    #     import ipdb

    #     ipdb.set_trace()


class Person(models.Model):
    given_name = models.CharField(verbose_name="Given name", max_length=80)

    family_name = models.CharField(verbose_name="Family name", max_length=120)

    def __str__(self):
        return self.full_name()

    def full_name(self):
        return f"{self.given_name} {self.family_name}"


class EmailAddress(models.Model):
    address = models.EmailField(verbose_name="Address", unique=True)

    person = models.ForeignKey(
        Person, on_delete=models.CASCADE, related_name="email_addresses"
    )

    def __str__(self):
        return self.address


class PhoneNumber(models.Model):
    number = models.CharField(verbose_name="Number", max_length=15, unique=True)

    person = models.ForeignKey(
        Person, on_delete=models.CASCADE, related_name="phone_numbers"
    )

    def __str__(self):
        return self.number


class PostalAddress(models.Model):
    address_lines = models.CharField(
        verbose_name="Address line", max_length=200, blank=True
    )

    locality = models.CharField(verbose_name="Locality", max_length=80, blank=True)

    region = models.CharField(verbose_name="Region", max_length=100, blank=True)

    postal_code = models.CharField(
        verbose_name="Postal code", max_length=30, blank=True
    )

    country = models.CharField(verbose_name="Country", max_length=30, blank=True)

    person = models.ForeignKey(
        Person, on_delete=models.CASCADE, related_name="postal_addresses"
    )


class CustomField(models.Model):
    name = models.CharField(verbose_name="Name of field", max_length=50)

    value = models.CharField(verbose_name="Value of field", max_length=150)

    person = models.ForeignKey(
        Person, on_delete=models.CASCADE, related_name="custom_fields"
    )


class ActionRecordManager(models.Manager):
    def create(self, campaign, add_tags=[], remove_tags=[], **kwargs):
        # Raise Incorrect Action Model
        if (
            self.model.__name__ == "Donation"
            and campaign.resource_name != "fundraising_pages"
        ):
            raise InvalidInstanceModelException(
                "Donation model request fundraising_pages campaign"
            )

        if self.model.__name__ == "Submission" and campaign.resource_name != "form":
            raise InvalidInstanceModelException(
                "Submission model request forms campaign"
            )

        if self.model.__name__ == "Signature" and campaign.resource_name != "petitions":
            raise InvalidInstanceModelException(
                "Signature model request petitions campaign"
            )

        # Instance of person
        person = kwargs.get("person")
        if person:
            del kwargs["person"]

        # Fields to create or get person instance
        given_name = kwargs.get("given_name")
        if given_name:
            del kwargs["given_name"]

        family_name = kwargs.get("family_name")
        if family_name:
            del kwargs["family_name"]

        email_address = kwargs.get("email_address")
        if email_address:
            del kwargs["email_address"]

        if not person and not email_address:
            raise FieldException("person or email_address is required")

        elif not person and email_address:
            person = Person.objects.filter(
                email_addresses__address=email_address
            ).first()

        if not person:
            person = Person.objects.create(
                given_name=given_name, family_name=family_name
            )
            EmailAddress.objects.create(address=email_address, person=person)

            phone_number = kwargs.get("phone_number")
            if phone_number:
                PhoneNumber.objects.create(number=phone_number, person=person)

            postal_address = kwargs.get("postal_address")
            if postal_address:
                PostalAddress.objects.create(**postal_address, person=person)

        # TODO: Mudar forma alterar implementação a partir dos tipos de ação
        if self.__get_resource_name() == 'donations':
            amount = kwargs.get("amount")
            created_date = kwargs.get("created_date")

            if not amount:
                raise FieldException("amount is required")

            if not created_date:
                raise FieldException("created_date is required")

            response = self.__request_action_network_api(
                person=person,
                campaign=campaign,
                add_tags=add_tags,
                remove_tags=remove_tags,
                # Params only used to donations
                recipients=[dict(display_name=campaign.title, amount=float(amount))],
                created_date=created_date.strftime("%Y-%m-%dT%H:%M:%SZ"),
            )
        else:
            response = self.__request_action_network_api(
                person=person,
                campaign=campaign,
                add_tags=add_tags,
                remove_tags=remove_tags,
            )

        # Call super create method for instance
        action = super(ActionRecordManager, self).create(
            person=person,
            campaign=campaign,
            api_response_json=response.json(),
            **kwargs,
        )

        self.__log_history(action)

        return action

    def __log_history(self, instance):
        user_api = User.objects.get(username="api")

        LogEntry.objects.log_action(
            user_id=user_api.id,
            content_type_id=ContentType.objects.get_for_model(instance.person).pk,
            object_id=instance.person.pk,
            object_repr=str(instance.person),
            action_flag=ADDITION,
            change_message=f"ADD {instance.campaign.resource_name} TO {instance.campaign.title} // {instance.uuid()}",
        )

    def __get_resource_name(self):
        if issubclass(self.model, SubmissionInterface):
            return "submissions"
        elif issubclass(self.model, SignatureInterface):
            return "signatures"
        elif issubclass(self.model, DonationInterface):
            return "donations"
        else:
            raise InvalidInstanceModelException(
                f"{self.model.__name__} should be implement an interface"
            )

    def __request_action_network_api(
        self, person, campaign, add_tags=[], remove_tags=[], **kwargs
    ):
        resource_name = self.__get_resource_name()
        endpoint = f"{campaign.get_endpoint()}/{resource_name}"

        payload = {
            "person": {
                "family_name": person.family_name,
                "given_name": person.given_name,
                "postal_address": list(
                    map(
                        lambda x: dict(postal_code=x.postal_code),
                        person.postal_addresses.all(),
                    )
                ),
                "email_addresses": list(
                    map(lambda x: dict(address=x.address), person.email_addresses.all())
                ),
                "phone_numbers": list(
                    map(lambda x: dict(number=x.number), person.phone_numbers.all())
                ),
                "custom_fields": {
                    item.name: item.value for item in person.custom_fields.all()
                },
            },
            "add_tags": add_tags,
            "remove_tags": remove_tags,
        }

        payload.update(kwargs)

        response = requests.post(
            endpoint,
            data=json.dumps(payload),
            headers={
                "Content-Type": "application/json",
                "OSDI-API-Token": campaign.action_group.api_secret_key,
            },
        )

        if response.status_code == 200:
            return response

        import ipdb

        ipdb.set_trace()

        raise InvalidRequestAPIException(response.text)


class ActionRecordModel(models.Model):
    person = models.ForeignKey(Person, on_delete=models.CASCADE)

    created_date = models.DateTimeField(verbose_name="Created date")

    # add_tags = ArrayField(models.CharField(verbose_name="Add tags", max_length=30))

    # remove_tags = ArrayField(models.CharField(verbose_name="Remove tags", max_length=30))

    campaign = models.ForeignKey(Campaign, on_delete=models.CASCADE)

    api_response_json = models.JSONField(verbose_name="API Response JSON")

    class Meta:
        abstract = True

    objects = ActionRecordManager()

    def uuid(self):
        uuid_text = self.api_response_json["identifiers"][0]
        return uuid_text.replace("action_network:", "")


class ActionGroupInterface(models.Model):
    name = models.CharField(verbose_name="Name", max_length=150)

    api_secret_key = models.CharField(verbose_name="API Secret key", max_length=200)

    is_valid = models.BooleanField(verbose_name="Is a valid group?", default=False)

    class Meta:
        abstract = True

    def __str__(self):
        return self.name


class SubmissionInterface(ActionRecordModel):
    class Meta:
        abstract = True


class SignatureInterface(ActionRecordModel):
    class Meta:
        abstract = True


class DonationInterface(ActionRecordModel):
    amount = models.DecimalField(verbose_name="Amount", decimal_places=2, max_digits=10)

    class Meta:
        abstract = True
