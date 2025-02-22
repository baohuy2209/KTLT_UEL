from PyQt6.QtWidgets import QApplication, QMainWindow

from File_exercise.Bai2.ui.MainWindowExt import MainWindowExt

app = QApplication([])
myWindow = MainWindowExt()
MainWindow = QMainWindow()
myWindow.setupUi(MainWindow)
myWindow.show()
app.exec()