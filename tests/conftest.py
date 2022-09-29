import pytest
from model_bakery import baker
from rest_framework.test import APIClient


@pytest.fixture
def api_client():
    return APIClient()


@pytest.fixture()
def competition():
    return baker.make(
        "domain.Competition",
        title="Deadlift FPN 2022",
        sex="masculino"
    )


@pytest.fixture()
def competitor():
    return baker.make(
        "domain.Competitor", age=30, sex="masculino", weight=84.0
    )


@pytest.fixture()
def competition_round(competitor):
    return baker.make(
        "domain.CompetitionRound",
        competitor=competitor,
        lifted_weight=120.0
    )
