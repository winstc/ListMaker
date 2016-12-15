#!/usr/bin/python3.5

import sys
from PyQt5.QtGui import QStandardItemModel, QStandardItem
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QVBoxLayout, QHBoxLayout, QTableWidget, QFileDialog, QTableWidgetItem
from file_handler import CSVFile as cvs_f


class MainWindow(QWidget):
    def __init__(self):

        super().__init__()

        self.init_UI()

    def init_UI(self):

        self.model = QStandardItemModel()

        self.resize(500, 500)
        self.move(300, 300)
        self.setWindowTitle('List Maker')

        openBtn = QPushButton('Open', self)
        openBtn.clicked.connect(self.open)

        saveBtn = QPushButton('Save', self)
        saveBtn.clicked.connect(self.save)

        newJobBtn = QPushButton('New Job', self)
        newJobBtn.clicked.connect(self.newitem)

        newPersonBtn = QPushButton('New Person', self)
        newPersonBtn.clicked.connect(self.newitem)

        exportBtn = QPushButton('Export', self)
        exportBtn.clicked.connect(self.export_XLSX)

        closeBtn = QPushButton('Close', self)
        closeBtn.clicked.connect(self.exit)

        self.jobtable = QTableWidget()

        btnBox = QHBoxLayout()
        btnBox.addStretch(1)
        btnBox.addWidget(openBtn)
        btnBox.addWidget(saveBtn)
        btnBox.addWidget(newJobBtn)
        btnBox.addWidget(newPersonBtn)
        btnBox.addWidget(exportBtn)
        btnBox.addWidget(closeBtn)

        vertBox = QVBoxLayout()
        vertBox.addWidget(self.jobtable)
        vertBox.addLayout(btnBox)

        self.setLayout(vertBox)

        self.show()

    def open(self):
        file_name = QFileDialog.getOpenFileName(self, 'Open File', '/home/winston/Desktop', "Comma Separated Value (*.csv)")
        data = cvs_f.read(self, file_name[0])

        self.jobtable.setRowCount(len(data))
        self.jobtable.setColumnCount(len(data[0]))

        for i, row in enumerate(data):
            for j, col in enumerate(row):
                item = QTableWidgetItem(col)
                self.jobtable.setItem(i, j, item)

    def save(self):
        data = []
        file_name = QFileDialog.getSaveFileName(self, 'Save File', '/home/winston/Desktop',
                                                "Comma Separated Value (*.csv)")
        for row in range(self.jobtable.rowCount()):
            print(row)
            rowdata = []
            for column in range(self.jobtable.columnCount()):
                print(column ,":")
                item = self.jobtable.item(row, column).data(0)
                print(item)
                rowdata.append(item)
                print(rowdata)
            data.append(rowdata)

        cvs_f.write(self, file_name[0], data)


    def export_XLSX(self):
        pass

    def newitem(self):
        pass

    def exit(self):
        sys.exit()


if __name__ == '__main__':

    app = QApplication(sys.argv)
    ex = MainWindow()
    sys.exit(app.exec_())