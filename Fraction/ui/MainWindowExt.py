import traceback

from PyQt6.QtWidgets import QTableWidgetItem

from Fraction.Data_access_layer.FractionDAL import FractionDAL
from Fraction.models.Fraction import Fraction

from Fraction.ui.MainWindow import Ui_MainWindow


class MainWindowExt(Ui_MainWindow):
    def setupUi(self, MainWindow):
        try:
            super().setupUi(MainWindow)
            self.MainWindow = MainWindow
            self.fraction_dal = FractionDAL()
            self.fraction_dal.connect()
            self.display_fraction()
            self.setupSignalsAndSlots()
        except:
            traceback.print_exc()
    def show(self):
        self.MainWindow.show()
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
        list_fraction = self.fraction_dal.get_all()
        list_approximate = [fraction.get_approximate() for fraction in list_fraction]
        dict_fraction = {}
        for i in range(len(list_approximate)):
            dict_fraction[list_approximate[i]] =  str(list_fraction[i])
        list_approximate = self.sort_algorithm(list_approximate)
        result = ""
        for i in range(len(list_approximate)):
            result += str(dict_fraction[list_approximate[i]])
            if i < len(list_approximate):
                result += ", "
        self.textEditDisplayFraction.append(result)
    def refresh(self):
        self.lineEditNumerator.setText("")
        self.lineEditDenominator.setText("")
        self.textEditDisplayFraction.setText("")
    def read_all(self):
        result = ""
        i = 0
        list_fraction = self.fraction_dal.get_all()
        for fraction in list_fraction:
            result += str(fraction)
            i += 1
            if i < len(list_fraction):
                result += ", "
        self.textEditDisplayFraction.append(result)
    def create_new_fraction(self):
        try:
            new_numerator = int(self.lineEditNumerator.text())
            new_denominator = int(self.lineEditDenominator.text())
            new_fraction = Fraction(new_numerator, new_denominator)
            result = self.fraction_dal.create_fraction(new_fraction)
            if result > 0:
                self.display_fraction()
        except:
            traceback.print_exc()
    def display_fraction(self):
        self.is_completed = False
        self.tableWidgetListFraction.setRowCount(0)
        list_fraction = self.fraction_dal.get_all()
        for i in range(len(list_fraction)):
            fraction_i = list_fraction[i]
            self.tableWidgetListFraction.insertRow(i)
            column_numerator = QTableWidgetItem(str(fraction_i.numerator))
            column_denominator = QTableWidgetItem(str(fraction_i.denominator))
            self.tableWidgetListFraction.setItem(i, 0, column_numerator)
            self.tableWidgetListFraction.setItem(i, 1, column_denominator)
        self.is_completed = True
    def choose_fraction(self):
        try:
            if self.is_completed == False:
                return
            current_row = self.tableWidgetListFraction.currentRow()
            current_numerator = self.tableWidgetListFraction.item(current_row, 0)
            current_denominator = self.tableWidgetListFraction.item(current_row, 1)
            self.lineEditNumerator.setText(current_numerator.text())
            self.lineEditDenominator.setText(current_denominator.text())
        except:
            traceback.print_exc()
