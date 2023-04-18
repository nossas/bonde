from django.utils.timezone import now

from rest_framework import serializers, status
from rest_framework.reverse import reverse
from rest_framework.response import Response
from rest_framework.generics import get_object_or_404, CreateAPIView, ListAPIView
from rest_framework.permissions import IsAuthenticated

from bonde.actionnetwork.models import Campaign, Person

from .models import Form, Donation, EmailPressure


class CampaignSerializer(serializers.ModelSerializer):
    group = serializers.CharField(source="action_group.name")
    url = serializers.SerializerMethodField()

    class Meta:
        model = Campaign
        fields = ['title', 'resource_name', 'group', 'url']

    def __init__(self, *args, **kwargs):
        # Instantiate the superclass normally

        exclude = kwargs.pop('exclude', None)

        # Instantiate the superclass normally
        super(CampaignSerializer, self).__init__(*args, **kwargs)

        if exclude is not None:
            # Drop any fields that are specified in the `exclude` argument.
            exclude = set(exclude)
            for field_name in exclude:
                self.fields.pop(field_name)
    
    def get_url(self, instance):
        request = self.context.get('request')

        if not request:
            # When use serializer in shell command hasnt request 
            return 'shell'
        
        return reverse(instance.resource_name, kwargs={"campaign_id": instance.id}, request=request)


class CampaignAPIListView(ListAPIView):
    queryset = Campaign.objects.all()
    serializer_class = CampaignSerializer
    permission_classes = [IsAuthenticated, ]

    def get_queryset(self, *args, **kwargs):
        if not self.request.user.is_superuser:
            return self.queryset.filter(action_group__users__in=[self.request.user])

        return self.queryset


class ActionCreateApiView(CreateAPIView):
    permission_classes = [IsAuthenticated, ]

    def __get_campaign(self):
        return get_object_or_404(Campaign, pk=self.kwargs.get('campaign_id'))

    def create(self, request, *args, **kwargs):
        
        campaign = self.__get_campaign()

        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        instance = serializer.save(campaign=campaign)

        # TODO: padronizar resposta de ação
        headers = self.get_success_headers(request.data)
        return Response({'action_id': instance.id}, status=status.HTTP_201_CREATED, headers=headers)


class PersonSerializer(serializers.ModelSerializer):
    email_address = serializers.EmailField()

    class Meta:
        model = Person
        fields = '__all__'


class ActionSerializerMixin(serializers.ModelSerializer):
    person = PersonSerializer()

    class Meta:
        exclude = ['api_response_json', 'campaign', 'created_date']

    def create(self, validated_data):
        person_data = validated_data.pop('person')
        
        instance = self.Meta.model.objects.create(**validated_data, **person_data, created_date=now())

        return instance


class FormSerializer(ActionSerializerMixin):
    fields = serializers.JSONField()

    class Meta(ActionSerializerMixin.Meta):
        model = Form


class FormCreateAPIView(ActionCreateApiView):
    serializer_class = FormSerializer


class DonationSerializer(ActionSerializerMixin):

    class Meta(ActionSerializerMixin.Meta):
        model = Donation


class DonationCreateAPIView(ActionCreateApiView):
    serializer_class = DonationSerializer


class EmailPressureSerializer(ActionSerializerMixin):

    class Meta(ActionSerializerMixin.Meta):
        model = EmailPressure


class EmailPressureAPIView(ActionCreateApiView):
    serializer_class = EmailPressureSerializer