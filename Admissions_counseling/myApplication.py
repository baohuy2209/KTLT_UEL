from PyQt6.QtWidgets import QApplication, QMainWindow

from Admissions_counseling.backend.AdmissionsCounSelingExt import AdmissionsCounSellingExt

app = QApplication([])
myWindow = AdmissionsCounSellingExt()
MainWindow = QMainWindow()
myWindow.setupUi(MainWindow)
myWindow.show()
app.exec()
