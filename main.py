import argparse
import pyexcel as pe

from dougsheets import plugin
from dougsheets import spreadsheet

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Filter spreadsheet')
    parser.add_argument('file', help='file name')
    args = parser.parse_args()
    filename = args.file

    spreadsheet.NewWindow(filename, './plugins')

# sheet.save_as(input("Save as: "))

