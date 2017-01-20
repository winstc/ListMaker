from PyQt5.QtWidgets import QDialog, QVBoxLayout, QHBoxLayout,QDialogButtonBox, QDateTimeEdit, QApplication, QPushButton
from PyQt5.QtCore import Qt, QDateTime
import sys

class insertDates(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)

        self.init_UI()

    def init_UI(self):
        self.setWindowTitle("Insert Dates")
        self.setWindowModality(Qt.ApplicationModal)
        self.resize(400,400)

        okButton = QPushButton("OK", self)

        closeButton = QPushButton("Close", self)

        btnBox = QHBoxLayout()
        btnBox.addStretch(1)
        btnBox.addWidget(okButton)
        btnBox.addWidget(closeButton)

        vertBox = QVBoxLayout()
        vertBox.addStretch(1)
        vertBox.addLayout(btnBox)

        self.setLayout(vertBox)

        self.show()

def showDialog():
    dialog = insertDates()
    result = dialog.exec_()

