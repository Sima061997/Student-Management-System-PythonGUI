import sqlite3


class DatabaseConnection:
    def __init__(self, db_file= "database.db"):
         self.database = db_file

    def connect(self):
        connection = sqlite3.connect(self.database)
        return connection