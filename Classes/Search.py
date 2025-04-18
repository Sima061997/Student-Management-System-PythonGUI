from PyQt6.QtWidgets import QDialog, QVBoxLayout, QLineEdit, QPushButton, QTableWidgetItem
from Classes.DBConnection import DatabaseConnection


#Search window displayed
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
        connection = DatabaseConnection().connect()
        cursor = connection.cursor()
        result = connection.execute("SELECT * from students WHERE name = %s", (name,))
        rows = result.fetchall()
        print(rows)
        cursor.close()
        connection.close()

        #clear the table first
        self.parent.table.setRowCount(0)

        for row_index, row_data in enumerate(rows):
            self.parent.table.insertRow(row_index)
            for col_index, data in enumerate(row_data):
                item = QTableWidgetItem(str(data))
                self.parent.table.setItem(row_index, col_index, item)
