# Form implementation generated from reading ui file 'C:\Users\ADMIN\PycharmProjects\KTLT_UEL\Admissions_counseling\ui\AdmissionsCounSelingWindow.ui'
#
# Created by: PyQt6 UI code generator 6.8.0
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(804, 1100)
        MainWindow.setStyleSheet("font-size:16px; ")
        self.centralwidget = QtWidgets.QWidget(parent=MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.scrollArea = QtWidgets.QScrollArea(parent=self.centralwidget)
        self.scrollArea.setGeometry(QtCore.QRect(10, 10, 781, 1031))
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName("scrollArea")
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 779, 1029))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.groupBox = QtWidgets.QGroupBox(parent=self.scrollAreaWidgetContents)
        self.groupBox.setGeometry(QtCore.QRect(0, 390, 771, 281))
        self.groupBox.setObjectName("groupBox")
        self.label = QtWidgets.QLabel(parent=self.groupBox)
        self.label.setGeometry(QtCore.QRect(30, 30, 51, 41))
        self.label.setObjectName("label")
        self.lineEditMath = QtWidgets.QLineEdit(parent=self.groupBox)
        self.lineEditMath.setGeometry(QtCore.QRect(130, 30, 151, 41))
        self.lineEditMath.setObjectName("lineEditMath")
        self.label_2 = QtWidgets.QLabel(parent=self.groupBox)
        self.label_2.setGeometry(QtCore.QRect(30, 90, 91, 41))
        self.label_2.setObjectName("label_2")
        self.lineEditLiterature = QtWidgets.QLineEdit(parent=self.groupBox)
        self.lineEditLiterature.setGeometry(QtCore.QRect(130, 90, 151, 41))
        self.lineEditLiterature.setObjectName("lineEditLiterature")
        self.label_3 = QtWidgets.QLabel(parent=self.groupBox)
        self.label_3.setGeometry(QtCore.QRect(30, 150, 71, 41))
        self.label_3.setObjectName("label_3")
        self.lineEditPhysics = QtWidgets.QLineEdit(parent=self.groupBox)
        self.lineEditPhysics.setGeometry(QtCore.QRect(130, 150, 151, 41))
        self.lineEditPhysics.setObjectName("lineEditPhysics")
        self.label_4 = QtWidgets.QLabel(parent=self.groupBox)
        self.label_4.setGeometry(QtCore.QRect(30, 210, 81, 41))
        self.label_4.setObjectName("label_4")
        self.lineEditChemistry = QtWidgets.QLineEdit(parent=self.groupBox)
        self.lineEditChemistry.setGeometry(QtCore.QRect(130, 210, 151, 41))
        self.lineEditChemistry.setObjectName("lineEditChemistry")
        self.label_5 = QtWidgets.QLabel(parent=self.groupBox)
        self.label_5.setGeometry(QtCore.QRect(390, 30, 81, 41))
        self.label_5.setObjectName("label_5")
        self.lineEditBiology = QtWidgets.QLineEdit(parent=self.groupBox)
        self.lineEditBiology.setGeometry(QtCore.QRect(490, 30, 151, 41))
        self.lineEditBiology.setObjectName("lineEditBiology")
        self.label_6 = QtWidgets.QLabel(parent=self.groupBox)
        self.label_6.setGeometry(QtCore.QRect(390, 90, 91, 41))
        self.label_6.setObjectName("label_6")
        self.lineEditGeography = QtWidgets.QLineEdit(parent=self.groupBox)
        self.lineEditGeography.setGeometry(QtCore.QRect(490, 90, 151, 41))
        self.lineEditGeography.setObjectName("lineEditGeography")
        self.label_7 = QtWidgets.QLabel(parent=self.groupBox)
        self.label_7.setGeometry(QtCore.QRect(390, 150, 91, 41))
        self.label_7.setObjectName("label_7")
        self.lineEditEnglish = QtWidgets.QLineEdit(parent=self.groupBox)
        self.lineEditEnglish.setGeometry(QtCore.QRect(490, 150, 151, 41))
        self.lineEditEnglish.setObjectName("lineEditEnglish")
        self.label_8 = QtWidgets.QLabel(parent=self.groupBox)
        self.label_8.setGeometry(QtCore.QRect(390, 210, 91, 41))
        self.label_8.setObjectName("label_8")
        self.lineEditHistory = QtWidgets.QLineEdit(parent=self.groupBox)
        self.lineEditHistory.setGeometry(QtCore.QRect(490, 210, 151, 41))
        self.lineEditHistory.setObjectName("lineEditHistory")
        self.groupBox_2 = QtWidgets.QGroupBox(parent=self.scrollAreaWidgetContents)
        self.groupBox_2.setGeometry(QtCore.QRect(10, 10, 761, 361))
        self.groupBox_2.setObjectName("groupBox_2")
        self.label_9 = QtWidgets.QLabel(parent=self.groupBox_2)
        self.label_9.setGeometry(QtCore.QRect(30, 40, 81, 31))
        self.label_9.setObjectName("label_9")
        self.lineEditFullname = QtWidgets.QLineEdit(parent=self.groupBox_2)
        self.lineEditFullname.setGeometry(QtCore.QRect(120, 30, 631, 41))
        self.lineEditFullname.setObjectName("lineEditFullname")
        self.label_10 = QtWidgets.QLabel(parent=self.groupBox_2)
        self.label_10.setGeometry(QtCore.QRect(30, 90, 81, 31))
        self.label_10.setObjectName("label_10")
        self.lineEditAddress = QtWidgets.QLineEdit(parent=self.groupBox_2)
        self.lineEditAddress.setGeometry(QtCore.QRect(120, 90, 631, 41))
        self.lineEditAddress.setObjectName("lineEditAddress")
        self.label_11 = QtWidgets.QLabel(parent=self.groupBox_2)
        self.label_11.setGeometry(QtCore.QRect(30, 150, 81, 31))
        self.label_11.setObjectName("label_11")
        self.lineEditSchool = QtWidgets.QLineEdit(parent=self.groupBox_2)
        self.lineEditSchool.setGeometry(QtCore.QRect(120, 150, 631, 41))
        self.lineEditSchool.setObjectName("lineEditSchool")
        self.label_12 = QtWidgets.QLabel(parent=self.groupBox_2)
        self.label_12.setGeometry(QtCore.QRect(30, 220, 51, 31))
        self.label_12.setObjectName("label_12")
        self.lineEditEmail = QtWidgets.QLineEdit(parent=self.groupBox_2)
        self.lineEditEmail.setGeometry(QtCore.QRect(120, 220, 361, 41))
        self.lineEditEmail.setObjectName("lineEditEmail")
        self.label_13 = QtWidgets.QLabel(parent=self.groupBox_2)
        self.label_13.setGeometry(QtCore.QRect(520, 220, 61, 31))
        self.label_13.setObjectName("label_13")
        self.radioButtonMale = QtWidgets.QRadioButton(parent=self.groupBox_2)
        self.radioButtonMale.setGeometry(QtCore.QRect(620, 220, 71, 31))
        self.radioButtonMale.setObjectName("radioButtonMale")
        self.radioButtonFemale = QtWidgets.QRadioButton(parent=self.groupBox_2)
        self.radioButtonFemale.setGeometry(QtCore.QRect(620, 260, 81, 31))
        self.radioButtonFemale.setObjectName("radioButtonFemale")
        self.label_14 = QtWidgets.QLabel(parent=self.groupBox_2)
        self.label_14.setGeometry(QtCore.QRect(30, 290, 81, 31))
        self.label_14.setObjectName("label_14")
        self.lineEditPhone = QtWidgets.QLineEdit(parent=self.groupBox_2)
        self.lineEditPhone.setGeometry(QtCore.QRect(120, 290, 361, 41))
        self.lineEditPhone.setObjectName("lineEditPhone")
        self.groupBox_3 = QtWidgets.QGroupBox(parent=self.scrollAreaWidgetContents)
        self.groupBox_3.setGeometry(QtCore.QRect(10, 690, 351, 201))
        self.groupBox_3.setObjectName("groupBox_3")
        self.listWidgetGuide = QtWidgets.QListWidget(parent=self.groupBox_3)
        self.listWidgetGuide.setGeometry(QtCore.QRect(30, 40, 301, 141))
        self.listWidgetGuide.setObjectName("listWidgetGuide")
        item = QtWidgets.QListWidgetItem()
        self.listWidgetGuide.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.listWidgetGuide.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.listWidgetGuide.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.listWidgetGuide.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.listWidgetGuide.addItem(item)
        self.groupBox_4 = QtWidgets.QGroupBox(parent=self.scrollAreaWidgetContents)
        self.groupBox_4.setGeometry(QtCore.QRect(10, 890, 761, 121))
        self.groupBox_4.setObjectName("groupBox_4")
        self.textEditProposal = QtWidgets.QTextEdit(parent=self.groupBox_4)
        self.textEditProposal.setGeometry(QtCore.QRect(30, 30, 711, 71))
        self.textEditProposal.setObjectName("textEditProposal")
        self.groupBox_5 = QtWidgets.QGroupBox(parent=self.scrollAreaWidgetContents)
        self.groupBox_5.setGeometry(QtCore.QRect(380, 690, 391, 201))
        self.groupBox_5.setObjectName("groupBox_5")
        self.label_15 = QtWidgets.QLabel(parent=self.groupBox_5)
        self.label_15.setGeometry(QtCore.QRect(20, 30, 71, 31))
        self.label_15.setObjectName("label_15")
        self.lineEditGroupA = QtWidgets.QLineEdit(parent=self.groupBox_5)
        self.lineEditGroupA.setGeometry(QtCore.QRect(100, 20, 101, 41))
        self.lineEditGroupA.setObjectName("lineEditGroupA")
        self.label_16 = QtWidgets.QLabel(parent=self.groupBox_5)
        self.label_16.setGeometry(QtCore.QRect(20, 90, 71, 31))
        self.label_16.setObjectName("label_16")
        self.lineEditGroupB = QtWidgets.QLineEdit(parent=self.groupBox_5)
        self.lineEditGroupB.setGeometry(QtCore.QRect(100, 90, 101, 41))
        self.lineEditGroupB.setObjectName("lineEditGroupB")
        self.label_17 = QtWidgets.QLabel(parent=self.groupBox_5)
        self.label_17.setGeometry(QtCore.QRect(20, 160, 81, 31))
        self.label_17.setObjectName("label_17")
        self.lineEditGroupA1 = QtWidgets.QLineEdit(parent=self.groupBox_5)
        self.lineEditGroupA1.setGeometry(QtCore.QRect(100, 150, 101, 41))
        self.lineEditGroupA1.setObjectName("lineEditGroupA1")
        self.label_18 = QtWidgets.QLabel(parent=self.groupBox_5)
        self.label_18.setGeometry(QtCore.QRect(210, 30, 71, 31))
        self.label_18.setObjectName("label_18")
        self.lineEditGroupC = QtWidgets.QLineEdit(parent=self.groupBox_5)
        self.lineEditGroupC.setGeometry(QtCore.QRect(280, 20, 101, 41))
        self.lineEditGroupC.setObjectName("lineEditGroupC")
        self.label_19 = QtWidgets.QLabel(parent=self.groupBox_5)
        self.label_19.setGeometry(QtCore.QRect(210, 90, 71, 31))
        self.label_19.setObjectName("label_19")
        self.lineEditGroupD = QtWidgets.QLineEdit(parent=self.groupBox_5)
        self.lineEditGroupD.setGeometry(QtCore.QRect(280, 90, 101, 41))
        self.lineEditGroupD.setObjectName("lineEditGroupD")
        self.pushButtonProposal = QtWidgets.QPushButton(parent=self.groupBox_5)
        self.pushButtonProposal.setGeometry(QtCore.QRect(210, 150, 171, 41))
        self.pushButtonProposal.setObjectName("pushButtonProposal")
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(parent=MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 804, 27))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(parent=MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.groupBox.setTitle(_translate("MainWindow", "Score"))
        self.label.setText(_translate("MainWindow", "Math:"))
        self.label_2.setText(_translate("MainWindow", "Literature:"))
        self.label_3.setText(_translate("MainWindow", "Physics:"))
        self.label_4.setText(_translate("MainWindow", "Chemistry:"))
        self.label_5.setText(_translate("MainWindow", "Biology:"))
        self.label_6.setText(_translate("MainWindow", "Geography:"))
        self.label_7.setText(_translate("MainWindow", "English: "))
        self.label_8.setText(_translate("MainWindow", "History:"))
        self.groupBox_2.setTitle(_translate("MainWindow", "Basic Information"))
        self.label_9.setText(_translate("MainWindow", "FullName:"))
        self.label_10.setText(_translate("MainWindow", "Address:"))
        self.label_11.setText(_translate("MainWindow", "School:"))
        self.label_12.setText(_translate("MainWindow", "Email: "))
        self.label_13.setText(_translate("MainWindow", "Gender:"))
        self.radioButtonMale.setText(_translate("MainWindow", "Male"))
        self.radioButtonFemale.setText(_translate("MainWindow", "Female"))
        self.label_14.setText(_translate("MainWindow", "Phone:"))
        self.groupBox_3.setTitle(_translate("MainWindow", "Guide"))
        __sortingEnabled = self.listWidgetGuide.isSortingEnabled()
        self.listWidgetGuide.setSortingEnabled(False)
        item = self.listWidgetGuide.item(0)
        item.setText(_translate("MainWindow", "Group A: Math, Physics, Chemistry"))
        item = self.listWidgetGuide.item(1)
        item.setText(_translate("MainWindow", "Group A1: Math, Physics, English"))
        item = self.listWidgetGuide.item(2)
        item.setText(_translate("MainWindow", "Group B: Math, Chemistry, Biology"))
        item = self.listWidgetGuide.item(3)
        item.setText(_translate("MainWindow", "Group C: Literature, History, Geography"))
        item = self.listWidgetGuide.item(4)
        item.setText(_translate("MainWindow", "Group D: Literature, Math, English"))
        self.listWidgetGuide.setSortingEnabled(__sortingEnabled)
        self.groupBox_4.setTitle(_translate("MainWindow", "Proposal"))
        self.groupBox_5.setTitle(_translate("MainWindow", "Result"))
        self.label_15.setText(_translate("MainWindow", "Group A: "))
        self.label_16.setText(_translate("MainWindow", "Group B: "))
        self.label_17.setText(_translate("MainWindow", "Group A1: "))
        self.label_18.setText(_translate("MainWindow", "Group C: "))
        self.label_19.setText(_translate("MainWindow", "Group D: "))
        self.pushButtonProposal.setText(_translate("MainWindow", "Proposal"))
