from django.db.models import Prefetch

from rest_framework import serializers
from rest_framework.generics import ListAPIView
from rest_framework.permissions import IsAuthenticated

from bonde.actionnetwork.models import Campaign
from bonde.openapi.actions.views import CampaignSerializer

from .models import UsersGroup


class UsersGroupSerializer(serializers.ModelSerializer):
    campaign_set = CampaignSerializer(many=True, exclude=["group"])

    class Meta:
        model = UsersGroup
        fields = ["name", "token", "campaign_set"]


class UsersGroupListAPIView(ListAPIView):
    serializer_class = UsersGroupSerializer
    permission_classes = [
        IsAuthenticated,
    ]

    def get_queryset(self, *args, **kwargs):
        campaign_resource_name = self.request.query_params.get("campaign_resource_name")
        queryset = UsersGroup.objects

        if campaign_resource_name:
            campaign_set_prefetched = Prefetch(
                "campaign_set",
                Campaign.objects.filter(resource_name=campaign_resource_name),
            )
            queryset = queryset.prefetch_related(campaign_set_prefetched)

        if not self.request.user.is_superuser:
            return queryset.filter(users__in=[self.request.user])

        return queryset.all()
