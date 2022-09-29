from django.urls import path

from api.views import competition_round_view

urlpatterns = [
    path(
        "competition/<competition_id>",
        competition_round_view.CompetitionAPIView.as_view(),
        name="competition",
    ),
    path(
        "competition/<competition_id>/rank",
        competition_round_view.CompetitionRankAPIView.as_view(),
        name="competition-rank",
    ),
]
