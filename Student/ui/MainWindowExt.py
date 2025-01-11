import traceback

from PyQt6.QtWidgets import QTableWidgetItem

from Student.data_access_layer.StudentDAL import StudentDAL
from Student.ui.MainWindow import Ui_MainWindow

class MainWindowExt(Ui_MainWindow):
    def setupUi(self, MainWindow):
        try:
            super().setupUi(MainWindow)
            self.MainWindow = MainWindow
            self.student_dal = StudentDAL()
            self.student_dal.connect()
            self.setupSignalAndSlots()
        except:
            traceback.print_exc()
    def setupSignalAndSlots(self):
        pass
    def display_student(self):
        self.is_completed = False
        students = self.student_dal.get_all()
        for student in students:
            print(student)
        # for i in range(len(students)):
        #     student_i = students[i]
        #     self.tableWidgetListStudent.insertRow(i)
        #     column_studentid = QTableWidgetItem(str(student_i.StudentID))
        #     column_fullname = QTableWidgetItem(str(student_i.FullName))
        #     column_phone = QTableWidgetItem(str(student_i.Phone))
        #     column_email = QTableWidgetItem(str(student_i.Email))
        #     column_address = QTableWidgetItem(str(student_i.Address))
        #     column_gender = QTableWidgetItem(str(student_i.Gender))
        #     column_grade = QTableWidgetItem(str(student_i.Grade))
        #     self.tableWidgetListStudent.setItem(i, 0, column_studentid)
        #     self.tableWidgetListStudent.setItem(i, 1, column_fullname)
        #     self.tableWidgetListStudent.setItem(i, 2, column_phone)
        #     self.tableWidgetListStudent.setItem(i, 3, column_email)
        #     self.tableWidgetListStudent.setItem(i, 4, column_address)
        #     self.tableWidgetListStudent.setItem(i, 5, column_gender)
        #     self.tableWidgetListStudent.setItem(i, 6, column_grade)
        self.is_completed = True
    def show(self):
        self.MainWindow.show()