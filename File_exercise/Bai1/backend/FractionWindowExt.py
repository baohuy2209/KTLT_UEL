import traceback

from PyQt6.QtWidgets import QFileDialog, QMessageBox

from File_exercise.Bai1.IO.FileFactory import FileFactory
from File_exercise.Bai1.model.Fraction import Fraction
from File_exercise.Bai1.model.ListFraction import ListFraction
from File_exercise.Bai1.ui.FractionWindow import Ui_MainWindow


class FractionWindowExt(Ui_MainWindow):
    def __init__(self):
        self.file_factory = FileFactory()
        self.list_fraction = ListFraction()
    def setupUi(self, MainWindow):
        super().setupUi(MainWindow)
        self.MainWindow = MainWindow
        self.setupSignalAndSlots()
    def setupSignalAndSlots(self):
        self.pushButtonRefresh.clicked.connect(self.refresh)
        self.pushButtonSave.clicked.connect(self.save)
        self.pushButtonRead.clicked.connect(self.read)
    def display(self):
        list_fraction = self.list_fraction.get_string()
        self.textEditFraction.setText(list_fraction)
    def refresh(self):
        self.textEditFraction.setText("")
    def save(self):
        try:
            list_fraction_str = self.textEditFraction.toPlainText()
            list_fraction_str = list_fraction_str.split(",")
            for fraction in list_fraction_str:
                numerator, denominator = fraction.split("/")
                temp_fraction = Fraction(numerator, denominator)
                self.list_fraction.add(temp_fraction)
            file_filter="Định dạng Json file (*.json);;Tất cả các loại file (*)"
            filename,selected_filter=QFileDialog.getSaveFileName(self.MainWindow,filter=file_filter)
            print("tên file mà bạn muốn lưu mới:",filename)
            if filename=="":
                return
            self.file_factory.writeData(filename,self.list_fraction.list_fraction)
            msgBox=QMessageBox()
            msgBox.setText(f"Đã xuất dữ liệu ra định dạng JSON thành công.\n "
                           f"Nơi xuất dữ liệu [{filename}]")
            msgBox.setWindowTitle("Thông báo")
            msgBox.exec()
        except:
            traceback.print_exc()
    def read(self):
        try:
            file_filter = "Định dạng Json file (*.json);;Tất cả các loại file (*)"
            filename, selected_filter = QFileDialog.getOpenFileName(self.MainWindow, filter=file_filter)
            if filename=="":
                return
            fractions=self.file_factory.readData(filename,Fraction)
            self.list_fraction.list_fraction = fractions
            self.display()
        except:
            traceback.print_exc()
    def show(self):
        self.MainWindow.show()
