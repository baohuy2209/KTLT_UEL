from List_exercise_1.list_fraction.model.Fraction import Fraction
from List_exercise_1.list_fraction.ui.FractionMainWindow import Ui_MainWindow


class FractionMainWindowExt(Ui_MainWindow):
    def setupUi(self, MainWindow):
        super().setupUi(MainWindow)
        self.MainWindow = MainWindow
        self.setupSignalAndSlots()
    def setupSignalAndSlots(self):
        self.pushButtonSum.clicked.connect(self.sum_fraction)
    def sum_fraction(self):
        fraction_text = self.textEditSum.toPlainText()
        list_fraction_text = fraction_text.split(",")
        list_fraction = []
        for fraction in list_fraction_text:
            numerator, denominator = fraction.split("/")
            temp_fraction = Fraction(int(numerator), int(denominator))
            list_fraction.append(temp_fraction)
        sum_fraction = Fraction(list_fraction[0].numerator,list_fraction[0].denominator)
        for i in range(1,len(list_fraction)):
            sum_fraction.sum(sum_fraction, list_fraction[i])
        self.lineEditResult.setText(str(sum_fraction))
    def show(self):
        self.MainWindow.show()
