import sys
import sqlite3
from PyQt6.QtWidgets import (QComboBox, QLabel, QLineEdit, QDialog, QVBoxLayout, QPushButton)
from PyQt6.QtGui import QAction


class EditOption(QDialog):
    def __init__(self, id, name, course, mobile):
        super().__init__()
        layout = QVBoxLayout()
        
        self.student_id = id
        
        self.name_input = QLineEdit(name)
        

        self.course_combo = QComboBox()
        self.course_combo.addItems(["Physics", "Maths", "Astronomy", "Biology"])
        self.course_combo.setCurrentText(course)
        

        self.mobile_input = QLineEdit(mobile)
        

        self.update = QPushButton("Update")
        self.result = QLabel("")

        layout.addWidget(self.name_input)
        layout.addWidget(self.course_combo)
        layout.addWidget(self.mobile_input)
        layout.addWidget(self.update)
        layout.addWidget(self.result)

        self.setLayout(layout)

        self.update.clicked.connect(self.update_student)

    def update_student(self):
        id = self.student_id
        name = self.name_input.text()
        course = self.course_combo.currentText()
        mobile = self.mobile_input.text()

        print(f"name {name} course {course} mobile {mobile}")

        conn = sqlite3.connect("database.db")
        cursor = conn.cursor()
        cursor.execute("UPDATE STUDENTS SET NAME = ?, COURSE = ?, MOBILE = ? WHERE ID = ?", (name, course, mobile, id))
        conn.commit()
        cursor.close()
        conn.close()
        self.result.setText("Updated Successfully!")

   