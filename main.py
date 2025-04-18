from PyQt6.QtWidgets import QApplication, QWidget, QMainWindow, QTableWidget, QTableWidgetItem, QToolBar, QStatusBar, \
    QLabel, QTableView, QPushButton
from PyQt6.QtGui import QAction, QIcon
from Classes import InsertDialog, SearchDialog, ClickSignal, EditDialog, DeleteMessage, DatabaseConnection
import sys


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Student Management System")

        #Adding Menu-bar
        file_menu_item = self.menuBar().addMenu("&File")
        help_menu_item = self.menuBar().addMenu("&Help")
        edit_menu_item = self.menuBar().addMenu("&Edit")

        add_student_action = QAction(QIcon("icons/icons/add.png"), "Add Student", self)
        add_student_action.triggered.connect(self.insert_student)
        file_menu_item.addAction(add_student_action)

        about_action = QAction("About", self)
        help_menu_item.addAction(about_action)

        search_student_action = QAction(QIcon("icons/icons/search.png"), "Search", self)
        search_student_action.triggered.connect(self.search_student)
        edit_menu_item.addAction(search_student_action)

        self.table = QTableWidget()
        self.table.setColumnCount(4)
        self.table.setHorizontalHeaderLabels(("Id", "Name", "Course", "Mobile"))
        self.table.verticalHeader().setVisible(False)
        self.setCentralWidget(self.table)

        # Create toolbar and add toolbar elements
        toolbar = QToolBar()
        toolbar.setMovable(True)
        self.addToolBar(toolbar)
        toolbar.addAction(add_student_action)
        toolbar.addAction(search_student_action)

        # Create status bar and add status bar elements
        statusbar = QStatusBar()
        self.setStatusBar(statusbar)

        edit_label = ClickSignal("Edit")
        edit_label.clicked.connect(self.edit_student)
        statusbar.addWidget(edit_label)

        delete_label = ClickSignal("Delete")
        delete_label.clicked.connect(self.delete_student)
        statusbar.addWidget(delete_label)

    def load_data(self):
        try:
            print("Loading data...")
            connection = DatabaseConnection().connect()
            cursor = connection.cursor()
            cursor.execute("SELECT * FROM students")
            result = cursor.fetchall()
            print(list(result))
            self.table.setRowCount(0)
            for row_index, row_data in enumerate(result):
                self.table.insertRow(row_index)
                for column_index, data in enumerate(row_data):
                    self.table.setItem(row_index, column_index, QTableWidgetItem(str(data)))
            connection.close()
        except Exception as e:
            print(f"Error loading data: {e}")

    #decorator function
    def insert_student(self):
        dialog = InsertDialog(self)
        dialog.exec()

    def search_student(self):
        dialog = SearchDialog(self)
        dialog.exec()

    def edit_student(self):
        current_item = self.table.currentItem()

        if current_item is None:
            return          # No changes when item is not selected
        # Get the row of the selected cell
        row = current_item.row()
        #Retrive the data from the selected row
        student_id = self.table.item(row, 0).text()
        name = self.table.item(row, 1).text()
        course = self.table.item(row, 2).text()
        mobile = self.table.item(row, 3).text()

        dialog = EditDialog(student_id, name, course, mobile, self)
        dialog.exec()

    def delete_student(self):
        current_item = self.table.currentItem()

        if current_item is None:
            return          # No changes when item is not selected

        row = current_item.row()

        #Retrive student Id from the selected row
        student_id = self.table.item(row, 0).text()

        dialog = DeleteMessage(student_id, self)
        dialog.show()


app = QApplication(sys.argv)
student_db = MainWindow()
student_db.load_data()
student_db.show()

sys.exit(app.exec())