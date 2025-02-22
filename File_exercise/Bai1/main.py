from PyQt6.QtWidgets import QApplication, QMainWindow

from File_exercise.Bai1.backend.FractionWindowExt import FractionWindowExt

app = QApplication([])
myWindow = FractionWindowExt()
MainWindow = QMainWindow()
myWindow.setupUi(MainWindow)
myWindow.show()
app.exec()