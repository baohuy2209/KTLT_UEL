from Fraction.models.Fraction import Fraction

fraction_1 = Fraction(1,3)
fraction_2 = Fraction(2, 3)
print(fraction_1)
print(fraction_2)
list_fraction = []
list_fraction.append(fraction_1)
list_fraction.append(fraction_2)
for fraction in list_fraction:
    print(fraction)
# list_fraction.add_new(fraction_1)
# list_fraction.add_new(fraction_2)
# list_fraction.print_list_fraction()