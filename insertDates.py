from PyQt5.QtWidgets import QDialog, QVBoxLayout, QHBoxLayout, QCalendarWidget, QPushButton, QRadioButton, QLabel, QSpinBox, QTableWidget, QTableWidgetItem
from PyQt5.QtCore import Qt, QDateTime
import sys

class insertDates(QDialog):
    def __init__(self, parent=None, table=QTableWidget, hasDates=False):
        super().__init__(parent)

        self.table = table
        self.hasDates = hasDates

        self.init_UI()

    def init_UI(self):
        self.setWindowTitle("Insert Dates")
        self.setWindowModality(Qt.ApplicationModal)
        self.resize(400,400)

        intervalLabel = QLabel("Rotation Interval:")
        self.mRotationsRBtn = QRadioButton("Monthly")
        self.mRotationsRBtn.setChecked(True)
        self.wRotationsRBtn = QRadioButton("Weekly")
        self.dRotationsRBtn = QRadioButton("Daily")
        self.cRotationsRBtn = QRadioButton("Custom:")
        self.customEntry = QSpinBox()
        self.customEntry.setRange(0, 365)
        self.customEntry.setFixedWidth(80)

        intervalBox = QVBoxLayout()
        intervalBox.addWidget(intervalLabel)
        intervalBox.addWidget(self.mRotationsRBtn)
        intervalBox.addWidget(self.wRotationsRBtn)
        intervalBox.addWidget(self.dRotationsRBtn)
        intervalBox.addWidget(self.cRotationsRBtn)
        intervalBox.addWidget(self.customEntry)

        startCalLabel = QLabel("Start Date:")

        self.startCal = QCalendarWidget()
        self.startCal.setGridVisible(True)
        self.startCal.selectionChanged.connect(self.dateChange)

        startCalBox = QVBoxLayout()
        startCalBox.addWidget(startCalLabel)
        startCalBox.addWidget(self.startCal)

        calBox = QHBoxLayout()
        calBox.addLayout(startCalBox)

        okButton = QPushButton("OK", self)
        okButton.clicked.connect(self._ok)

        closeButton = QPushButton("Close", self)
        closeButton.clicked.connect(self._close)

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

    def _close(self):
        self.destroy()

    def dateChange(self):
        pass

    def _ok(self):

        if not self.hasDates:
            self.table.insertRow(0)

        date = self.startCal.selectedDate()

        for i in range(self.table.columnCount() - 1):
            if self.dRotationsRBtn.isChecked():
                dateOut = date.addDays(i)
            elif self.wRotationsRBtn.isChecked():
                dateOut = date.addDays(i * 7)
            elif self.mRotationsRBtn.isChecked():
                dateOut = date.addMonths(i)
            elif self.cRotationsRBtn.isChecked():
                dateOut = date.addDays(i * self.customEntry.value())

            dateOut = dateOut.getDate()

            item = QTableWidgetItem("{}/{}/{}".format(dateOut[1], dateOut[2], dateOut[0]))  # create a new table item
            self.table.setItem(0, i + 1, item)  # insert the item into the table

        self.hasDates = True
        self.done(0)

def showDialog(parent, table=QTableWidget, hasDates=False):
    dialog = insertDates(parent, table, hasDates)
    result = dialog.exec_()
    return True

def updateDates(table=QCalendarWidget):
    pass

