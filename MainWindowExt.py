import traceback

from PyQt6.QtWidgets import QTableWidgetItem

from Fraction.models.Fraction import Fraction
from Fraction.models.ListFraction import ListFraction
from MainWindow import Ui_MainWindow


class MainWindowExt(Ui_MainWindow):
    def __int__(self):
        self.MainWindow = None
        self.list_fraction = ListFraction()
    def setupUi(self, MainWindow):
        super().setupUi(MainWindow)
        self.MainWindow = MainWindow
        self.setupSignalsAndSlots()
    def setupSignalsAndSlots(self):
        self.pushButtonCreate.clicked.connect(self.create_new_fraction)
        self.pushButtonReadAll.clicked.connect(self.read_all)
    def read_all(self):
        result_string = str(self.list_fraction)
        self.lineEditAllFraction.setText(result_string)
    def create_new_fraction(self):
        try:
            new_numerator = int(self.lineEditNumerator.text())
            new_denominator = int(self.lineEditDenominator.text())
            new_fraction = Fraction(new_numerator, new_denominator)
            self.list_fraction.add_new(new_fraction)
            print(new_fraction)
            self.display_fraction()
        except:
            traceback.print_exc()
    def display_fraction(self):
        self.is_completed = False
        self.tableWidgetListFraction.setRowCount(0)
        for i in range(self.list_fraction.count()):
            fraction_i = self.list_fraction[i]
            self.tableWidgetListFraction.insertRow(i)
            column_stt = QTableWidgetItem(str(i))
            column_numerator = QTableWidgetItem(str(fraction_i.numerator))
            column_denominator = QTableWidgetItem(str(fraction_i.denominator))
            self.tableWidgetListFraction.setItem(i, 0, column_stt)
            self.tableWidgetListFraction.setItem(i, 1, column_numerator)
            self.tableWidgetListFraction.setItem(i, 2, column_denominator)
        self.is_completed = True

    def show(self):
        self.MainWindow.show()