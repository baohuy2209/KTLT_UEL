from ManagementInvoice.data_access_layer.InvoiceDAL import InvoiceDAL

invoice_dal = InvoiceDAL()
invoices = invoice_dal.get_all_invoices()
for invoice in invoices:
    print(invoice)
    print(type(invoice.is_deleted))
invoice = invoice_dal.get_invoice_by_id("#0001")
print(invoice)