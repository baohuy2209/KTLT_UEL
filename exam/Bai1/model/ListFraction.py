from exam.Bai1.model.Fraction import Fraction

def get_key_from_value(d, value):
    key_result = 0
    for k, v in d.items():
        if v == value:
            key_result = k
            break
    return key_result
class ListFraction:
    def __init__(self):
        self.list_fraction = []
    def get_all(self):
        return self.list_fraction
    def add(self, fraction):
        self.list_fraction.append(fraction)
    def get_length(self):
        return len(self.list_fraction)
    def get_fraction_by_id(self, i):
        return self.list_fraction[i]
    def get_all_approximate(self):
        my_dict = {}
        for i in range(len(self.list_fraction)):
            approximate = self.list_fraction[i].approximate()
            my_dict[i] = approximate
        return my_dict
    def max_fraction(self):
        my_dict = self.get_all_approximate()
        max_fraction = my_dict[0]
        for i in range(1,len(self.list_fraction)):
            if self.list_fraction[i].approximate() > max_fraction:
                max_fraction = my_dict[i]
        max_fraction = self.list_fraction[get_key_from_value(my_dict, max_fraction)]
        return max_fraction
    def sum(self):
        result_fraction = Fraction(0, 1)
        for i in range(len(self.list_fraction)):
            result_fraction.sum(self.list_fraction[i])
        return result_fraction