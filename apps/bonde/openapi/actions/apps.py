from django.apps import AppConfig
from django.utils.translation import gettext_lazy as _

class ActionsOpenApiConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'bonde.openapi.actions'
    label = 'openapi_actions'
    verbose_name = _('openapi actions')
