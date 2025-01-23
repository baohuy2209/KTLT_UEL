from ManagementInvoice.io.JSONFileFactory import JSONFileFactory
from ManagementInvoice.models.Invoice import Invoice


class InvoiceDAL:
    def __init__(self):
        self.list_invoice = []
    def delete(self, id):
        json_factory = JSONFileFactory()
        invoice_delete = self.get_invoice_by_id(id)
        self.list_invoice = json_factory.read_file("data/invoice.json", "r")
        for invoice in self.list_invoice:
            if invoice == invoice_delete:
                invoice["is_deleted"] = "True"
                break
        # Mở file JSON ở chế độ ghi để xóa nội dung

        json_factory.update_file("data/invoice.json", "w", self.list_invoice)
    def add_invoice(self, new_invoice):
        json_factory = JSONFileFactory()
        json_factory.write_file("data/invoice.json", "w", new_invoice)
    def get_all_invoices(self):
        json_factory = JSONFileFactory()
        self.list_invoice = json_factory.read_file("data/invoice.json", "r")
        list_invoice = []
        for invoice in self.list_invoice:
            element_invoice = Invoice(invoice_id=invoice["invoice_id"], company_name=invoice["company_name"], street_name=invoice["street_name"], address=invoice["address"], date=invoice["date"], person_send=invoice["person_send"], person_received=invoice["person_received"], list_detail=invoice["list_detail"], tax_rate=invoice["tax_rate"], other_cost=invoice["other_cost"], is_deleted=bool(invoice["is_deleted"]))
            list_invoice.append(element_invoice)
        return list_invoice
    def get_invoice_by_id(self, id):
        invoice_needed = {}
        for i in range(len(self.list_invoice)):
            if id == self.list_invoice[i]["invoice_id"]:
                invoice_needed = self.list_invoice[i]
                break
        return invoice_needed