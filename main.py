import os
from os.path import expanduser
import argparse

from dougsheets import plugin
from dougsheets import spreadsheet

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Filter spreadsheet')
    parser.add_argument('file', help='file name')
    parser.add_argument('--cli', action='store_true', help='Use commands instead of a GUI')
    args = parser.parse_args()
    filename = args.file
    headless = args.cli

    if os.path.isfile(filename):
        SysPluginDirectory = os.path.abspath('sysplugins/')
        if not os.path.exists(SysPluginDirectory):
            if os.name is not "nt":
                SysPluginDirectory = "/etc/dougsheets/sysplugins"
            else:
                SysPluginDirectory = os.path.join(os.getenv('APPDATA'), "dougsheets/sysplugins")

        if os.name is not "nt":
            UserPluginDirectory = os.path.join(expanduser('~'), '.config/dougsheets/plugins')
        else:
            # I am sorry that you have to use Windows :(
            UserPluginDirectory = os.path.join(os.getenv('APPDATA'), "dougsheets/plugins")

        if not os.path.exists(UserPluginDirectory):
            os.makedirs(UserPluginDirectory)

        spreadsheet.NewWindow(filename, [SysPluginDirectory, UserPluginDirectory], headless)
    else:
        print("DougSheets: File does not exist: " + filename)

