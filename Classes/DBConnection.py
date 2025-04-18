import mysql.connector
from mysql.connector import Error


class DatabaseConnection:
    def __init__(self, host="localhost", user="root", password="pythoncourse", db="school"):
         self.host = host
         self.user = user
         self.password = password
         self.database = db

    def connect(self):
        print("Connecting to DB...")
        try:
            connection = mysql.connector.connect(host=self.host,
                                                 user=self.user,
                                                 password=self.password,
                                                 database=self.database)

            if connection.is_connected():
                print("Connected...")
                return connection

        except Error as e:
            print(f"Database connection failed: {e}")
            return None


connection = DatabaseConnection().connect()
cursor = connection.cursor()
cursor.execute("SELECT * FROM students")
result = cursor.fetchall()
print(list(result))
