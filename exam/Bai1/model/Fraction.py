class Fraction:
    def __init__(self, numerator = None, denominator = None):
        self.numerator = numerator
        self.denominator = denominator
    def gcd(self, a, b):
        if a < 0:
            a = -a
        if b < 0:
            b = -b
        while a != b:
            if a < b:
                b = b - a
            else:
                a = a - b
        return a
    def simple_fraction(self, a, b):
        gcd = self.gcd(a,b)
        a /= gcd
        b /= gcd
    def sum(self, another_fraction):
        self.numerator = self.numerator*another_fraction.denominator + another_fraction.numerator*self.denominator
        self.denominator = self.denominator*another_fraction.denominator
    def approximate(self):
        return round(self.numerator / self.denominator, 2)
    def __str__(self):
        info = f"{self.numerator}/{self.denominator}"
        return info