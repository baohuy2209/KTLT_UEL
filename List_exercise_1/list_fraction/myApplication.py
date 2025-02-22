from PyQt6.QtWidgets import QApplication, QMainWindow

from List_exercise_1.list_fraction.backend.FractionMainWindowExt import FractionMainWindowExt

app = QApplication([])
myWindow = FractionMainWindowExt()
MainWindow = QMainWindow()
myWindow.setupUi(MainWindow)
myWindow.show()
app.exec()