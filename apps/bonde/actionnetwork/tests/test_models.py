import pytest

import requests_mock
from model_bakery import baker

from actionnetwork.models import Campaign
from actionnetwork.exceptions import InvalidRequestAPIException


def test_save_response_json_when_create_campaign(db):
    action_group = baker.make("actionnetwork.ActionGroup")
    params = {
        "title": "Campaign #1",
        "action_group": action_group,
        "resource_name": "forms",
    }

    with requests_mock.mock()  as m:
        m.post(
            f"https://actionnetwork.org/api/v2/{params['resource_name']}/",
            status_code=200,
            json={"title": params['title']}
        )

        campaign = Campaign.objects.create(**params)

        assert m.called is True
        assert m.last_request.headers['OSDI-API-Token'] == action_group.api_secret_key

        assert campaign.api_response_json['title'] == campaign.title


def test_not_create_campaign_and_raise_exception(db):
    action_group = baker.make("actionnetwork.ActionGroup")
    params = {
        "title": "Campaign #1",
        "action_group": action_group,
        "resource_name": "forms",
    }

    with requests_mock.mock()  as m:
        m.post(
            f"https://actionnetwork.org/api/v2/{params['resource_name']}/",
            status_code=500,
            json={"title": params['title']}
        )

        with pytest.raises(InvalidRequestAPIException):
            Campaign.objects.create(**params)
