from django.contrib import admin

from .models import (
    ActionGroup,
    Campaign,
    Person,
    EmailAddress,
    PhoneNumber,
    PostalAddress,
    CustomField,
    Signature,
    Submission,
    Donation
)


class ReadOnlyMixin(object):

    def has_add_permission(self, request, obj=None):
        return False

    def has_delete_permission(self, request, obj=None):
        return False



class EmailAddressInline(ReadOnlyMixin, admin.TabularInline):
    model = EmailAddress
    readonly_fields = ('address', )


class PhoneNumberInline(ReadOnlyMixin, admin.TabularInline):
    model = PhoneNumber
    readonly_fields = ('number', )


class PostalAddressInline(ReadOnlyMixin, admin.StackedInline):
    model = PostalAddress


class CustomFieldInline(admin.TabularInline):
    model = CustomField


class PersonAdmin(admin.ModelAdmin):
    list_display = ('email_address', 'full_name')
    inlines = [
        EmailAddressInline,
        PhoneNumberInline,
        PostalAddressInline,
        CustomFieldInline
    ]
    search_fields = ('given_name', 'email_addresses__address', )

    @admin.display(ordering='given_name', description='Person name')
    def full_name(self, obj):
        return obj.given_name + " " + obj.family_name

    @admin.display(ordering='email_addresses__address', description='Email')
    def email_address(self, obj):
        return obj.email_addresses.first()

    def has_add_permission(self, request, obj=None):
        return False


class CampaignAdmin(admin.ModelAdmin):
    list_display = ('title', 'resource_name')
    fields = ('title', 'action_group', 'resource_name', 'api_response_json')
    readonly_fields = ('api_response_json', )
    
    def save_model(self, request, obj, form, change):
        if not change:
            return Campaign.objects.create(**form.cleaned_data)
        return super().save_model(request, obj, form, change)


class ActionAdmin(admin.ModelAdmin):
    list_display = ('action__uuid', 'person__full_name', 'person__uuid', 'campaign__title')
    readonly_fields = ('api_response_json', )

    @admin.display(ordering='person__given_name', description='Person name')
    def person__full_name(self, obj):
        return obj.person.given_name + " " + obj.person.family_name

    @admin.display(ordering='campaign__title', description='Campaign title')
    def campaign__title(self, obj):
        return obj.campaign.title

    @admin.display(description='Person UUID')
    def person__uuid(self, obj):
        return obj.api_response_json['action_network:person_id']
    
    @admin.display(description='Action UUID')
    def action__uuid(self, obj):
        return obj.uuid()

    def has_add_permission(self, request, obj=None):
        return False
    
    def has_change_permission(self, request, obj=None):
        return False

    def has_delete_permission(self, request, obj=None):
        return False


class DonationActionAdmin(ActionAdmin):
    list_display = ActionAdmin.list_display + ('amount', 'created_date', )

# Register your models here.
admin.site.register(ActionGroup)
admin.site.register(Campaign, CampaignAdmin)
admin.site.register(Person, PersonAdmin)

admin.site.register(Donation, DonationActionAdmin)
admin.site.register(Submission, ActionAdmin)
admin.site.register(Signature, ActionAdmin)