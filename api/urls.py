from django.urls import path

from api.views import competition_view

urlpatterns = [
    path(
        "competition/",
        competition_view.CompetitionAPIView.as_view(),
        name="competition",
    ),
    path(
        "competition/<competition_id>",
        competition_view.CompetitionAPIView.as_view(),
        name="competition",
    ),
    path(
        "competition/<competition_id>/rank",
        competition_view.CompetitionRankAPIView.as_view(),
        name="competition-rank",
    ),
    path(
        "round-highlight",
        competition_view.HighlightCompetitionRoundAPIView.as_view(),
        name="round-highlight",
    ),
]
