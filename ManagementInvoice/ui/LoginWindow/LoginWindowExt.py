import traceback

from PyQt6.QtWidgets import QMessageBox, QMainWindow

from ManagementInvoice.data_access_layer.UserDAL import UserDAL
from ManagementInvoice.ui.LoginWindow.LoginWindow import Ui_MainWindow
from ManagementInvoice.ui.MainWindow.MainWindowExt import MainWindowExt


class LoginWindowExt(Ui_MainWindow):
    def __init__(self):
        self.user_dal = UserDAL()
        self.list_user = self.user_dal.get_all_users()
        self.main_window = None
        self.ano_qmainwindow = None
    def setupUi(self, MainWindow):
        super().setupUi(MainWindow)
        self.MainWindow = MainWindow
        self.setupSignalAndSlots()
    def setupSignalAndSlots(self):
        self.pushButtonLogin.clicked.connect(self.login)
    def login(self):
        try:
            username = self.lineEditUsername.text()
            password = self.lineEditPassword.text()
            check_exist = False
            for user in self.list_user:
                if username == user.username and password == user.password:
                    check_exist = True
                    break
            if not check_exist:
                msg = QMessageBox()
                msg.setText("Doesn't exist this account")
                msg.setWindowTitle("Error !!!")
                msg.exec()
            else:
                self.MainWindow.close()
                msg = QMessageBox()
                msg.setText("You have successfully logged in.")
                msg.setWindowTitle("Announcement")
                msg.exec()
                self.ano_qmainwindow = QMainWindow()
                self.main_window = MainWindowExt()
                self.main_window.setupUi(self.ano_qmainwindow)
                self.main_window.show()
        except:
            traceback.print_exc()
    def show(self):
        self.MainWindow.show()