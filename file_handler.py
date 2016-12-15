#!/usr/bin/python3.5

import csv


class CSVFile:
    def __init__(self):
        pass

    def create(self):
        pass

    def read(self, file):
        out = []
        with open(file) as csvFile:
            for row in csv.reader(csvFile):
                out += [row]

        return out

    def write(self, file, data):
        with open(file, 'w') as csvFile:
            csv_write = csv.writer(csvFile)
            for row in data:
                csv_write.writerow(row)


class XLSXFile:
    def __init__(self):
        pass

    def create(self):
        pass

    def read(self):
        pass

    def write(self):
        pass


if __name__ == '__main__':
    c = CSVFile()
    c.write('/home/winston/Desktop/test1.csv', c.read('/home/winston/Desktop/test.csv'))

