class Employee:
    def __init__(self, employeeid = None, name = None, email = None, phone = None, address = None, lottery=None):
        self.employeeid = employeeid
        self.name = name
        self.email = email
        self.phone = phone
        self.address = address
        self.lottery = lottery
    def __str__(self):
        info = f"{self.employeeid} | {self.name} | {self.email} | {self.phone} | {self.address} | {self.lottery}"
        return info