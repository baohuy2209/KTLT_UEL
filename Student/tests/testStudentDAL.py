from Student.data_access_layer.StudentDAL import StudentDAL

student_dal = StudentDAL()
student_dal.connect()
students = student_dal.get_all()
for student in students:
    print(student)