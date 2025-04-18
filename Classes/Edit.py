from PyQt6.QtWidgets import QLabel
from PyQt6.QtCore import pyqtSignal
from PyQt6.QtWidgets import QDialog, QVBoxLayout, QLineEdit, QComboBox, QPushButton
from Classes.DBConnection import DatabaseConnection


class ClickSignal(QLabel):
    clicked = pyqtSignal()

    def mousePressEvent(self, event):
        # fires the mouse click signal
        self.clicked.emit()
        super().mousePressEvent(event)

#Insert window displayed
class EditDialog(QDialog):
    def __init__(self, student_id, name, course, mobile, parent=None):
        super().__init__()
        self.parent = parent

        self.setWindowTitle("Edit Student Data")
        self.setFixedWidth(300)
        self.setFixedHeight(300)

        layout = QVBoxLayout()
        self.student_id = student_id
        # Add student_name widget
        self.student_name = QLineEdit(name)
        layout.addWidget(self.student_name)

        # Add combo box of courses
        self.course_name = QComboBox()
        courses = ["Biology", "Math", "Astronomy", "Physics"]
        self.course_name.addItems(courses)
        layout.addWidget(self.course_name)

        #Add mobile number
        self.student_mobile_no = QLineEdit(mobile)
        #self.student_mobile_no.setPlaceholderText("Mobile Number")
        layout.addWidget(self.student_mobile_no)

        # Add button
        button = QPushButton("Edit")
        button.clicked.connect(self.edit_student)
        layout.addWidget(button)

        self.setLayout(layout)

    def edit_student(self):
        print("Edit Student passed")
        name = self.student_name.text()
        course = self.course_name.itemText(self.course_name.currentIndex())
        mobile_no = self.student_mobile_no.text()
        connection = DatabaseConnection().connect()
        cursor = connection.cursor()
        cursor.execute("""UPDATE students
            SET name = ?, course = ?, mobile = ? 
            WHERE id = ?
            """, (name, course, mobile_no, self.student_id))
        connection.commit()
        cursor.close()
        connection.close()

        # Call back to main window to refresh table
        if self.parent:
            self.parent.load_data()






