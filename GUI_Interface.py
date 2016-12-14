#!/usr/bin/python3.5

import sys
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QVBoxLayout, QTableWidget, QHBoxLayout

class mainWindow(QWidget):
    def __init__(self):

        super().__init__()

        self.init_UI()

    def init_UI(self):

        self.resize(500, 500)
        self.move(300, 300)
        self.setWindowTitle('List Maker')

        openBtn = QPushButton('Open', self)
        openBtn.clicked.connect(self.open)

        saveBtn = QPushButton('Save', self)
        saveBtn.clicked.connect(self.save)

        newItemBtn = QPushButton('New Item', self)
        newItemBtn.clicked.connect(self.newitem)

        exportBtn = QPushButton('Export', self)
        exportBtn.clicked.connect(self.export_XLSX)

        closeBtn = QPushButton('Close', self)
        closeBtn.clicked.connect(self.close)



        jobtable = QTableWidget()
        jobtable.setRowCount(1)
        jobtable.setColumnCount(5)

        btnBox = QHBoxLayout()
        btnBox.addStretch(1)
        btnBox.addWidget(openBtn)
        btnBox.addWidget(saveBtn)
        btnBox.addWidget(newItemBtn)
        btnBox.addWidget(exportBtn)
        btnBox.addWidget(closeBtn)


        vertBox = QVBoxLayout()
        vertBox.addWidget(jobtable)
        vertBox.addLayout(btnBox)

        self.setLayout(vertBox)

        self.show()

    def open(self):
        pass

    def save(self):
        pass

    def export_XLSX(self):
        pass

    def newitem(self):
        pass

    def close(self):
        sys.exit()


if __name__ == '__main__':

    app = QApplication(sys.argv)
    ex = mainWindow()
    sys.exit(app.exec_())