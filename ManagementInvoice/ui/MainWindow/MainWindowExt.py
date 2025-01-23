import traceback

from PyQt6.QtWidgets import QTableWidgetItem, QMainWindow

from ManagementInvoice.data_access_layer.InvoiceDAL import InvoiceDAL
from ManagementInvoice.ui.CreateInvoice.CreateInvoiceWindowExt import CreateInvoiceWindowExt
from ManagementInvoice.ui.DetailInvoice.DetailInvoiceExt import DetailInvoiceExt
from ManagementInvoice.ui.MainWindow.MainWindow import Ui_MainWindow


class MainWindowExt(Ui_MainWindow):
    def __init__(self):
        self.invoice_dal = InvoiceDAL()
        self.list_invoice = self.invoice_dal.get_all_invoices()
        self.detail_window = None
        self.detail_qmainwindow = None
        self.create_window = None
        self.create_qmainwindow = None
    def setupUi(self, MainWindow):
        super().setupUi(MainWindow)
        self.MainWindow = MainWindow
        self.setupSignalAndSlots()
    def setupSignalAndSlots(self):
        self.pushButtonShowDetail.clicked.connect(self.show_detail)
        self.pushButtonCreate.clicked.connect(self.create_invoice)
        self.pushButtonRefresh.clicked.connect(self.refresh)
        self.pushButtonDelete.clicked.connect(self.delete)
    def delete(self):
        current_row = self.tableWidgetListInvoice.currentRow()
        id = self.tableWidgetListInvoice.item(current_row,0).text()
        self.invoice_dal.delete(id)
    def refresh(self):
        self.display()
    def show(self):
        self.MainWindow.show()
        self.display()
    def display(self):
        self.tableWidgetListInvoice.setRowCount(0)
        for i in range(len(self.list_invoice)):
            invoice_i = self.list_invoice[i]
            if not invoice_i.is_deleted:
                self.tableWidgetListInvoice.insertRow(i)
                column_id = QTableWidgetItem(str(invoice_i.invoice_id))
                column_date = QTableWidgetItem(str(invoice_i.date))
                column_send_to = QTableWidgetItem(str(invoice_i.person_received))
                column_received = QTableWidgetItem(str(invoice_i.person_send))
                self.tableWidgetListInvoice.setItem(i, 0, column_id)
                self.tableWidgetListInvoice.setItem(i, 1, column_date)
                self.tableWidgetListInvoice.setItem(i, 2, column_send_to)
                self.tableWidgetListInvoice.setItem(i, 3, column_received)
    def create_invoice(self):
        try:
            self.create_qmainwindow = QMainWindow()
            self.create_window = CreateInvoiceWindowExt()
            self.create_window.setupUi(self.create_qmainwindow)
            self.create_window.show()
        except:
            traceback.print_exc()
    def show_detail(self):
        try:
            row = self.tableWidgetListInvoice.currentRow()
            column_id = self.tableWidgetListInvoice.item(row,0).text()
            print(column_id)
            current_invoice = self.invoice_dal.get_invoice_by_id(column_id)
            self.detail_qmainwindow = QMainWindow()
            self.detail_window = DetailInvoiceExt(current_invoice)
            self.detail_window.setupUi(self.detail_qmainwindow)
            self.detail_window.show()
        except:
            traceback.print_exc()