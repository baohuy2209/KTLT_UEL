class ListEmployee:
    def __init__(self):
        self.list_employee = []
    def get_count(self):
        return len(self.list_employee)
    def add(self, employee):
        self.list_employee.append(employee)
    def get_employee_by_id(self, emp_id):
        emp_temp = None
        for emp in self.list_employee:
            if emp.id == emp_id:
                emp_temp = emp
                break
        return emp_temp
    def remove_employee_by_id(self, emp_id):
        e = self.get_employee_by_id(emp_id)
        if e == None:
            return False
        else:
            self.list_employee.remove(e)
            return True