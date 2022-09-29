import pytest
from django.urls import reverse
from rest_framework import status
from model_bakery import baker


@pytest.mark.django_db
class TestCompetitionAPIView:

    def test_should_return_competition_if_it_exists(
        self, competition, api_client
    ):
        # given
        endpoint = reverse(
            "competition",
            kwargs={"competition_id": competition.competition_id},
        )

        # when
        response = api_client.get(endpoint)

        # then
        assert response.status_code == status.HTTP_200_OK
        assert response.json() == {
            'competition_id': str(competition.competition_id),
            'title': competition.title,
            'sex': competition.sex,
            'rounds': competition.rounds,
        }

    def test_should_return_404_when_competition_does_not_exists(
        self, api_client
    ):
        # given
        endpoint = reverse(
            "competition",
            kwargs={"competition_id": "aaaa"},
        )

        # when
        response = api_client.get(endpoint)

        # then
        assert response.status_code == status.HTTP_404_NOT_FOUND
        assert response.json() == {"detail": "Not found."}


@pytest.mark.django_db
class TestCompetitionRankAPIView:

    def test_should_return_404_when_competition_does_not_exists(
        self, api_client
    ):
        # given
        endpoint = reverse(
            "competition-rank",
            kwargs={"competition_id": "aaaa"},
        )

        # when
        response = api_client.get(endpoint)

        # then
        assert response.status_code == status.HTTP_404_NOT_FOUND
        assert response.json() == {"detail": "Not found."}

    def test_should_list_competitors_and_round_stats_for_a_competition(
        self, competition, api_client
    ):
        # given
        endpoint = reverse(
            "competition-rank",
            kwargs={"competition_id": competition.competition_id},
        )
        competitors = baker.make(
            "domain.Competitor", competition=competition,
            age=30,
            sex=competition.sex,
            weight=84.0,
            _quantity=2
        )
        init = 120.0
        rounds = []
        for competitor in competitors:
            rounds.append(baker.make(
                "domain.CompetitionRound",
                competitor=competitor,
                lifted_weight=init
            ))
            init -= 10.0

        # when
        response = api_client.get(endpoint)

        # then
        assert response.status_code == status.HTTP_200_OK
        json_response = response.json()
        assert len(json_response) == 2
        expected_response = {
            'competitor_id': str(competitors[0].competitor_id),
            'competition': str(competition.competition_id),
            'name': str(competitors[0].name),
            'age': competitors[0].age,
            'sex': competitors[0].sex,
            'weight': competitors[0].weight,
            'picture': None,
            'last_valid_round': {
                'round_id': str(rounds[0].round_id),
                'lifted_weight': rounds[0].lifted_weight,
                'coefficient': str(rounds[0].coefficient),
                'valid': True,
                'created_at': rounds[0].created_at.strftime(
                    "%Y-%m-%dT%H:%M:%S.%fZ"
                ),
            }
        }
        assert json_response[0] == expected_response
