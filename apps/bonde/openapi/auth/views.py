from rest_framework import serializers, viewsets
from rest_framework.permissions import IsAuthenticated

from .models import User, UsersGroup


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['url', 'email', 'first_name', 'is_staff']


class UsersGroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = UsersGroup
        fields = ['url', 'name']


# class UserViewSet(viewsets.ModelViewSet):
#     queryset = User.objects.all()
#     serializer_class = UserSerializer
#     permission_classes = [IsAuthenticated, ]

#     def get_queryset(self, *args, **kwargs):
#         import ipdb;ipdb.set_trace()


class UsersGroupViewSet(viewsets.ModelViewSet):
    queryset = UsersGroup.objects.all()
    serializer_class = UsersGroupSerializer
    permission_classes = [IsAuthenticated, ]
    
    def get_queryset(self, *args, **kwargs):
        if not self.request.user.is_superuser:
            return self.queryset.filter(users__in=[self.request.user])

        return self.queryset