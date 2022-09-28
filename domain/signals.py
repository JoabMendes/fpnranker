from django.db.models.signals import pre_save
from django.dispatch import receiver

from domain.models import CompetitionRound

from utils.wilks import CoefficientCalculator


@receiver(
    pre_save,
    sender=CompetitionRound,
    dispatch_uid="competition_round_pre_save_handler",
)
def competition_round_pre_save_handler(sender, instance, **kwargs):
    # calculate wilks coefficient
    sex = "male"
    if instance.competitor.sex == "feminino":
        sex = "female"
    coefficient = CoefficientCalculator.calculate(
        sex=sex,
        body_weight=instance.competitor.weight,
        lifted_weight=instance.lifted_weight
    )
    instance.coefficient = coefficient
