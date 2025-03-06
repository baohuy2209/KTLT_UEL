import os

from exam.Bai2.IO.FileFactory import FileFactory
from exam.Bai2.model.Employee import Employee


class EmployeeDAL:
    def __init__(self):
        self.list_employee = []
        self.file_factory = FileFactory()
    def add(self, new_emp):
        self.list_employee.append(new_emp)
    def get_filepath(self, path):
        current_dir = os.path.dirname(__file__)
        filepath = os.path.join(current_dir, path)
        return str(filepath)
    def store_new(self):
        filepath = self.get_filepath("../data/employee.txt")
        result = ""
        for i in range(len(self.list_employee)):
            result += str(self.list_employee[i])
            if i < len(self.list_employee) - 1:
                result += "\n"
        self.file_factory.writeData(filepath, result)
    def get_index_by_id(self, id):
        index = 0
        for i in range(len(self.list_employee)):
            if self.list_employee[i].employeeid == id:
                index = i
                break
        return index
    def update(self, new_emp):
        index = self.get_index_by_id(new_emp.employeeid)
        self.list_employee[index] = new_emp
        self.store_new()
    def delete(self, id):
        index = self.get_index_by_id(id)
        self.list_employee.pop(index)
        self.store_new()
    def get_all_employee(self):
        filepath = self.get_filepath("../data/employee.txt")
        list_employee = self.file_factory.readData(filepath, "r")
        list_employee = list_employee.split("\n")
        my_list_employee = []
        for emp in list_employee:
            temp_list = emp.split(" | ")
            empid = temp_list[0]
            name = temp_list[1]
            email = temp_list[2]
            phone = temp_list[3]
            address = temp_list[4]
            lottery = int(temp_list[5])
            new_emp = Employee(empid, name, email, phone, address, lottery)
            my_list_employee.append(new_emp)
        self.list_employee = my_list_employee
        return self.list_employee

