class ListFraction:
    def __int__(self):
        self.listFraction = []
    def add_new(self, new_element):
        self.listFraction.append(new_element)
    def print_list_fraction(self):
        for fraction in self.listFraction:
            info = str(fraction)
            print(info)
    def count(self):
        return len(self.listFraction)