# Import libraries
import mysql.connector
from decimal import Decimal

# ทำโมเดล+เขียนคำสั่ง SQL
class DataModel:
    def __init__(self, id, pregnancies, glucose, skin_thickness, BMI, age, result):
        self.id = id
        self.pregnancies = pregnancies
        self.glucose = glucose
        self.skin_thickness = skin_thickness
        self.BMI = BMI
        self.age = age
        self.result = result

    # insertแถวลงในDatabase
    def insert(self, result):
        connection = mysql.connector.connect(
            host="localhost",
            user="root",
            password="ppgdmild",
            database="diabetesdb"
        )
        cursor = connection.cursor()
        query = "INSERT INTO diabetestable (pregnancies, glucose, skin_thickness, BMI, age, result) VALUES (%s, %s, %s, %s, %s, %s)"
        values = (self.pregnancies, Decimal(str(self.glucose)), Decimal(str(self.skin_thickness)), Decimal(str(self.BMI)), self.age, result)
        cursor.execute(query, values)
        connection.commit()
        return cursor.lastrowid


    #แสดงค่าทั้งหมด
    @staticmethod
    def get_all():
        connection = mysql.connector.connect(
            host="localhost",
            user="root",
            password="ppgdmild",
            database="diabetesdb"
        )
        cursor = connection.cursor()
        query = "SELECT * FROM diabetestable"
        cursor.execute(query)
        result = cursor.fetchall()
        data_list = []
        for row in result:
            data_list.append(DataModel(row[0], row[1], row[2], row[3], row[4], row[5], row[6]))
        return data_list
