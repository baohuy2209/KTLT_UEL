class Student:
    def __init__(self, StudentID=None, FullName=None, Phone=None, Email=None, Address=None, Gender=None, Grade=None):
        self.StudentID = StudentID
        self.FullName = FullName
        self.Phone = Phone
        self.Email = Email
        self.Address = Address
        self.Gender = Gender
        self.Grade = Grade
    def __str__(self):
        info = f"Information Student: \n + StudentID: {self.StudentID} \n + FullName: {self.FullName} \n + Phone: {self.Phone} \n + Email: {self.Email} \n + Address: {self.Address} \n + Gender: {self.Gender} \n + Grade: {self.Grade}"
        return info