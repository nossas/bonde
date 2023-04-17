from django.conf import settings

from appconf import AppConf


class ZendeskConf(AppConf):
    GROUPMODEL = 'actionnetwork.ActionGroup'

    class Meta:
        prefix = 'actionnetwork'