from PyQt6.QtWidgets import QApplication, QMainWindow

from exam.Bai3.ui.SignupWindowExt import SignupWindowExt

app = QApplication([])
MainWindow = QMainWindow()
myWindow = SignupWindowExt()
myWindow.setupUi(MainWindow)
myWindow.show()
app.exec()