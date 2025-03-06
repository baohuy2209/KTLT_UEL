from PyQt6.QtWidgets import QApplication, QMainWindow

from exam.Bai2.ui.ManagementEmployeeWindowExt import ManagementEmployeeWindowExt

app = QApplication([])
MainWindow = QMainWindow()
myWindow = ManagementEmployeeWindowExt()
myWindow.setupUi(MainWindow)
myWindow.show()
app.exec()