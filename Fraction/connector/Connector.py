import mysql.connector
from mysql.connector import Error
class Connector:
    def __init__(self):
        self.server="localhost"#127.0.0.1
        self.port=3306
        self.database="database_10k"
        self.username="root"
        self.password="Huy_22092005"
    def connect(self,server=None,port=None,database=None,username=None,password=None):
        try:
            if server!=None:
                self.server=server
                self.port=port
                self.database=database
                self.username=username
                self.password=password
            self.conn=mysql.connector.connect(
                host=self.server,
                user=self.username,
                password=self.password,
                database=self.database
                )
        except Error as e:
            print("Lỗi khi kết nối đến MySQL:", e)
    def query(self,sql,val_input=None):
        cursor=self.conn.cursor()
        cursor.execute(sql,val_input)
        return cursor