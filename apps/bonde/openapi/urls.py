from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
# from snippets import views

from .actions.views import CampaignAPIListView, FormCreateAPIView, DonationCreateAPIView, EmailPressureAPIView
from .auth.views import UsersGroupListAPIView

urlpatterns = [
    path('groups/', UsersGroupListAPIView.as_view(), name="groups"),
    path('campaigns/', CampaignAPIListView.as_view(), name="campaigns"),
    path('campaigns/<int:campaign_id>/forms', FormCreateAPIView.as_view(), name="forms"),
    path('campaigns/<int:campaign_id>/donations', DonationCreateAPIView.as_view(), name="fundraising_pages"),
    path('campaigns/<int:campaign_id>/email_pressures', EmailPressureAPIView.as_view(), name="petitions"),
]

urlpatterns = format_suffix_patterns(urlpatterns)