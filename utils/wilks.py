from decimal import Decimal


MEN_CONSTANTS = {
    "a": Decimal("47.46178854"),
    "b": Decimal("8.472061379"),
    "c": Decimal("0.07369410346"),
    "d": Decimal("-0.001395833811"),
    "e": Decimal("0.00000707665973070743"),
    "f": Decimal("-0.0000000120804336482315"),
}

WOMEN_CONSTANTS = {
    "a": Decimal("-125.4255398"),
    "b": Decimal("13.71219419"),
    "c": Decimal("-0.03307250631"),
    "d": Decimal("-0.001050400051"),
    "e": Decimal("0.00000938773881462799"),
    "f": Decimal("-0.000000023334613884954"),
}


class CoefficientCalculator:

    @staticmethod
    def calculate(sex: str, body_weight: float, lifted_weight: float):
        bw = Decimal(body_weight)
        c = MEN_CONSTANTS
        if sex == "female":
            c = WOMEN_CONSTANTS

        coefficient_base = (
            c["a"] + (c["b"] * bw) + (c["c"] * bw**2) + (c["d"] * bw**3) +
            (c["e"] * bw**4) + (c["f"] * bw**5)
        )
        coefficient = 600 / coefficient_base
        return round(Decimal(lifted_weight) * coefficient, 3)

