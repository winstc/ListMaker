#!/usr/bin/python3.5
# Written by Winston Cadwell
# This file contains the main logic and interface code
# for the list maker program.

import sys  # import system library
from PyQt5 import QtCore
from PyQt5.QtWidgets import QDialog, QAbstractItemView, QApplication, QStatusBar, QAction, QMainWindow, QPushButton, QVBoxLayout, QHBoxLayout, QTableWidget, QFileDialog, \
    QTableWidgetItem, QInputDialog, QMessageBox, QProgressDialog  # import the needed Qt widgets
import file_handler as fh  # import file_handler.py
import insertDates as idate


class MainWindow(QMainWindow):  # class for the main window of the program

    def __init__(self):  #

        super().__init__()

        self.init_UI()  # call init_UI method

    def init_UI(self):  # handles the setup of the MainWindow

        self.current_file = None  # create a variable that will be used to store the currently opened file name

        self.updated = False
        self.updating = False
        self.defaultRots = 0
        self.live = False

        self.resize(500, 500)  # resize the window
        self.move(300, 300)  # move the window away from the screen edge
        self.setWindowTitle('List Maker')  # set the window title

        openAction = QAction('Open', self)
        openAction.setShortcut('Ctrl+O')
        openAction.setStatusTip('Open a file')
        openAction.triggered.connect(self.open)

        saveAction = QAction('Save', self)
        saveAction.setShortcut('Ctrl+S')
        saveAction.setStatusTip('Save current document')
        saveAction.triggered.connect(self.save)

        exportXLSXAction = QAction('Export to XLSX', self)
        exportXLSXAction.setShortcut('Ctrl+E')
        exportXLSXAction.setStatusTip('Export to XLSX')
        exportXLSXAction.triggered.connect(self.save)

        quitAction = QAction('Quit', self)
        quitAction.triggered.connect(self._close)

        addRowsAction = QAction('Add Rows', self)
        addRowsAction.setShortcut('Ctrl+I')
        addRowsAction.setStatusTip('Add row to table')
        addRowsAction.triggered.connect(self.addrow)

        deleteRowAction = QAction('Delete Row', self)
        deleteRowAction.setStatusTip('Delete Selected Row')
        deleteRowAction.setShortcut('Delete')
        deleteRowAction.triggered.connect(self.deleteRow)


        addDatesAction = QAction('Add Dates', self)
        addDatesAction.setShortcut('Ctrl+D')
        addDatesAction.setStatusTip('Add Dates to table')
        addDatesAction.triggered.connect(self.addDates)

        self.updateLiveAction = QAction('Live', self, checkable=True)
        self.updateLiveAction.triggered.connect(self.toggleLive)

        updateNormalAction = QAction('Normal Update', self)
        updateNormalAction.setShortcut('Ctrl+U')
        updateNormalAction.setStatusTip('Updates the list')
        updateNormalAction.triggered.connect(self.update_normal)

        fileMenu = self.menuBar().addMenu("File")
        fileMenu.addAction(openAction)
        fileMenu.addAction(saveAction)
        fileMenu.addAction(exportXLSXAction)
        fileMenu.addAction(quitAction)

        editMenu = self.menuBar().addMenu("Edit")
        editMenu.addAction(deleteRowAction)

        insertMenu = self.menuBar().addMenu("Insert")
        insertMenu.addAction(addRowsAction)
        insertMenu.addAction(addDatesAction)

        updateMenu = self.menuBar().addMenu("Update")
        updateMenu.addAction(self.updateLiveAction)
        updateMenu.addAction(updateNormalAction)

        self.statusBar = QStatusBar()
        self.setStatusBar(self.statusBar)

        self.statusBar.showMessage("Ready...")

        # create and configure the main table
        self.jobtable = QTableWidget()  # create a new table widget
        self.jobtable.insertColumn(0)  # add a new column at index 0
        self.jobtable.insertColumn(0)  # add a new column at index 0
        self.jobtable.insertRow(0)  # add a new row at index 0
        self.jobtable.cellChanged.connect(self.table_change)

        self.setCentralWidget(self.jobtable)  # set the window layout to use veryBox for the layout

        self.jobtable.setSelectionBehavior(QAbstractItemView.SelectRows)

        self.show()  # show the main window

    def open(self):  # called when user clicks the open button
        file_name = QFileDialog.getOpenFileName(self, 'Open File', '/home/', "Comma Separated Value (*.csv);;Text File (*.txt)")  # create a new 'open file' dialog
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

        # prompt user for location and name of file
        file_name = QFileDialog.getSaveFileName(self, 'Save File', self.current_file,
                                                "Comma Separated Value (*.csv)")
        if file_name[0] != '':  # if the selected path is not blank
            csv_f = fh.CSVFile(file_name[0])  # create new instance of CSVFile class using selected filename
            csv_f.write(self.read_table_data())  # get data from table write it to .csv file
            return 1  # return if save was attempted
        else:  # if file name was blank
            return 0  # return 0

    def export_XLSX(self):
        data = []  # used to store the data read from table
        # prompt user for file path and name
        file_name = QFileDialog.getSaveFileName(self, 'Save File', self.current_file,
                                                "XLSX File (*.xlsx)")
        if file_name[0] != '':  # if the file path is not blank
            xlsx_f = fh.XLSXFile(file_name[0], "Sheet1")  # create new instance of XLSXFile class
            xlsx_f.write(self.read_table_data()) # get data from table write it to .xlsx file
            return 1  # return if save was attempted
        else:  # if file name was blank
            return 0  # return 0

    def addrow(self):  # adds rows to the table
        # ask the user how many row they want
        num_of_rows = QInputDialog.getInt(self, 'Add Rows', 'Number of Rows to Insert', 1)

        if num_of_rows[1]:  # if the dialog exits with a yes
            for i in range(num_of_rows[0]):  # for number of requested rows
                self.jobtable.insertRow(self.jobtable.rowCount())  # add row at the end of the table

    def deleteRow(self):
        for index in sorted(self.jobtable.selectionModel().selectedRows(), reverse=True):
            self.jobtable.removeRow(index.row())

    def update_normal(self):
        self.updated = True

        # prompt user for number of rotations - default is the number of rows it the table
        num_rotations = QInputDialog.getInt(self, 'Update', 'Number of Rotations', self.jobtable.rowCount())
        self.defaultRots = num_rotations[0]

        if num_rotations[1]:
            self.update_list(num_rotations[0])

    def update_list_old(self, rotations):  # add rotations to the list

        self.updating = True

        if rotations:  # if user confirms dialog
            if self.jobtable.columnCount() > 2:  # if there are at least two columns in the table
                for x in range(self.jobtable.columnCount(), 1, -1):  # for every column but the first two
                    self.jobtable.removeColumn(x)  # delete the column
            if self.jobtable.columnCount() == 2:  # if there are only two columns
                rotation = 1  # stores the current rotation

                # create a progress bar dialog - without this the UI would appear unresponsive
                progress = QProgressDialog("Generating List...", "Cancel", 0, rotations)
                progress.setWindowModality(QtCore.Qt.ApplicationModal)

                # for each column in the rotation
                for c in range(self.jobtable.columnCount(), rotations + self.jobtable.columnCount() - 1):
                    if progress.wasCanceled():  # if cancel button clicked
                        break  # break the loop

                    self.jobtable.insertColumn(self.jobtable.columnCount())  # add another column at end of table
                    offset = 0  # stores the offset of each column
                    print("TEST {0}-{1}".format(c, offset))
                    progress.setValue(rotation)  # update the progress bar
                    for r in range(self.jobtable.rowCount()):  # for each row in each column
                        try:
                            item = QTableWidgetItem(self.jobtable.item(r, 1).data(0))  # create a new table item
                            if rotation + r < self.jobtable.rowCount():  # if r is less than the row count
                                self.jobtable.setItem(rotation + r, c, item)  # insert the item into the table
                            else:  # if bottom of table is reached - start at top of table
                                self.jobtable.setItem(offset, c, item)  # insert item into the table
                                offset += 1  # increment offset

                        except TypeError:  # if it doesn't work
                            pass  # do nothing

                    rotation += 1  # increment rotation

        self.updating = False

    def update_list(self, rotations):
        self.updating = True  # set updating variable to true to prevent problems while updating

        # set the correct number of columns
        if self.jobtable.columnCount()-1 < rotations:  # check if we need more columns
            for n in range(rotations-self.jobtable.columnCount()+1):  # for each needed column
                self.jobtable.insertColumn(self.jobtable.columnCount())  # add a column at the end of the table
        elif self.jobtable.columnCount()-1 > rotations:  # if there are too many columns
            for n in range(self.jobtable.columnCount()-rotations-1):  # for each column to be deleted
                self.jobtable.removeColumn(self.jobtable.columnCount()-1)  # add a column at the end of the table

        offset = 0

        # start filling columns
        for col in range(2, rotations+1):  # for each column in rotation minus the start rotation
            offset +=1
            if offset == self.jobtable.rowCount():
                offset = 0
            for row in range(self.jobtable.rowCount()):
                prow = row + offset
                if row + offset >= self.jobtable.rowCount():
                    prow = prow - self.jobtable.rowCount()
                print(prow)

                try:
                    item = QTableWidgetItem(self.jobtable.item(row, 1).data(0))  # create a new table item
                    self.jobtable.setItem(prow, col, item)  # insert the item into the table


                except TypeError:  # if it doesn't work
                    pass  # do nothing



    def _close(self):  # called when user clicks the close button
        if self.current_file:  # if there is an open file
            self.save_on_exit()  # prompt user to save
        else:

            sys.exit()  # else just exit

    def save_on_exit(self):
        save = QMessageBox()  # create a dialog box to prompt user to save
        save.setText("You are about to exit.")  # set dialog text
        save.setInformativeText("Do you want to save your work?")  # set dialog subtext
        save.setStandardButtons(QMessageBox.Save | QMessageBox.Cancel | QMessageBox.Discard)  # add buttons to dialog
        save.setDefaultButton(QMessageBox.Save)  # set the default button

        return_val = save.exec_()  # show the dialog

        if return_val == QMessageBox.Save:  # if uses selects save
            if self.save():  # call save method -  if user saves
                sys.exit()  # exit
        elif return_val == QMessageBox.Cancel:  # if user selects cancel
            pass  # do nothing
        elif return_val == QMessageBox.Discard:  # if user selects discard
            sys.exit()  # exit

    def read_table_data(self):  # read data from the table returns it as a list
        data = []  # used to store the data read from table

        for row in range(self.jobtable.rowCount()):  # for each row in the table
            rowdata = []  # temporarily stores row data
            for column in range(self.jobtable.columnCount()):  # read each row column by column
                item = self.jobtable.item(row, column).data(0)  # read the data of cell at coordinate (row, column)
                rowdata.append(item)  # append the cell to row data
            data.append(rowdata)  # append the completed row to full data list

        return data  # return the table data

    def toggleLive(self):
        self.live = self.updateLiveAction.isChecked()

    def table_change(self):
        if not self.updating:
            self.statusBar.showMessage("Reviewing Changes...")
            if self.updated and self.live:
                self.update_list(self.defaultRots)
            else:
                self.statusBar.showMessage("Skipping Update")

    def addDates(self):
        idate.showDialog()

def run_main_program():
    app = QApplication(sys.argv)  # create a new QApplication
    ex = MainWindow()  # create the main window

    sys.exit(app.exec_())  # exit when the app closes

