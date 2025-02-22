class Employee:
    def __init__(self, emp_id=None, name=None, job=None, email=None, phone=None):
        self.id = emp_id
        self.name = name
        self.job = job
        self.email = email
        self.phone = phone
    def __str__(self):
        info=f"Information: \n + ID: {self.id} \n + Name: {self.name} \n + Job: {self.job} \n + Email: {self.email} \n + Phone: {self.phone}"
        return info 