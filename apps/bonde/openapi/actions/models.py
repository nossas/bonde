from django.db import models
from django.utils.timezone import now

from bonde.actionnetwork.models import SubmissionInterface, SignatureInterface, DonationInterface


class Form(SubmissionInterface):
    fields = models.JSONField(blank=True, null=True)

    class Meta:
        app_label = 'openapi_actions'


class TargetEmailPressure(models.Model):
    name = models.CharField(verbose_name="Name", max_length=100)
    email_address = models.EmailField(verbose_name="Email address")

    class Meta:
        app_label = 'openapi_actions'


class EmailPressure(SignatureInterface):
    email_subject = models.CharField(verbose_name="Email subject", max_length=80)
    email_body = models.TextField(verbose_name="Email body")
    targets = models.ManyToManyField(TargetEmailPressure)

    class Meta:
        app_label = 'openapi_actions'


class Donation(DonationInterface):
    PAYMENT_METHOD_CHOICES = (
        ('creditcard', 'Cartão de crédito'),
        ('boleto', 'Boleto'),
        ('pix', 'Pix')
    )

    payment_method = models.CharField(verbose_name="Payment method", max_length=20, choices=PAYMENT_METHOD_CHOICES)
    is_subscription = models.BooleanField(verbose_name="Is subscription?", default=False)

    class Meta:
        app_label = 'openapi_actions'