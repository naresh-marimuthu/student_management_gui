import sys
import sqlite3
from PyQt6.QtWidgets import (QGridLayout, QLabel, QDialog, QPushButton)
from PyQt6.QtGui import QAction


class DeleteOption(QDialog):
    def __init__(self, id):
        super().__init__()
        
        self.student_id = id
        
        self.delete = QLabel("Are you sure want to proceed?")
        self.yes = QPushButton("Yes")
        self.no = QPushButton("No")
        self.result = QLabel("")
        
        grid_layout = QGridLayout()

        grid_layout.addWidget(self.delete, 0, 0, 1, 2)
        grid_layout.addWidget(self.yes, 1, 0)
        grid_layout.addWidget(self.no, 1, 1)
        grid_layout.addWidget(self.result, 3, 0, 1, 2)
        self.setLayout(grid_layout)

        self.yes.clicked.connect(self.delete_student)

    def delete_student(self):
        id = self.student_id
        
        conn = sqlite3.connect("database.db")
        cursor = conn.cursor()
        cursor.execute("DELETE FROM STUDENTS WHERE ID = ?", (id,))
        conn.commit()
        cursor.close()
        conn.close()
        self.result.setText("Deleted Successfully!")

   