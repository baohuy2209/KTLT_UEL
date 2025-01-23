class Invoice:
    def __init__(self, invoice_id,company_name, street_name, address, date, person_send, person_received, list_detail, tax_rate, other_cost, is_deleted):
        self.invoice_id = invoice_id
        self.company_name = company_name
        self.street_name = street_name
        self.address = address
        self.date = date,
        self.person_send = person_send
        self.person_received = person_received
        self.list_detail = list_detail
        self.tax_rate = tax_rate
        self.other_cost = other_cost
        self.is_deleted = is_deleted
    def __str__(self):
        info = f"{self.invoice_id} - {self.company_name} - {self.is_deleted}"
        return info