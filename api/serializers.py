from rest_framework import serializers


from domain.models import CompetitionRound, Competitor, Competition


class RankCompetitionRoundSerializer(serializers.ModelSerializer):

    class Meta:
        model = CompetitionRound
        fields = (
            'round_id',
            'lifted_weight',
            'coefficient',
            'valid',
            'created_at'
        )


class RankCompetitorSerializer(serializers.ModelSerializer):

    last_valid_round = serializers.SerializerMethodField()

    class Meta:
        model = Competitor
        fields = (
            'id',
            'competitor_id',
            'competition',
            'name',
            'age',
            'sex',
            'weight',
            'picture',
            'last_valid_round'
        )

    @staticmethod
    def get_last_valid_round(competitor):
        try:
            last_valid_round = CompetitionRound.objects.filter(
                competitor=competitor,
                valid=True
            ).latest("created_at")
            return RankCompetitionRoundSerializer(last_valid_round).data
        except CompetitionRound.DoesNotExist:
            return {
                'round_id': None,
                'lifted_weight': 0.0,
                'coefficient': 0.0,
                'valid': True,
                'created_at': None
            }


class CompetitionSerializer(serializers.ModelSerializer):

    class Meta:
        model = Competition
        fields = (
            'competition_id',
            'title',
            'sex',
            'rounds'
        )
