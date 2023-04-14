from django.conf import settings

from appconf import AppConf


class ZendeskConf(AppConf):
    DATABASE_NAME = 'bonde'

    class Meta:
        prefix = 'mapa_zendesk'