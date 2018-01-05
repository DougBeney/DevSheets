import os
from os.path import expanduser
import argparse

import pyexcel as pe

from dougsheets import plugin
from dougsheets import spreadsheet

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Filter spreadsheet')
    parser.add_argument('file', help='file name')
    args = parser.parse_args()
    filename = args.file

    SysPluginDirectory = os.path.abspath('sysplugins/')
    UserPluginDirectory = os.path.join(expanduser('~'), '.config/dougsheets/plugins')

    print(UserPluginDirectory)
    if not os.path.exists(UserPluginDirectory):
        os.makedirs(UserPluginDirectory)

    spreadsheet.NewWindow(filename, [SysPluginDirectory, UserPluginDirectory])

# sheet.save_as(input("Save as: "))

