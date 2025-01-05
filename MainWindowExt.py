import traceback

from PyQt6.QtWidgets import QTableWidgetItem

from Fraction.models.Fraction import Fraction
from Fraction.test.testListFraction import fraction

from MainWindow import Ui_MainWindow


class MainWindowExt(Ui_MainWindow):
    def setupUi(self, MainWindow):
        super().setupUi(MainWindow)
        self.MainWindow = MainWindow
        self.list_fraction = []
        self.setupSignalsAndSlots()
    def setupSignalsAndSlots(self):
        self.pushButtonCreate.clicked.connect(self.create_new_fraction)
        self.pushButtonReadAll.clicked.connect(self.read_all)
        self.pushButtonRefresh.clicked.connect(self.refresh)
        self.pushButtonSort.clicked.connect(self.sort)
    def sort_algorithm(self, list_sort):
        for i in range(len(list_sort)):
            for j in range(i+1, len(list_sort)):
                if list_sort[i] < list_sort[j]:
                    list_sort[i], list_sort[j] = list_sort[j], list_sort[i]
        return list_sort
    def sort(self):
        list_approximate = [fraction.get_approximate() for fraction in self.list_fraction]
        list_approximate = self.sort_algorithm(list_approximate)
        print(list_approximate)
        result = ""
        for i in range(len(list_approximate)):
            result += str(list_approximate[i])
            if i < len(list_approximate):
                result += ", "
        self.textEditDisplayFraction.append(result)
    def refresh(self):
        self.lineEditNumerator.setText("")
        self.lineEditDenominator.setText("")
    def read_all(self):
        result = ""
        i = 0
        for fraction in self.list_fraction:
            result += str(fraction)
            i += 1
            if i < len(self.list_fraction):
                result += ", "
        self.textEditDisplayFraction.append(result)
    def create_new_fraction(self):
        try:
            new_numerator = int(self.lineEditNumerator.text())
            new_denominator = int(self.lineEditDenominator.text())
            new_fraction = Fraction(new_numerator, new_denominator)
            self.list_fraction.append(new_fraction)
            print(new_fraction)
            self.display_fraction()
        except:
            traceback.print_exc()
    def display_fraction(self):
        self.is_completed = False
        self.tableWidgetListFraction.setRowCount(0)
        for i in range(len(self.list_fraction)):
            fraction_i = self.list_fraction[i]
            self.tableWidgetListFraction.insertRow(i)
            column_numerator = QTableWidgetItem(str(fraction_i.numerator))
            column_denominator = QTableWidgetItem(str(fraction_i.denominator))
            self.tableWidgetListFraction.setItem(i, 0, column_numerator)
            self.tableWidgetListFraction.setItem(i, 1, column_denominator)
        self.is_completed = True
    def choose_fraction(self):
        if self.is_completed == False:
            return
        current_row = self.tableWidgetListFraction.currentRow()
        current_numerator = self.tableWidgetListFraction.item(current_row, 0)
        current_denominator = self.tableWidgetListFraction.item(current_row, 1)
        self.lineEditNumerator.setText(current_numerator.text())
        self.lineEditDenominator.setText(current_denominator.text())
        self.refresh()
    def show(self):
        self.MainWindow.show()