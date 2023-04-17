from django.apps import AppConfig
from django.utils.translation import gettext_lazy as _


class OpenApiConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'bonde.openapi'
    label = 'openapi'
    verbose_name = _('bonde')