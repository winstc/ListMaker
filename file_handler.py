#!/usr/bin/python3.5

import csv
import xlsxwriter


class CSVFile:
    def __init__(self, file):
        self.file = file

    def read(self):
        out = []
        with open(self.file) as csvFile:
            for row in csv.reader(csvFile):
                out += [row]

        return out

    def write(self, data):
        with open(self.file, 'w') as csvFile:
            csv_write = csv.writer(csvFile)
            for row in data:
                csv_write.writerow(row)


class XLSXFile:
    def __init__(self, path, worksheet):
        self.workbook = xlsxwriter.Workbook(path)
        self.worksheet = self.workbook.add_worksheet(worksheet)

    def write(self, data):
        for index, row in enumerate(data):
            self.worksheet.write_row('A' + str(index + 1), row)

    def close(self):
        self.workbook.close()
