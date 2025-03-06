from exam.Bai2.data_access_layer.EmployeeDAL import EmployeeDAL
from exam.Bai2.model.Employee import Employee

employee_dal = EmployeeDAL()
list_employee = employee_dal.get_all_employee()
for emp in list_employee:
    print(emp)