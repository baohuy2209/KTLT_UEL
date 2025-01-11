from Student.connector.Connector import Connector
from Student.models.Student import Student

class StudentDAL(Connector): 
    def get_all(self):
        sql = 'select * from student'
        cursor = self.query(sql)
        data = cursor.fetchall()
        students = []
        for record in data:
            studentID = record[0]
            fullname = record[1]
            phone = record[2]
            email = record[3]
            address = record[4]
            gender = record[5]
            grade = record[6]
            student = Student(studentID, fullname, phone, email, address, gender, grade)
            students.append(student)
        cursor.close()
        return students