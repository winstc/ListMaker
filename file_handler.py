#!/usr/bin/python3.5
# Written by Winston Cadwell
# file_handler classes used by List Maker to manipulate files
# these classes are used for all file actions in List Maker
# The CSVFile class contains files for csv file manipulation
# The XLSX class contains files for excel file manipulation

import csv  # import csv library for csv file manipulation
import xlsxwriter  # import xlsx library for excel file manipulation
import json


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

class JSONFile:  # class for read/writing of .csv files
    def __init__(self, file):
        self.file = file  # store the requested file path

    def writeJson(self, data, live=False, updated=False, default_rots=0):
        with open(self.file, 'w') as file:
            file.write(json.dumps({"live": live, "updated": updated, "defaultRots": default_rots,"data": data}, sort_keys=True, indent=4))

    def readJsonTable(self):
        with open(self.file, 'r') as file:
            JSON_String = file.read()
            parsed_JSON = json.loads(JSON_String)

            return parsed_JSON['data']

    def readJson(self, value):
        with open(self.file, 'r') as file:
            JSON_String = file.read()
            parsed_JSON = json.loads(JSON_String)

        if value == "live":
            return parsed_JSON['live']
        elif value == "updated":
            return parsed_JSON['updated']
        elif value == "defaultRots":
            return parsed_JSON['defaultRots']
        else:
            return None

class XLSXFile:  # class for read/writing of .xlsx files
    def __init__(self, path, worksheet):
        self.workbook = xlsxwriter.Workbook(path)  # set up the workbook
        self.worksheet = self.workbook.add_worksheet(worksheet)  # add a worksheet

    def write(self, data):  # writes xlsx file
        for index, row in enumerate(data):  # for each row in data
            self.worksheet.write_row('A' + str(index + 1), row)  # write it the the spread sheet

    def close(self):  # closes the workbook
        self.workbook.close()  # close the workbook

