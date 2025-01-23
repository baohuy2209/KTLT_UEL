from PyQt6.QtWidgets import QTableWidgetItem

from ManagementInvoice.ui.DetailInvoice.DetailInvoice import Ui_MainWindow


class DetailInvoiceExt(Ui_MainWindow):
    def __init__(self, detail_invoice):
        self.detail_invoice = detail_invoice
        print(self.detail_invoice)
    def setupUi(self, MainWindow):
        super().setupUi(MainWindow)
        self.MainWindow = MainWindow
        self.import_invoice_information()
    def import_invoice_information(self):
        detail_invoice = self.detail_invoice
        self.labelInvoiceId.setText(str(detail_invoice["invoice_id"]))
        self.labelCompanyName.setText(str(detail_invoice["company_name"]))
        self.labelAddress.setText(str(detail_invoice["address"]))
        self.labelStreetName.setText(str(detail_invoice["street_name"]))
        self.lineEditDate.setText(str(detail_invoice["date"]))
        service_for = ""
        i = 0
        for detail in detail_invoice["list_detail"]:
            service_for += detail["Detail"].split(" (")[0]
            if i == len(detail_invoice["list_detail"]) - 2:
                service_for += " & "
            else:
                service_for += " , "
            i += 1
        self.lineEditForService.setText(service_for)
        self.lineEditPersonReceived.setText(str(detail_invoice["person_received"]))
        self.tableWidgetListdetail.setRowCount(0)
        sum = 0
        for i in range(len(detail_invoice["list_detail"])):
            self.tableWidgetListdetail.insertRow(i)
            detail = detail_invoice["list_detail"][i]
            sum += float(detail["Amount"])
            column_detail = QTableWidgetItem(str(detail["Detail"]))
            column_amount = QTableWidgetItem(str(detail["Amount"]))
            self.tableWidgetListdetail.setItem(i, 0, column_detail)
            self.tableWidgetListdetail.setItem(i, 1, column_amount)
        self.lineEditSubtotal.setText(str(sum))
        self.lineEditTaxRate.setText(str(detail_invoice["tax_rate"]))
        self.lineEditOtherCase.setText(str(detail_invoice["other_cost"]))
        total_cost = sum*(100-detail_invoice["tax_rate"])/100 - float(detail_invoice["other_cost"])
        self.lineEditTotal.setText(str(total_cost))
    def show(self):
        self.MainWindow.show()
