class ListFraction:
    def __init__(self):
        self.list_fraction = []
    def get_count(self):
        return len(self.list_fraction)
    def enter_list(self, input_list):
        for i in input_list:
            self.list_fraction.append(i)
    def add(self, fraction):
        self.list_fraction.append(fraction)
    def get_string(self):
        list_fraction = ""
        for i in range(len(self.list_fraction)):
            list_fraction += str(self.list_fraction[i])
            if i < len(self.list_fraction) - 1:
                list_fraction += ","
        return list_fraction