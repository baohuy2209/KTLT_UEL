from PyQt6.QtWidgets import QMainWindow

from ShopGroceries.ui.Product.ProductWindowExt import ProductWindowExt
from ShopGroceries.ui.home.MainWindow import Ui_MainWindow


class MainWindowExt(Ui_MainWindow):
    def __init__(self):
        self.product_window = None
        self.product_mainwindow = None
        self.catalog_window = None
        self.catalog_mainwindow = None
    def setupUi(self, MainWindow):
        super().setupUi(MainWindow)
        self.MainWindow = MainWindow
        self.setupSignalAndSlots()
    def setupSignalAndSlots(self):
        self.actionProducts.triggered.connect(self.show_product)
        self.actionCatalog.triggered.connect(self.show_catalog)
    def show_product(self):
        self.product_window = ProductWindowExt()
        self.product_mainwindow = QMainWindow()
        self.product_window.setupUi(self.product_mainwindow)
        self.product_window.show()
    def show_catalog(self):
        self.catalog_window = ProductWindowExt()
        self.catalog_mainwindow = QMainWindow()
        self.catalog_window.setupUi(self.product_mainwindow)
        self.catalog_window.show()
    def show(self):
        self.MainWindow.show()