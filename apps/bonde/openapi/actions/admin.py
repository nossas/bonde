from django.contrib import admin

from bonde.actionnetwork.admin import ActionAdmin, DonationActionAdmin

from .models import Form, EmailPressure, Donation, TargetEmailPressure


class EmailPressureActionAdmin(ActionAdmin):

    def save_model(self, request, obj, form, change):
        if not change:
            targets = form.cleaned_data.pop('targets')

            obj = self.model.objects.create(**form.cleaned_data)
            obj.targets.set(targets)
            obj.save()

            return obj
        
        return super().save_model(request, obj, form, change)


admin.site.register(TargetEmailPressure, admin.ModelAdmin)
admin.site.register(Form, ActionAdmin)
admin.site.register(EmailPressure, EmailPressureActionAdmin)
admin.site.register(Donation, DonationActionAdmin)