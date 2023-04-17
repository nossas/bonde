from django.contrib import admin

from bonde.actionnetwork.admin import ActionAdmin, DonationActionAdmin

from .models import Form, EmailPressure, Donation, TargetEmailPressure



admin.site.register(TargetEmailPressure, admin.ModelAdmin)
admin.site.register(Form, ActionAdmin)
admin.site.register(EmailPressure, ActionAdmin)
admin.site.register(Donation, DonationActionAdmin)