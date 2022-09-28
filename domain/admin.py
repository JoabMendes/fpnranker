from django.contrib import admin
#
# # Register your models here.

from domain.models import (
    Competition,
    Competitor,
    CompetitionRound
)


@admin.register(Competition)
class CompetitionAdmin(admin.ModelAdmin):
    search_fields = ("title",)
    list_display = [
        "title", "sex", "created_at"
    ]
    readonly_fields = ("competition_id",)


@admin.register(Competitor)
class CompetitorAdmin(admin.ModelAdmin):
    search_fields = ("name",)
    list_display = [
        "name", "age", "weight"
    ]
    readonly_fields = ("competitor_id",)
    autocomplete_fields = ("competition",)


@admin.register(CompetitionRound)
class CompetitionRoundAdmin(admin.ModelAdmin):
    search_fields = ("competitor__name",)
    list_display = [
        "competitor", "lifted_weight", "coefficient", "valid"
    ]
    readonly_fields = ("round_id", "coefficient")
    autocomplete_fields = ("competitor",)
