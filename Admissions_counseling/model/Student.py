class Student:
    def __init__(self, fullname = None, address=None, school=None, email=None, phone=None, gender = None, math=None, literature=None, physics=None, chemistry=None, biology=None, geography=None, english=None, history=None):
        self.fullname = fullname
        self.address = address
        self.school = school
        self.email = email
        self.phone = phone
        self.gender = gender
        self.math = math
        self.literature = literature
        self.physics = physics
        self.chemistry = chemistry
        self.biology = biology
        self.geography = geography
        self.english = english
        self.history = history
    def __str__(self):
        infor = f"Information of Student: \n + Fullname: {self.fullname} \n + Address: {self.address} \n + School: {self.school} \n + Email: {self.email} \n + Phone: {self.phone} \n + Score: \n\t *Math: {self.math} \n\t *Literature: {self.literature} \n\t *Physics: {self.physics} \n\t *Chemistry: {self.chemistry} \n\t *Biology: {self.biology} \n\t *Geography: {self.geography} \n\t *English: {self.english} \n\t *History: {self.history}"