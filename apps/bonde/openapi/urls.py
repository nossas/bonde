from django.urls import path, include

from rest_framework import routers

from .auth.views import UsersGroupViewSet

router = routers.DefaultRouter()

# router.register(r'auth/users', UserViewSet)
router.register(r'auth/groups', UsersGroupViewSet)