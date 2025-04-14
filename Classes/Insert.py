from PyQt6.QtWidgets import QDialog, QVBoxLayout, QLineEdit, QComboBox, QPushButton
import sqlite3


class InsertDialog(QDialog):
    def __init__(self, parent=None):
        super().__init__()
        self.parent = parent

        self.setWindowTitle("Insert Student Data")
        self.setFixedWidth(300)
        self.setFixedHeight(300)

        layout = QVBoxLayout()

        # Add student_name widget
        self.student_name = QLineEdit()
        self.student_name.setPlaceholderText("Name")
        layout.addWidget(self.student_name)

        # Add combo box of courses
        self.course_name = QComboBox()
        courses = ["Biology", "Math", "Astronomy", "Physics"]
        self.course_name.addItems(courses)
        layout.addWidget(self.course_name)

        #Add mobile number
        self.student_mobile_no = QLineEdit()
        self.student_mobile_no.setPlaceholderText("Mobile Number")
        layout.addWidget(self.student_mobile_no)

        # Add button
        button = QPushButton("Insert")
        button.clicked.connect(self.add_student)
        layout.addWidget(button)

        self.setLayout(layout)

    def add_student(self):
        print("Add Student passed")
        name = self.student_name.text()
        course = self.course_name.itemText(self.course_name.currentIndex())
        mobile_no = self.student_mobile_no.text()
        connection = sqlite3.connect("database.db")
        cursor = connection.cursor()
        cursor.execute("INSERT INTO students (name, course, mobile) VALUES (?, ?, ?)",
                       (name, course, mobile_no))
        connection.commit()
        cursor.close()
        connection.close()

        # Call back to main window to refresh table
        if self.parent:
            self.parent.load_data()


