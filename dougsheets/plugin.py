import os
import string
import wx


class Plugin:
    OPEN_PROMPT = wx.FD_OPEN | wx.FD_FILE_MUST_EXIST
    SAVE_PROMPT = wx.FD_SAVE | wx.FD_OVERWRITE_PROMPT

    def init(self):
        # This is the method you would overwrite
        pass


    def exampleAction(self, e):
        print("This is an example menu item action. Please assign your own.")

    def createMenu(self, text):
        if not self.gui.headless:
            menu = wx.Menu()
            self.gui.MenuBar.Append(menu, text)
            return menu
        else:
            return None

    def createMenuItem(self, menu, text, action=exampleAction, help="", id=wx.ID_ANY, cli_help=None):
        if not self.gui.headless:
            item = menu.Append(id, text, help)
            self.gui.frame.Bind(wx.EVT_MENU, action, item)
        else:
            if cli_help is None and help is not None:
                cli_help = help
            self.gui.repl.commandlist.append({
                "cmd": text.lower().replace(" ", "_"),
                "help": cli_help,
                "action": action
            })

    def col2num(self, col):
        num = 0
        for c in col:
            if c in string.ascii_letters:
                num = num * 26 + (ord(c.upper()) - ord('A')) + 1
        return num

    def is_number(self, s):
        try:
            float(s)
            return True
        except ValueError:
            pass

        try:
            import unicodedata
            unicodedata.numeric(s)
            return True
        except (TypeError, ValueError):
            pass
        return False

    def showMessage(self, title, text, styles=wx.OK):
        self.gui.showMessage(title, text, styles)

    def getFilePath(self, type=OPEN_PROMPT, message="File Dialog", default_directory=None, default_filename=None, wildcard_file_selector="*"):
        if not self.gui.headless:
            base = os.path.basename(self.gui.filename)
            dir = self.gui.filename.replace(base, '')
            if not default_directory:
                default_directory = dir
            if not default_filename:
                default_filename = base
            openFileDialog = wx.FileDialog(self.gui.frame, message, default_directory, default_filename, wildcard_file_selector, type)
            the_modal = openFileDialog.ShowModal()
            if the_modal == wx.ID_CANCEL:
                return None
            choosen_path = openFileDialog.GetPath()
            openFileDialog.Destroy()
            return choosen_path
        else:
            if type == self.OPEN_PROMPT:
                return input("What is the name of the file? ")
            else:
                return input("What should we name the file? ")

    def getDialog(self, title, question):
        return self.gui.getDialog(title, question)

    def getSheetObject(self):
        return self.gui.sheetObject

    def updateSheet(self):
        self.gui.update_sheet()

    def isHeadless(self):
        if self.gui.headless:
            return True
        else:
            return False

    def hasCLIArguments(self, dict):
        if self.isHeadless():
            if dict.get('arguments', False):
                return True
            else:
                return False
        else:
            return False

    def CLIVar(self, var, dict):
        if self.isHeadless():
            if dict.get(var, False):
                return dict[var]
            else:
                return None
        else:
            return None

    def getInput__Variable(self, var, title, text, e):
        if self.CLIVar(var, e):
            the_variable = self.CLIVar(var, e)
        else:
            the_variable = self.getDialog(title, text)
        return the_variable

    def getInput__Column(self, var, title, text, e):
        if self.CLIVar(var, e):
            the_column = self.CLIVar(var, e)
            if not self.is_number(the_column):
                the_column = self.col2num(the_column) - 1
        else:
            userinput = self.getDialog(title, text)
            if userinput:
                the_column = self.col2num(userinput) - 1
                if col == None or col < 0:
                    return None
                else:
                    return the_column
            else:
                return None
        return the_column

    def __init__(self, gui, menu):
        self.gui = gui
        self.menu = menu
        self.init()

