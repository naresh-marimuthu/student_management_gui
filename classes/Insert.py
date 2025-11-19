import sys
import sqlite3
from PyQt6.QtWidgets import (QComboBox, QLabel, QLineEdit, QDialog, QVBoxLayout, QPushButton)
from PyQt6.QtGui import QAction


class Insert(QDialog):
    def __init__(self):
        super().__init__()
        layout = QVBoxLayout()
        
        self.name = QLabel("Name")
        self.name_input = QLineEdit()

        self.course = QLabel("Course")
        self.course_combo = QComboBox()
        self.course_combo.addItems(["Physics", "Maths", "Astronomy", "Biology"])

        self.mobile = QLabel("Mobile")
        self.mobile_input = QLineEdit()
        self.submit = QPushButton("Register")

        layout.addWidget(self.name)
        layout.addWidget(self.name_input)
        layout.addWidget(self.course)
        layout.addWidget(self.course_combo)
        layout.addWidget(self.mobile)
        layout.addWidget(self.mobile_input)
        layout.addWidget(self.submit)

        self.setLayout(layout)
        
        self.submit.clicked.connect(self.register)

    def register(self):
        name = self.name_input.text()
        course = self.course_combo.currentText()
        mobile = self.mobile_input.text()

        print(f"name {name} course {course} mobile {mobile}")

        conn = sqlite3.connect("database.db")
        cursor = conn.cursor()
        cursor.execute("INSERT INTO STUDENTS (NAME, COURSE, MOBILE) VALUES (?, ?, ?)", (name, course, mobile))
        conn.commit()
        cursor.close()
        conn.close()
        
