class ListStudent:
    def __init__(self):
        self.list_student = []
    def get_count(self):
        return len(self.list_student)
    def enter_list(self, input_list):
        for i in input_list:
            self.list_student.append(i)
    def add(self, student):
        self.list_student.append(student)
