#!/usr/bin/python3.5

import sys
from PyQt5.QtGui import QStandardItemModel, QStandardItem
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QVBoxLayout, QHBoxLayout, QTableWidget, QFileDialog, QTableWidgetItem, QInputDialog, QMessageBox
import file_handler as fh


class MainWindow(QWidget):
    def __init__(self):

        super().__init__()

        self.init_UI()

    def init_UI(self):

        self.current_file = None

        self.model = QStandardItemModel()

        self.resize(500, 500)
        self.move(300, 300)
        self.setWindowTitle('List Maker')

        openBtn = QPushButton('Open', self)
        openBtn.clicked.connect(self.open)

        saveBtn = QPushButton('Save', self)
        saveBtn.clicked.connect(self.save)

        addRowBtn = QPushButton('Add Rows', self)
        addRowBtn.clicked.connect(self.addrow)

        updateBtn = QPushButton("Update", self)
        updateBtn.clicked.connect(self.update_list)

        exportBtn = QPushButton('Export', self)
        exportBtn.clicked.connect(self.export_XLSX)

        closeBtn = QPushButton('Close', self)
        closeBtn.clicked.connect(self._close)

        self.jobtable = QTableWidget()
        self.jobtable.itemChanged.connect(self.data_changed)
        self.jobtable.insertColumn(0)
        self.jobtable.insertColumn(0)
        self.jobtable.insertRow(0)

        btnBox = QHBoxLayout()
        btnBox.addStretch(1)
        btnBox.addWidget(openBtn)
        btnBox.addWidget(saveBtn)
        btnBox.addWidget(addRowBtn)
        btnBox.addWidget(updateBtn)
        btnBox.addWidget(exportBtn)
        btnBox.addWidget(closeBtn)

        vertBox = QVBoxLayout()
        vertBox.addWidget(self.jobtable)
        vertBox.addLayout(btnBox)

        self.setLayout(vertBox)

        self.show()

    def open(self):
        file_name = QFileDialog.getOpenFileName(self, 'Open File', '/home/', "Comma Separated Value (*.csv)")
        if file_name[0] != '':
            self.current_file = file_name[0]
            csv_f = fh.CSVFile(file_name[0])
            data = csv_f.read()

            self.jobtable.setRowCount(len(data))
            self.jobtable.setColumnCount(len(data[0]))

            for i, row in enumerate(data):
                for j, col in enumerate(row):
                    item = QTableWidgetItem(col)
                    self.jobtable.setItem(i, j, item)

    def save(self):
        data = []
        file_name = QFileDialog.getSaveFileName(self, 'Save File', self.current_file,
                                                "Comma Separated Value (*.csv)")
        if file_name[0] != '':
            for row in range(self.jobtable.rowCount()):
                rowdata = []
                for column in range(self.jobtable.columnCount()):
                    item = self.jobtable.item(row, column).data(0)
                    rowdata.append(item)
                data.append(rowdata)

            csv_f = fh.CSVFile(file_name[0])
            csv_f.write(data)
            return 1
        else:
            return 0

    def export_XLSX(self):
        data = []
        file_name = QFileDialog.getSaveFileName(self, 'Save File', self.current_file,
                                                "XLSX File (*.xlsx)")
        if file_name[0] != '':
            for row in range(self.jobtable.rowCount()):
                rowdata = []
                for column in range(self.jobtable.columnCount()):
                    item = self.jobtable.item(row, column).data(0)
                    rowdata.append(item)
                data.append(rowdata)

            xlsx_f = fh.XLSXFile(file_name[0], "Sheet1")
            xlsx_f.write(data)
            return 1
        else:
            return 0

    def addrow(self):
        num_of_rows = QInputDialog.getInt(self, 'Add Rows', 'Number of Rows to Insert', 1)

        if num_of_rows[1]:
            for i in range(num_of_rows[0]):
                self.jobtable.insertRow(self.jobtable.rowCount())

    def data_changed(self):
        pass

    def update_list(self):
        if self.jobtable.columnCount() > 2:
            for x in range(self.jobtable.columnCount(), 1, -1):
                print(x)
                self.jobtable.removeColumn(x)
        if self.jobtable.columnCount() == 2:
            num_rotations = QInputDialog.getInt(self, 'Update', 'Number of Rotations', self.jobtable.rowCount())
            rotation = 1
            if True:
                for c in range(self.jobtable.columnCount(), num_rotations[0] + self.jobtable.columnCount()-1):
                    self.jobtable.insertColumn(self.jobtable.columnCount())
                    offset = 0
                    for r in range(self.jobtable.rowCount()):
                        try:
                            item = QTableWidgetItem(self.jobtable.item(r, 1).data(0))
                            print(item.text())
                            if rotation + r < self.jobtable.rowCount():
                                self.jobtable.setItem(rotation + r, c, item)
                            else:
                                self.jobtable.setItem(offset, c, item)
                                offset += 1

                        except TypeError:
                            pass
                    rotation += 1

    def _close(self):
        if self.current_file:
            self.save_on_exit()
        else:
            sys.exit()

    def save_on_exit(self):
        save = QMessageBox()
        save.setText("You are about to exit.")
        save.setInformativeText("Do you want to save your work?")
        save.setStandardButtons(QMessageBox.Save | QMessageBox.Cancel | QMessageBox.Discard)
        save.setDefaultButton(QMessageBox.Save)

        return_val = save.exec_()

        if return_val == QMessageBox.Save:
            if self.save():
                sys.exit()
        elif return_val == QMessageBox.Cancel:
            pass
        elif return_val == QMessageBox.Discard:
            sys.exit()


if __name__ == '__main__':

    app = QApplication(sys.argv)
    ex = MainWindow()
    sys.exit(app.exec_())