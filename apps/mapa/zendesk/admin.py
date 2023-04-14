from django.contrib import admin
from .models import SolidarityUsers


class SolidarityUsersAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'condition', 'city', 'cep')
    list_filter = ('condition', )

admin.site.register(SolidarityUsers, SolidarityUsersAdmin)