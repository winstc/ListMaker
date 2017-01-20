from PyQt5.QtWidgets import QDialog, QVBoxLayout, QHBoxLayout, QCalendarWidget, QPushButton, QRadioButton, QLabel, QSpinBox
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

        intervalLabel = QLabel("Rotation Interval:")
        mRotationsRBtn = QRadioButton("Monthly")
        wRotationsRBtn = QRadioButton("Weekly")
        dRotationsRBtn = QRadioButton("Daily")
        cRotationsRBtn = QRadioButton("Custom:")
        customEntry = QSpinBox()
        customEntry.setRange(0, 365)
        customEntry.setFixedWidth(80)

        intervalBox = QVBoxLayout()
        intervalBox.addWidget(intervalLabel)
        intervalBox.addWidget(mRotationsRBtn)
        intervalBox.addWidget(wRotationsRBtn)
        intervalBox.addWidget(dRotationsRBtn)
        intervalBox.addWidget(cRotationsRBtn)
        intervalBox.addWidget(customEntry)

        startCalLabel = QLabel("Start Date:")

        startCal = QCalendarWidget()
        startCal.setGridVisible(True)

        startCalBox = QVBoxLayout()
        startCalBox.addWidget(startCalLabel)
        startCalBox.addWidget(startCal)

        endCalLabel = QLabel("End Date:")

        endCal = QCalendarWidget()
        endCal.setGridVisible(True)

        endCalBox = QVBoxLayout()
        endCalBox.addWidget(endCalLabel)
        endCalBox.addWidget(endCal)

        calBox = QHBoxLayout()
        calBox.addLayout(startCalBox)
        calBox.addLayout(endCalBox)

        okButton = QPushButton("OK", self)

        closeButton = QPushButton("Close", self)

        btnBox = QHBoxLayout()
        btnBox.addStretch(1)
        btnBox.addWidget(okButton)
        btnBox.addWidget(closeButton)

        vertBox = QVBoxLayout()
        vertBox.addLayout(intervalBox)
        vertBox.insertSpacing(20, 20)
        vertBox.addLayout(calBox)
        vertBox.addLayout(btnBox)

        self.setLayout(vertBox)

        self.show()

def showDialog():
    dialog = insertDates()
    result = dialog.exec_()

