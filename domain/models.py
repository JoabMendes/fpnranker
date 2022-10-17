import uuid
from django.db import models

FEMALE_SEX_CHOICE = "feminino"
MALE_SEX_CHOICE = "masculino"
SEX_CHOICES = (
    (MALE_SEX_CHOICE, "Masculino"),
    (FEMALE_SEX_CHOICE, "Feminino"),
)


class Competition(models.Model):
    competition_id = models.UUIDField(primary_key=True, default=uuid.uuid4)
    title = models.CharField(
        max_length=128, blank=False, null=False,
        verbose_name="Título"
    )
    sex = models.CharField(
        max_length=20,
        choices=SEX_CHOICES,
        verbose_name="Sexo"
    )
    rounds = models.PositiveIntegerField(null=False, blank=False, default=3)
    created_at = models.DateTimeField(auto_now_add=True, blank=True)
    updated_at = models.DateTimeField(auto_now=True, blank=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Competição"
        verbose_name_plural = "Competições"


class Competitor(models.Model):
    id = models.BigAutoField(primary_key=True, editable=False)
    competitor_id = models.UUIDField(default=uuid.uuid4)
    competition = models.ForeignKey(Competition, on_delete=models.CASCADE)
    name = models.CharField(
        max_length=256, blank=False, null=False,
        verbose_name="Nome"
    )
    age = models.PositiveIntegerField(
        null=False, blank=False, default=1,
        verbose_name="Idade"
    )
    sex = models.CharField(
        max_length=20,
        choices=SEX_CHOICES,
        verbose_name="Sexo"
    )
    weight = models.FloatField(
        null=False, blank=False, default=0.0,
        verbose_name="Peso (Kg)"
    )
    picture = models.FileField(
        upload_to='competitor_images',
        blank=False,
        null=False
    )
    created_at = models.DateTimeField(auto_now_add=True, blank=True)
    updated_at = models.DateTimeField(auto_now=True, blank=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Competidor(a)"
        verbose_name_plural = "Competidores(as)"


class CompetitionRound(models.Model):
    id = models.BigAutoField(primary_key=True, editable=False)
    round_id = models.UUIDField(default=uuid.uuid4)
    competitor = models.ForeignKey(Competitor, on_delete=models.CASCADE)
    lifted_weight = models.FloatField(
        null=False, blank=False, default=0.0,
        verbose_name="Peso Levantado (Kg)"
    )
    coefficient = models.DecimalField(
        blank=True,
        null=True,
        max_digits=15,
        decimal_places=3,
        verbose_name="Coeficiente"
    )
    valid = models.BooleanField(default=True, verbose_name="Round válido?")
    created_at = models.DateTimeField(auto_now_add=True, blank=True)
    updated_at = models.DateTimeField(auto_now=True, blank=True)

    def __str__(self):
        return f"{self.competitor.name}"

    class Meta:
        verbose_name = "Round"
        verbose_name_plural = "Rounds"
