class Fraction:
    def __init__(self, numerator, denominator):
        self.numerator = numerator
        self.denominator = denominator
    def get_approximate(self):
        return round((self.numerator/self.denominator),5)
    def __str__(self):
        fraction = f"{self.numerator} / {self.denominator}"
        return fraction
