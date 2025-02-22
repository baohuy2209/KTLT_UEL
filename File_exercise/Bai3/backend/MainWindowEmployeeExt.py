import traceback

from PyQt6.QtWidgets import QFileDialog, QTableWidgetItem, QMessageBox

from File_exercise.Bai3.IO.FileFactory import FileFactory
from File_exercise.Bai3.model.Employee import Employee
from File_exercise.Bai3.model.ListEmployee import ListEmployee
from File_exercise.Bai3.ui.MainWindowEmployee import Ui_MainWindow


class MainWindowEmployeeExt(Ui_MainWindow):
    def __init__(self):
        self.file_factory = FileFactory()
        self.list_employee = ListEmployee()
    def setupUi(self, MainWindow):
        super().setupUi(MainWindow)
        self.MainWindow = MainWindow
        self.setupSignalAndSlots()
    def setupSignalAndSlots(self):
        self.actionSave_File.triggered.connect(self.save_file)
        self.actionRead_File.triggered.connect(self.read_file)
        self.pushButtonCreate.clicked.connect(self.create)
        self.pushButtonStore.clicked.connect(self.store)
        self.pushButtonUpdate.clicked.connect(self.update)
        self.pushButtonDelete.clicked.connect(self.delete)
    def update(self):
        emp = self.list_employee.get_employee_by_id(self.lineEditID.text())
        if emp==None:
            return
        emp.name = self.lineEditName.text()
        emp.job = self.lineEditJob.text()
        emp.email = self.lineEditEmail.text()
        emp.phone = self.lineEditPhone.text()
        self.display()
    def delete(self):
        msgBox = QMessageBox(self.MainWindow)
        msgBox.setWindowTitle("Xác nhận xóa!")
        msgBox.setIcon(QMessageBox.Icon.Question)
        msgBox.setText(f"Bạn có chắc chắn muốn xóa nhân viên có mã =[{self.lineEditID.text()}] hay không?")
        buttons = QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No
        msgBox.setStandardButtons(buttons)
        button = msgBox.exec()
        if button == QMessageBox.StandardButton.Yes:
            result = self.list_employee.remove_employee_by_id(int(self.lineEditID.text()))
            if result:
                self.display()
            else:
                print("Some error occurs")
    def store(self):
        id = self.lineEditID.text()
        name = self.lineEditName.text()
        job = self.lineEditJob.text()
        email = self.lineEditEmail.text()
        phone = self.lineEditPhone.text()
        emp = Employee(id, name, job, email, phone)
        self.list_employee.add(emp)
        self.display()
    def create(self):
        self.lineEditPhone.setText("")
        self.lineEditEmail.setText("")
        self.lineEditName.setText("")
        self.lineEditID.setText("")
        self.lineEditJob.setText("")
    def save_file(self):
        try:
            file_filter="Định dạng Json file (*.json);;Tất cả các loại file (*)"
            filename,selected_filter=QFileDialog.getSaveFileName(self.MainWindow,filter=file_filter)
            print("tên file mà bạn muốn lưu mới:",filename)
            if filename=="":
                return
            self.file_factory.writeData(filename,self.list_employee.list_employee)
            msgBox=QMessageBox()
            msgBox.setText(f"Đã xuất dữ liệu ra định dạng JSON thành công.\n "
                           f"Nơi xuất dữ liệu [{filename}]")
            msgBox.setWindowTitle("Thông báo")
            msgBox.exec()
        except:
            traceback.print_exc()
    def read_file(self):
        file_filter = "Định dạng Json file (*.json);;Tất cả các loại file (*)"
        filename, selected_filter = QFileDialog.getOpenFileName(self.MainWindow, filter=file_filter)
        if filename == "":
            return
        employees = self.file_factory.readData(filename, Employee)
        self.list_employee.list_employee = employees
        self.display()
    def show(self):
        self.MainWindow.show()
    def display(self):
        self.is_completed = False
        self.tableWidgetListEmployee.setRowCount(0)
        for i in range(self.list_employee.get_count()):
            employee_i = self.list_employee.get_employee_by_id(str(f"emp{i+1}"))
            self.tableWidgetListEmployee.insertRow(i)
            column_id = QTableWidgetItem(str(employee_i.id))
            column_name = QTableWidgetItem(employee_i.name)
            column_job = QTableWidgetItem(employee_i.job)
            column_email = QTableWidgetItem(employee_i.email)
            column_phone = QTableWidgetItem(employee_i.phone)
            self.tableWidgetListEmployee.setItem(i, 0, column_id)
            self.tableWidgetListEmployee.setItem(i, 1, column_name)
            self.tableWidgetListEmployee.setItem(i, 2, column_job)
            self.tableWidgetListEmployee.setItem(i, 3, column_email)
            self.tableWidgetListEmployee.setItem(i, 4, column_phone)
        self.is_completed = True
    def choose_employee(self):
        if self.is_completed == False:
            return
        row = self.tableWidgetListEmployee.currentRow()
        column_id = self.tableWidgetListEmployee.item(row, 0)
        column_name = self.tableWidgetListEmployee.item(row, 1)
        column_job = self.tableWidgetListEmployee.item(row, 2)
        column_email = self.tableWidgetListEmployee.item(row, 3)
        column_phone = self.tableWidgetListEmployee.item(row, 4)
        self.lineEditID.setText(column_id.text())
        self.lineEditName.setText(column_name.text())
        self.lineEditJob.setText(column_job.text())
        self.lineEditEmail.setText(column_email.text())
        self.lineEditPhone.setText(column_phone.text())