from Fraction.Data_access_layer.FractionDAL import FractionDAL
from Fraction.models.Fraction import Fraction

fraction_dal = FractionDAL()
fraction_dal.connect()
# fraction = Fraction(1,2)
# result = fraction_dal.create_fraction(fraction)
# if result > 0:
#     print("Add successfully")
list_fraction = fraction_dal.get_all()
for fraction in list_fraction:
    print(fraction)
