import argparse
import pyexcel as pe

import gui

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Filter spreadsheet')
    parser.add_argument('file', help='file name')
    args = parser.parse_args()
    filename = args.file

    gui.GUI(filename)

# sheet.save_as(input("Save as: "))

