import sys
import sqlite3
from PyQt6.QtWidgets import (QApplication, QMainWindow, QTableWidget, QTableWidgetItem, QStatusBar, QPushButton)
from PyQt6.QtGui import QAction
from classes.Insert import Insert
from classes.Edit import EditOption
from classes.Delete import DeleteOption


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Student Management Application")
        self.setGeometry(100, 100, 800, 600)

        file_menu = self.menuBar().addMenu("&File")
        file_action = QAction("&Add record", self)
        file_action.triggered.connect(self.add_record)
        file_menu.addAction(file_action)
        
        help_menu = self.menuBar().addMenu("&Help")
        help_action = QAction("&About us", self)
        help_action.triggered.connect(self.about_us)
        help_menu.addAction(help_action)

        self.table = QTableWidget()
        self.table.setColumnCount(4)
        self.table.setHorizontalHeaderLabels(["ID", "NAME", "COURSE", "MOBILE"])
        self.table.verticalHeader().setVisible(False)
        self.setCentralWidget(self.table)

        self.status_bar = QStatusBar()
        self.setStatusBar(self.status_bar)

        #Cell click Event
        self.table.cellClicked.connect(self.cell_clicked)    

    def cell_clicked(self):
        children = self.status_bar.findChildren(QPushButton) 
        if children:
            for child in children:
                self.status_bar.removeWidget(child)
        self.edit_button = QPushButton("Edit Records")
        self.edit_button.clicked.connect(self.Edit)
        self.delete_button = QPushButton("Delete Records")
        self.delete_button.clicked.connect(self.Delete)

        self.status_bar.addWidget(self.edit_button)
        self.status_bar.addWidget(self.delete_button)

    def add_record(self):
        insert = Insert()
        insert.exec()
        main_window.load_data()

    def Edit(self):
        index = self.table.currentRow()
        student_id = self.table.item(index, 0).text()
        student_name = self.table.item(index, 1).text()
        student_course = self.table.item(index, 2).text()
        student_mobile = self.table.item(index, 3).text()
        print(f"student details - {student_id} - {student_name} - {student_course} - {student_mobile}")
        edit = EditOption(student_id, student_name, student_course, student_mobile)
        edit.exec()
        main_window.load_data()


    def Delete(self):
        index = self.table.currentRow()
        student_id = self.table.item(index, 0).text()
        delete_student = DeleteOption(student_id)
        delete_student.exec()
        main_window.load_data()

    def about_us(self):
        pass    

    def load_data(self):
        conn = sqlite3.connect("database.db")
        cursor = conn.cursor()
        
        rows = cursor.execute("SELECT * FROM STUDENTS") 

        self.table.setRowCount(0)

        for row_index, row_data in enumerate(rows):
            self.table.insertRow(row_index)
            for col_index, col_data in enumerate(row_data):
                self.table.setItem(row_index, col_index, QTableWidgetItem(str(col_data)))

        cursor.close()
        conn.close()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    main_window = MainWindow()
    main_window.show()
    main_window.load_data()
    sys.exit(app.exec())
