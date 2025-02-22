from PyQt6.QtWidgets import QApplication, QMainWindow

from File_exercise.Bai3.backend.MainWindowEmployeeExt import MainWindowEmployeeExt

app = QApplication([])
myWindow = MainWindowEmployeeExt()
myWindow.setupUi(QMainWindow())
myWindow.show()
app.exec()