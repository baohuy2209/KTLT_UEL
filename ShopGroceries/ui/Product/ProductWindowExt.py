from datetime import date

from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import QTableWidgetItem

from ShopGroceries.data_access_layer.ProductDAL import ProductDAL
from ShopGroceries.ui.Product.ProductWindow import Ui_MainWindow


class ProductWindowExt(Ui_MainWindow):
    def __init__(self):
        self.products = self.get_all_products()
    def setupUi(self, MainWindow):
        super().setupUi(MainWindow)
        self.MainWindow = MainWindow
        self.setupSignalAndSlots()
    def get_all_products(self):
        product_dal = ProductDAL()
        product_dal.connect()
        products = product_dal.get_list_products()
        return products
    def setupSignalAndSlots(self):
        self.pushButtonCreate.clicked.connect(self.create_new)
        self.pushButtonStore.clicked.connect(self.store)
        self.pushButtonDisplay.clicked.coonect(self.display_products)
    def store(self):
        pass
    def create_new(self):
        self.lineEditName.clear()
        self.lineEditProductID.clear()
        self.lineEditQuantity.clear()
        self.lineEditPrice.clear()
        self.dateEditCreatedAt.clear()
        self.comboBoxTypeProduct.clear()
    def display_products(self):
        self.tableWidgetListProduct.setRowCount(0)
        for i in range(len(self.products)):
            product_i = self.products[i]
            self.tableWidgetListProduct.insertRow(i)
            column_id = QTableWidgetItem(str(product_i.ProductID))
            column_name = QTableWidgetItem(str(product_i.Name))
            column_quantity = QTableWidgetItem(str(product_i.Quantity))
            if product_i.Quantity < 5:
                column_quantity.setForeground(Qt.GlobalColor.red)
                column_quantity.setBackground(Qt.GlobalColor.yellow)
            column_price = QTableWidgetItem(str(product_i.Price))
            column_date = QTableWidgetItem(str(date.today()))
            column_type = QTableWidgetItem(str(product_i.ProductType))
            self.tableWidgetListProduct.setItem(i, 0, column_id)
            self.tableWidgetListProduct.setItem(i, 1, column_name)
            self.tableWidgetListProduct.setItem(i, 2, column_price)
            self.tableWidgetListProduct.setItem(i, 3, column_quantity)
            self.tableWidgetListProduct.setItem(i, 3, column_quantity)
            self.tableWidgetListProduct.setItem(i, 4, column_date)
            self.tableWidgetListProduct.setItem(i, 5, column_type)
    def show(self):
        self.MainWindow.show()