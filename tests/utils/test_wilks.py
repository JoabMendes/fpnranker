from decimal import Decimal

from utils.wilks import CoefficientCalculator


class TestCoefficientCalculator:

    def test_male_coefficient(self):
        coefficient = CoefficientCalculator.calculate(
            sex="male", body_weight=84.0, lifted_weight=120.0
        )
        assert coefficient == Decimal("95.543")

    def test_female_coefficient(self):
        coefficient = CoefficientCalculator.calculate(
            sex="female", body_weight=84.0, lifted_weight=120.0
        )
        assert coefficient == Decimal("133.268")
