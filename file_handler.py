#!/usr/bin/python3.5
# Written by Winston Cadwell
# file_handler classes used by List Maker to manipulate files
# these classes are used for all file actions in List Maker
# The CSVFile class contains files for csv file manipulation
# The XLSX class contains files for excel file manipulation

import csv  # import csv library for csv file manipulation
import xlsxwriter  # import xlsx library for excel file manipulation


class CSVFile:  # class for read/writing of .csv files
    def __init__(self, file):
        self.file = file  # store the requested file path

    def read(self):  # reads csv file into a list
        out = []  # list to store read data
        with open(self.file) as csvFile:  # open the file
            for row in csv.reader(csvFile):  # for each row in the file
                out += [row]  # append it to the list

        return out  # return the list

    def write(self, data):  # writes csv file
        with open(self.file, 'w') as csvFile:  # open the file
            csv_write = csv.writer(csvFile)  # create a new writer
            for row in data:  # row each row
                csv_write.writerow(row)  # write the row


class XLSXFile:  # class for read/writing of .xlsx files
    def __init__(self, path, worksheet):
        self.workbook = xlsxwriter.Workbook(path)  # set up the workbook
        self.worksheet = self.workbook.add_worksheet(worksheet)  # add a worksheet

    def write(self, data):  # writes xlsx file
        for index, row in enumerate(data):  # for each row in data
            self.worksheet.write_row('A' + str(index + 1), row)  # write it the the spread sheet

    def close(self):  # closes the workbook
        self.workbook.close()  # close the workbook
