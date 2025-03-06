import hashlib
import random
import string

from PyQt6.QtWidgets import QMessageBox

from exam.Bai3.dal.UserDal import UserDAL
from exam.Bai3.model.User import User
from exam.Bai3.ui.SignupWindow import Ui_MainWindow


class SignupWindowExt(Ui_MainWindow):
    def __init__(self):
        self.length_suggest_password = 12
        self.user_dal = UserDAL()
    def setupUi(self, MainWindow):
        super().setupUi(MainWindow)
        self.MainWindow = MainWindow
        self.setupSignalAnsSlots()
    def setupSignalAnsSlots(self):
        self.pushButtonSuggestUsername.clicked.connect(self.suggest_username)
        self.pushButtonRegister.clicked.connect(self.register)
        self.pushButtonSuggestPassword.clicked.connect(self.suggest_password)
    def suggest_username(self):
        email = self.lineEditEmail.text()
        name = email.split("@")[0]
        number_random = random.randint(1, 100)
        username_suggest = name + str(number_random)
        self.lineEdiUsername.setText(username_suggest)
    def suggest_password(self):
        self.lineEditPassword.setText("")
        characters = string.ascii_letters + string.digits + string.punctuation
        password = ''.join(random.choice(characters) for _ in range(self.length_suggest_password))
        self.lineEditPassword.setText(password)
        msg = QMessageBox()
        msg.setWindowTitle("Suggestion Password: ")
        msg.setText(f"Your suggesting password: {password}")
        msg.setIcon(QMessageBox.Icon.Information)
        msg.setStandardButtons(QMessageBox.StandardButton.Close)
        button = msg.exec()
        if button == QMessageBox.StandardButton.Close:
            msg.close()
    def hash_password(self, password):
        return hashlib.sha256(password.encode()).hexdigest()
    def register(self):
        email = self.lineEditEmail.text()
        username = self.lineEdiUsername.text()
        password = self.lineEditPassword.text()
        list_current_user = self.user_dal.get_all_user()
        for user in list_current_user:
            if email == user.email:
                msg = QMessageBox()
                msg.setWindowTitle("Error !!!")
                msg.setIcon(QMessageBox.Icon.Warning)
                msg.setText("The email is existed !!!")
                msg.exec()
                return
        new_id = self.user_dal.get_len() + 1
        new_hash_password = self.hash_password(password)
        new_user = User(new_id, email, username, new_hash_password)
        self.user_dal.register_user(new_user.__dict__)
        msg = QMessageBox()
        msg.setWindowTitle("Information")
        msg.setIcon(QMessageBox.Icon.Information)
        msg.setText("You sign up successfully !!!")
        msg.exec()
    def show(self):
        self.MainWindow.show()