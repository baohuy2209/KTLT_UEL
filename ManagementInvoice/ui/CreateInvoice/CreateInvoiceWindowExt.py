from ManagementInvoice.data_access_layer.InvoiceDAL import InvoiceDAL
from ManagementInvoice.ui.CreateInvoice.CreateInvoiceWindow import Ui_MainWindow


class CreateInvoiceWindowExt(Ui_MainWindow):
    def __init__(self):
        self.invoice_dal = InvoiceDAL()
        self.list_detail = []
    def setupUi(self, MainWindow):
        super().setupUi(MainWindow)
        self.MainWindow = MainWindow
        self.setupSignalAndSlots()
    def setupSignalAndSlots(self):
        self.pushButtonCreate.clicked.connect(self.create_invoice)
        self.pushButtonAddDetail.clicked.connect(self.add_detail_list)
    def show(self):
        self.MainWindow.show()
    def create_invoice(self):
        invoice_id = self.lineEditInvoiceID.text()
        company_name = self.lineEditCompany.text()
        street_name = self.lineEditStreet.text()
        address = self.lineEditAddress.text()
        date = self.lineEditDate.text()
        person_send = self.lineEditPersonSend.text()
        person_received = self.lineEditPersonReceived.text()
        list_detail = self.list_detail
        tax_rate = float(self.lineEditTaxRate.text())
        other_cost = float(self.lineEditOtherCost.text())
        new_invoice = {
            "invoice_id": invoice_id,
            "company_name": company_name,
            "street_name": street_name,
            "address": address,
            "date": date,
            "person_send": person_send,
            "person_received": person_received,
            "list_detail": list_detail,
            "tax_rate": tax_rate,
            "other_cost": other_cost
        }
        self.invoice_dal.add_invoice(new_invoice)
    def add_detail_list(self):
        detail = self.lineEditDetail.text()
        amount = float(self.lineEditAmount.text())
        object_detail = {
            "Detail": detail,
            "Amount": amount,
        }
        self.list_detail.append(object_detail)
        self.lineEditDetail.setText("")
        self.lineEditAmount.setText("")