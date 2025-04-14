from PyQt6.QtWidgets import QDialog, QVBoxLayout, QLineEdit, QPushButton
import sqlite3

from main import student_db


class SearchDialog(QDialog):
    def __init__(self, parent=None):
        super().__init__()
        self.parent = parent

        self.setWindowTitle("Search Student")
        self.setFixedWidth(300)
        self.setFixedHeight(300)

        layout = QVBoxLayout()

        # Add search student widget
        self.student_name = QLineEdit()
        self.student_name.setPlaceholderText("Name")
        layout.addWidget(self.student_name)

        #Add button
        button = QPushButton("Search")
        button.clicked.connect(self.search_std)
        layout.addWidget(button)

        self.setLayout(layout)

    def search_std(self):
        name = self.student_name.text()
        connection = sqlite3.connect("database.db")
        cursor = connection.cursor()
        result = connection.execute("SELECT  * from students WHERE name = ?", (name,))

        print(rows)


        items = student_db.table.findItems(name, Qt.MatchFlag.MatchFixedString)
        for item in items:
            print(item)
            student_db.table.item(item.row(), 1).setSelected(True)

        cursor.close()
        connection.close()

        # Call back to main window to refresh table
        if self.parent:
            self.parent.load_data()
