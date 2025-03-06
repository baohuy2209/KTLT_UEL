import random

from PyQt6.QtWidgets import QMessageBox

from exam.Bai1.model.Fraction import Fraction
from exam.Bai1.model.ListFraction import ListFraction
from exam.Bai1.ui.FractionWindow import Ui_MainWindow


class FractionWindowExt(Ui_MainWindow):
    def __init__(self):
        self.list_fraction = ListFraction()
    def setupUi(self, MainWindow):
        super().setupUi(MainWindow)
        self.MainWindow = MainWindow
        self.setupSignalAndSlots()
    def setupSignalAndSlots(self):
        self.pushButtonCreate.clicked.connect(self.create_100_fraction)
        self.pushButtonSum.clicked.connect(self.sum)
        self.pushButtonDisplay.clicked.connect(self.display)
        self.pushButtonMaxFraction.clicked.connect(self.max_fraction)
        self.pushButtonClearAll.clicked.connect(self.clear_all)
        self.pushButtonSortAscending.clicked.connect(self.sort_ascending)
        self.pushButtonSortDescending.clicked.connect(self.sort_descending)
    def sort_descending_algorithm(self, list_sort):
        for i in range(len(list_sort)):
            for j in range(i+1, len(list_sort)):
                if list_sort[i] < list_sort[j]:
                    list_sort[i], list_sort[j] = list_sort[j], list_sort[i]
        return list_sort
    def sort_descending(self):
        list_fraction = self.list_fraction.get_all()
        list_approximate = [fraction.approximate() for fraction in list_fraction]
        dict_fraction = {}
        for i in range(len(list_approximate)):
            dict_fraction[list_approximate[i]] = str(list_fraction[i])
        list_approximate = self.sort_descending_algorithm(list_approximate)
        result = ""
        for i in range(len(list_approximate)):
            result += str(dict_fraction[list_approximate[i]])
            if i < len(list_approximate) - 1:
                result += ", "
            else:
                result += "."
        self.textEditFraction.setText(f"List fraction descending: {result}")
    def max_fraction(self):
        max_fraction = self.list_fraction.max_fraction()
        self.lineEditResult.setText(f"Max fraction: {max_fraction}")
    def clear_all(self):
        self.lineEditResult.setText("")
        self.textEditFraction.setText("")
    def sort_ascending_algorithm(self, list_sort):
        for i in range(len(list_sort)):
            for j in range(i+1, len(list_sort)):
                if list_sort[i] > list_sort[j]:
                    list_sort[i], list_sort[j] = list_sort[j], list_sort[i]
        return list_sort
    def sort_ascending(self):
        list_fraction = self.list_fraction.get_all()
        list_approximate = [fraction.approximate() for fraction in list_fraction]
        dict_fraction = {}
        for i in range(len(list_approximate)):
            dict_fraction[list_approximate[i]] = str(list_fraction[i])
        list_approximate = self.sort_ascending_algorithm(list_approximate)
        result = ""
        for i in range(len(list_approximate)):
            result += str(dict_fraction[list_approximate[i]])
            if i < len(list_approximate) - 1:
                result += ", "
            else:
                result += "."
        self.textEditFraction.setText(f"List fraction ascending {result}")
    def display(self):
        str_display = ""
        for i in range(self.list_fraction.get_length()):
            current_fraction = self.list_fraction.get_fraction_by_id(i)
            str_display += str(current_fraction)
            if i < self.list_fraction.get_length() - 1:
                str_display += ", "
            else:
                str_display += "."
        self.textEditFraction.setText(str_display)
    def sum(self):
        result = self.list_fraction.sum()
        self.lineEditResult.setText(f"Sum of 100 fractions: {result}")
    def create_100_fraction(self):
        for _ in range(100):
            numerator = random.randint(-100, 100)
            denominator = random.randint(1, 100)
            new_fraction = Fraction(numerator, denominator)
            self.list_fraction.add(new_fraction)
        msg = QMessageBox()
        msg.setWindowTitle("Announcement")
        msg.setText("Create 100 fractions successfully !!!")
        msg.setIcon(QMessageBox.Icon.Information)
        msg.setStandardButtons(QMessageBox.StandardButton.Close)
        button = msg.exec()
        if button == QMessageBox.StandardButton.Close:
            msg.close()

    def show(self):
        self.MainWindow.show()