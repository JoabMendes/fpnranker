from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from django.http import Http404
from django.core.exceptions import ValidationError

from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status

from domain.models import Competition, Competitor
from api.serializers import (
    RankCompetitorSerializer,
    CompetitionSerializer
)


@method_decorator(csrf_exempt, name="dispatch")
class CompetitionAPIView(APIView):
    permission_classes = ()

    def _get_competition(self, competition_id):
        try:
            return Competition.objects.get(competition_id=competition_id)
        except (Competition.DoesNotExist, ValidationError):
            raise Http404

    def get(self, request, competition_id=None, format=None):
        if competition_id:
            competition = self._get_competition(competition_id=competition_id)
            serialized = CompetitionSerializer(competition)
            return Response(serialized.data)
        else:
            competitions = Competition.objects.all()
            serialized = CompetitionSerializer(competitions, many=True)
            return Response(serialized.data)

    def post(self, request, format=None):
        serializer = CompetitionSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(
                serializer.errors,
                status=status.HTTP_400_BAD_REQUEST
            )

    def patch(self, request, competition_id, format=None):
        competition = self._get_competition(competition_id=competition_id)
        serializer = CompetitionSerializer(
            competition, data=request.data, partial=True
        )
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(
            serializer.errors, status=status.HTTP_400_BAD_REQUEST
        )


@method_decorator(csrf_exempt, name="dispatch")
class CompetitionRankAPIView(APIView):
    permission_classes = ()

    def _get_competition(self, competition_id):
        try:
            return Competition.objects.get(competition_id=competition_id)
        except (Competition.DoesNotExist, ValidationError):
            raise Http404

    def get(self, request, competition_id, format=None):
        competition = self._get_competition(competition_id=competition_id)
        competitors = Competitor.objects.filter(competition=competition)
        serialized = RankCompetitorSerializer(competitors, many=True)
        return Response(serialized.data)
