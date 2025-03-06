from PyQt6.QtWidgets import QApplication, QMainWindow

from exam.Bai1.backend.FractionWindowExt import FractionWindowExt

app = QApplication([])
MainWindow = QMainWindow()
myWindow = FractionWindowExt()
myWindow.setupUi(MainWindow)
myWindow.show()
app.exec()