from django.apps import AppConfig
from django.utils.translation import gettext_lazy as _


class AuthOpenApiConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'bonde.openapi.auth'
    label = 'openapi_auth'
    verbose_name = _('openapi auth')