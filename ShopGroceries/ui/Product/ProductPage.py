from PyQt6.QtWidgets import QApplication, QMainWindow

from ShopGroceries.ui.Product.ProductWindowExt import ProductWindowExt


def ProductPage():
    app = QApplication([])
    myWindow = ProductWindowExt()
    MainWindow = QMainWindow()
    myWindow.setupUi(MainWindow)
    myWindow.show()
    app.exec()
ProductPage()