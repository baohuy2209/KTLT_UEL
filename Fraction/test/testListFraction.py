from Fraction.models.Fraction import Fraction
from Fraction.models.ListFraction import ListFraction

list_fraction = ListFraction()
fraction_1 = Fraction(1,3)
fraction_2 = Fraction(2, 3)
list_fraction.add_new(fraction_1)
list_fraction.add_new(fraction_2)
list_fraction.print_list_fraction()