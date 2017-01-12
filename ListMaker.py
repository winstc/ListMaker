#!/usr/bin/python3.5
# this file simply check that dependencies are installed and runs the program

import GUI_Interface
import importlib as imp

run = True

found = imp.util.find_spec('PyQt5')
if found:
    ('PyQt5 Found...')
else:
    print('PyQt5 Not Found!! - Please install it...')
    run = False

found = imp.util.find_spec('xlsxwriter')
if found:
    print('XLSXWriter Found...')
else:
    print('PyQt5 Not Found!! - Please install it...')
    run = False

found = imp.util.find_spec('csv')
if found:
    print('csv Found...')
else:
    print('csv Not Found!! - Please install it...')
    run = False


if run:
    GUI_Interface.run_main_program()
else:
    print("Something Went Wrong")
    print("Please verify all dependencies are installed!")
