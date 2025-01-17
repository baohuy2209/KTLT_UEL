from PyQt6.QtWidgets import QMessageBox
from sympy.solvers.diophantine.diophantine import length

from List_exercise.Bai1 import new_element1
from List_exercise.ui.ListWindow import Ui_MainWindow


class ListWindowExt(Ui_MainWindow):
    def __init__(self):
        self.list = []
    def setupUi(self, MainWindow):
        super().setupUi(MainWindow)
        self.MainWindow = MainWindow
        self.setupSignalsAndSlot()
    def setupSignalsAndSlot(self):
        self.pushButtonEnter.clicked.connect(self.enter_list)
        self.pushButtonRefresh.clicked.connect(self.refresh)
        self.pushButtonDisplay.clicked.connect(self.display)
        self.pushButtonSort.clicked.connect(self.sort_list)
        self.pushButtonInsert.clicked.connect(self.insert)
        self.pushButton.clicked.connect(self.deleteAll)
        self.pushButtonUpdate.clicked.connect(self.update)
    def deleteAll(self):
        self.list.clear()
    def update(self):
        new_element = self.lineEditNewElementUpdate.text()
        location = self.lineEditUpdateIndex.text()
        if new_element == '':
            msg = QMessageBox()
            msg.setText("Empty element")
            msg.setWindowTitle("Error !!!")
            msg.exec()
        if location == '' or int(location) < len(self.list):
            msg = QMessageBox()
            msg.setText("Location have error about index of range or empty!!!")
            msg.setWindowTitle("Error !!!")
            msg.exec()
        for i in range(len(self.list)):
            if i == location:
                self.list[i] = new_element
                break
        self.display()
    def insert(self):
        new_element = self.lineEditElementInsert.text()
        location = self.lineEditInsertIndex.text()
        if new_element == '':
            msg = QMessageBox()
            msg.setText("Empty element")
            msg.setWindowTitle("Error !!!")
            msg.exec()
        if location == '' or int(location) < len(self.list):
            msg = QMessageBox()
            msg.setText("Location have error about index of range or empty!!!")
            msg.setWindowTitle("Error !!!")
            msg.exec()
        self.list.insert(int(location), int(new_element))
        self.display()
    def sort_list(self):
        list_sort = self.sort(self.list)
        list_str = ''
        length = len(list_sort)
        for i in range(length):
            list_str += str(list_sort[i])
            if i < length - 1:
                list_str += ','
        self.textEditDisplay.setText(list_str)
    def sort(self, list_sort):
        for i in range(len(list_sort)):
            for j in range(i+1, len(list_sort)):
                if list_sort[i] > list_sort[j]:
                    list_sort[i], list_sort[j] = list_sort[j], list_sort[i]
        return list_sort
    def display(self):
        list_str = ""
        length = len(self.list)
        for i in range(length):
            list_str += str(self.list[i])
            if i < length - 1:
                list_str += ','
        self.textEditDisplay.setText(list_str)

    def refresh(self):
        self.lineEditInsertIndex.setText("")
        self.lineEditUpdateIndex.setText("")
        self.lineEditElementInsert.setText("")
        self.lineEditNewElementUpdate.setText("")
        self.lineEditEnter.setText("")
        self.textEditDisplay.setText("")
    def enter_list(self):
        input = self.lineEditEnter.text()
        if input == '':
            msg = QMessageBox()
            msg.setText("Empty list")
            msg.setWindowTitle("Error !!!")
            msg.exec()
        input_list = [int(element) for element in input.split(',')]
        for i in input_list:
            self.list.append(i)
        msg = QMessageBox()
        msg.setText("Enter new list successfully")
        msg.setWindowTitle("Announce")
        msg.exec()
    def show(self):
        self.MainWindow.show()