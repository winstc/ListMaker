# Job List Maker
This is program for making rotation lists for jobs, chores, etc. The user can create a list with multiple jobs and names
that rotate. The lists are saved as a standard Comma Separated Value (*.csv) and can be exported to an Xecel Spreadsheet.


## Installation

### Prerequisites
   
 * [Python3](https://www.python.org/downloads/)
 * [PyQt5](https://www.riverbankcomputing.com/software/pyqt/download5)
 * [xlsxwriter](http://xlsxwriter.readthedocs.io/)

##### On Ubuntu:
```bash
$ sudo apt-get install python3 pip3
$ pip install PyQt5 xlsxwriter
```

### Running the Software

* On GNU/Linux
 * Open a terminal at the location containing this software
 * Run `python3 ListMaker.py`

 
## Instructions

##### Creating a New Document
 1. Start a new instance of Job List Maker
 2. The software automatically add one row with two columns
 3. Click the _Add Rows_ button
 4. You will be prompted to enter the number of rows, not including already existing rows. (Rows should normally corespont to people)
 5. There should now be two columns with the correct number of rows
 6. Populate Data
    * _Column 1_ should be used for names of people
    * _Column 2_ should be used for the jobs

##### Updating Rotations
 1. The table must have at leats one row populated with data
 2. After verifying that all data has been entered correctly, click the _Update_ Button
 3. You will be prompted for a number. Enter the number of desired rotations (This includes _Column 2_)
 4. Select _OK_ to continue (This will overwrite all columns past _Column 2_)
 5. Columns should now be updated

## Credits
Written By: Winston Cadwell