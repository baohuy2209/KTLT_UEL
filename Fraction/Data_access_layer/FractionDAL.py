from Fraction.connector.Connector import Connector
from Fraction.models.Fraction import Fraction


class FractionDAL(Connector):
    def get_all(self):
        sql = 'select * from fraction'
        cursor = self.query(sql)
        data = cursor.fetchall()
        fractions = []
        for record in data:
            id = record[0]
            numerator = int(record[1])
            denominator = int(record[2])
            fraction = Fraction(numerator, denominator)
            fractions.append(fraction)
        cursor.close()
        return fractions
    def create_fraction(self, fraction):
        sql_insert = "insert into fraction (numerator, denominator) values(%s,%s)"
        str_numerator = str(fraction.get_numerator())
        str_denominator = str(fraction.get_denominator())
        val_input = (str_numerator, str_denominator)
        cursor = self.query(sql_insert,val_input)
        self.conn.commit()
        return cursor.rowcount
