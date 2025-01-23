from PyQt6.QtWidgets import QApplication, QMainWindow

from ManagementInvoice.ui.LoginWindow.LoginWindowExt import LoginWindowExt

app = QApplication([])
loginWindowExt = LoginWindowExt()
MainWindow = QMainWindow()
loginWindowExt.setupUi(MainWindow)
loginWindowExt.show()
app.exec()
