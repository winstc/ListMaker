#!/usr/bin/python3.5

import sys  # import system library
from PyQt5.QtGui import QStandardItemModel  # import the QStandardItemModel object
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QVBoxLayout, QHBoxLayout, QTableWidget, QFileDialog, \
    QTableWidgetItem, QInputDialog, QMessageBox  # import the needed Qt widgets
import file_handler as fh  # import file_handler.py


class MainWindow(QWidget):  # class for the main window of the program

    def __init__(self):  #

        super().__init__()

        self.init_UI()  # call init_UI method

    def init_UI(self):  # handles the setup of the MainWindow

        self.current_file = None  # create a variable that will be used to store the currently opened file name

        self.resize(500, 500)  # resize the window
        self.move(300, 300)  # move the window away from the screen edge
        self.setWindowTitle('List Maker')  # set the window title

        openBtn = QPushButton('Open', self)  # create the open button
        openBtn.clicked.connect(self.open)  # link it to its method

        saveBtn = QPushButton('Save', self)  # create the save button
        saveBtn.clicked.connect(self.save)  # link it the its method

        addRowBtn = QPushButton('Add Rows', self)  # create the Add Rows button
        addRowBtn.clicked.connect(self.addrow)  # link it the its method

        updateBtn = QPushButton("Update", self)  # create the update button
        updateBtn.clicked.connect(self.update_list)  # link it the its method

        exportBtn = QPushButton('Export', self)  # create the export button
        exportBtn.clicked.connect(self.export_XLSX)  # link it the its method

        closeBtn = QPushButton('Close', self)  # create the close button
        closeBtn.clicked.connect(self._close)  # link it the its method

        # create and configure the main table
        self.jobtable = QTableWidget()  # create a new table widget
        self.jobtable.itemChanged.connect(self.data_changed)  # call data_changed method when user changes selection
        self.jobtable.insertColumn(0)  # add a new column at index 0
        self.jobtable.insertColumn(0)  # add a new column at index 0
        self.jobtable.insertRow(0)  # add a new row at index 0

        btnBox = QHBoxLayout()  # create a layout box for program buttons
        btnBox.addStretch(1)  # set the box to fill the window horizontally
        # add program buttons to the layout box
        btnBox.addWidget(openBtn)
        btnBox.addWidget(saveBtn)
        btnBox.addWidget(addRowBtn)
        btnBox.addWidget(updateBtn)
        btnBox.addWidget(exportBtn)
        btnBox.addWidget(closeBtn)

        vertBox = QVBoxLayout()  # create another layout box to hold the rest of the UI
        vertBox.addWidget(self.jobtable)  # add the table to the layout box
        vertBox.addLayout(btnBox)  # add the button layout box to vertBox

        self.setLayout(vertBox)  # set the window layout to use veryBox for the layout

        self.show()  # show the main window

    def open(self):  # called when user clicks the open button
        file_name = QFileDialog.getOpenFileName(self, 'Open File', '/home/', "Comma Separated Value (*.csv)")  # create a new 'open file' dialog
        if file_name[0] != '':  # if the file name isn't blank
            self.current_file = file_name[0]  # set current_file name to the file the user picked
            csv_f = fh.CSVFile(file_name[0])  # create a new 'CSVFile' instance from file_handler.py
            data = csv_f.read()  # read the .csv file

            # set columns and rows to match those of the file
            self.jobtable.setRowCount(len(data))
            self.jobtable.setColumnCount(len(data[0]))

            for i, row in enumerate(data):  # for each row in csv data
                for j, col in enumerate(row): # and each column in each row
                    item = QTableWidgetItem(col)  # create a new item with the data for current cell
                    self.jobtable.setItem(i, j, item)  # add it to the table

    def save(self):  # saves the currently opened file
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


if __name__ == '__main__':  # if file is launched by itself
        app = QApplication(sys.argv)  # create a new QApplication
        ex = MainWindow()  # create the main window
        sys.exit(app.exec_())  # exit when the app closes