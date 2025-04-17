from PyQt6.QtWidgets import QMessageBox
import sqlite3


class DeleteDialog(QMessageBox):
    def __init__(self, student_id, parent=None):
        super().__init__()
        self.student_id = student_id
        self.parent = parent
        print("Delete Dialog passed")
        #button = QPushButton("Delete")
        #button.clicked.connect(self.de_student)
        self.delete_student()

    def delete_student(self):
        print("Delete student passed")
        # Show confirmation dialog before deleting
        # Show confirmation dialog before deleting
        reply = QMessageBox.question(
            self, "Confirm Deletion", f"Are you sure you want to delete student with ID {self.student_id}?",
            QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No, QMessageBox.StandardButton.No
        )

        if reply == QMessageBox.StandardButton.Yes:
            # Execute DELETE query to remove student form db
            connection = sqlite3.connect("database.db")
            cursor = connection.cursor()
            cursor.execute("DELETE FROM students WHERE id = ?", (self.student_id,))
            connection.commit()
            connection.close()
            # Call back to main window to refresh table
            if self.parent:
                self.parent.load_data()