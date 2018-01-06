import os
from os.path import expanduser
import argparse

from dougsheets import plugin
from dougsheets import spreadsheet

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Filter spreadsheet')
    parser.add_argument('file', help='file name')
    args = parser.parse_args()
    filename = args.file

    SysPluginDirectory = os.path.abspath('sysplugins/')
    UserPluginDirectory = os.path.join(expanduser('~'), '.config/dougsheets/plugins')

    if not os.path.exists(UserPluginDirectory):
        os.makedirs(UserPluginDirectory)

    spreadsheet.NewWindow(filename, [SysPluginDirectory, UserPluginDirectory])

