class Fraction:
    def __init__(self, numerator, denominator):
        self.numerator = numerator
        self.denominator = denominator
    def GCD(self, a, b):
        while a != b:
            if a > b:
                a = a - b
            else:
                b = b - a
        return a
    def simplify_fraction(self):
        gcd = self.GCD(self.numerator, self.denominator)
        self.numerator /= gcd
        self.denominator /= gcd
    def sum(self, fraction1, fraction2):
        self.numerator = fraction1.numerator*fraction2.denominator + fraction2.numerator*fraction1.denominator
        self.denominator = fraction1.denominator*fraction2.denominator
        self.simplify_fraction()
    def __str__(self):
        info = f"{self.numerator} / {self.denominator}"
        return info