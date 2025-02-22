from PyQt6.QtWidgets import QApplication, QMainWindow

from List_exercise_1.Essay.backend.EssayWindowExt import EssayMainWindowExt

app = QApplication([])
myWindow = EssayMainWindowExt()
MainWindow = QMainWindow()
myWindow.setupUi(MainWindow)
myWindow.show()
app.exec()