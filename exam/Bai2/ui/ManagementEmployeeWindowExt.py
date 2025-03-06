import random

from PyQt6.QtWidgets import QTableWidgetItem, QMainWindow

from exam.Bai2.data_access_layer.EmployeeDAL import EmployeeDAL
from exam.Bai2.model.Employee import Employee
from exam.Bai2.ui.ManagementEmployeeWindow import Ui_MainWindow
from exam.Bai2.ui.RewardWindowExt import RewardWindowExt


class ManagementEmployeeWindowExt(Ui_MainWindow):
    def __init__(self):
        self.employee_dal = EmployeeDAL()
        self.reward_window = None
    def setupUi(self, MainWindow):
        super().setupUi(MainWindow)
        self.MainWindow = MainWindow
        self.setupSignalAndSlots()
        self.display()
    def setupSignalAndSlots(self):
        self.pushButtonCreate.clicked.connect(self.create)
        self.pushButtonDelete.clicked.connect(self.delete)
        self.pushButtonStore.clicked.connect(self.store)
        self.pushButtonUpdate.clicked.connect(self.update)
        self.tableWidgetListEmployee.itemSelectionChanged.connect(self.choose_emp)
        self.actionWheel_of_reward.triggered.connect(self.open_wheel)
    def open_wheel(self):
        WheelHome = QMainWindow()
        self.reward_window = RewardWindowExt()
        self.reward_window.setupUi(WheelHome)
        self.reward_window.list_employee = self.employee_dal.get_all_employee()
        self.reward_window.show()
    def choose_emp(self):
        if self.is_completed == False:
            return
        row = self.tableWidgetListEmployee.currentRow()
        column_id = self.tableWidgetListEmployee.item(row, 0)
        column_name = self.tableWidgetListEmployee.item(row, 1)
        column_email = self.tableWidgetListEmployee.item(row, 2)
        column_phone = self.tableWidgetListEmployee.item(row, 3)
        column_address = self.tableWidgetListEmployee.item(row, 4)
        self.lineEditID.setText(column_id.text())
        self.lineEditName.setText(column_name.text())
        self.lineEditPhone.setText(column_phone.text())
        self.lineEditPhone.setText(column_phone.text())
        self.lineEditEmail.setText(column_email.text())
        self.lineEditAddress.setText(column_address.text())
    def display(self):
        list_employee = self.employee_dal.get_all_employee()
        self.is_completed = False
        self.tableWidgetListEmployee.setRowCount(0)
        for i in range(len(list_employee)):
            emp_i = list_employee[i]
            self.tableWidgetListEmployee.insertRow(i)
            column_id = QTableWidgetItem(str(emp_i.employeeid))
            column_name = QTableWidgetItem(str(emp_i.name))
            column_phone = QTableWidgetItem(str(emp_i.phone))
            column_email = QTableWidgetItem(str(emp_i.email))
            column_address = QTableWidgetItem(str(emp_i.address))
            self.tableWidgetListEmployee.setItem(i, 0, column_id)
            self.tableWidgetListEmployee.setItem(i, 1, column_name)
            self.tableWidgetListEmployee.setItem(i, 2, column_email)
            self.tableWidgetListEmployee.setItem(i, 3, column_phone)
            self.tableWidgetListEmployee.setItem(i, 4, column_address)
        self.is_completed = True
    def update(self):
        id = self.lineEditID.text()
        new_name = self.lineEditName.text()
        new_email = self.lineEditEmail.text()
        new_phone = self.lineEditPhone.text()
        new_address = self.lineEditAddress.text()
        new_lottery = random.randint(1, 100)
        emp = Employee(id, new_name, new_email, new_phone, new_address, new_lottery)
        self.employee_dal.update(emp)
        self.display()
    def store(self):
        id = self.lineEditID.text()
        email = self.lineEditEmail.text()
        name = self.lineEditName.text()
        phone = self.lineEditPhone.text()
        address = self.lineEditAddress.text()
        lottery = random.randint(1, 100)
        new_emp = Employee(employeeid=id, name=name, email=email, phone=phone, address=address, lottery = lottery)
        self.employee_dal.add(new_emp)
        self.employee_dal.store_new()
        self.display()
    def delete(self):
        id = self.lineEditID.text()
        self.employee_dal.delete(id)
        self.display()
    def create(self):
        self.lineEditID.setText("")
        self.lineEditEmail.setText("")
        self.lineEditName.setText("")
        self.lineEditPhone.setText("")
        self.lineEditAddress.setText("")
    def show(self):
        self.MainWindow.show()
