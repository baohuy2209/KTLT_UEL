from PyQt6.QtWidgets import QApplication, QMainWindow

from List_exercise.ui.ListWindowExt import ListWindowExt

app = QApplication([])
myWindow = ListWindowExt()
myWindow.setupUi(QMainWindow())
myWindow.show()
app.exec()
