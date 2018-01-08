import os
import string
import wx

class Plugin:
    OPEN_PROMPT = wx.FD_OPEN | wx.FD_FILE_MUST_EXIST
    SAVE_PROMPT = wx.FD_SAVE | wx.FD_OVERWRITE_PROMPT
    def init(self):
        # This is the method you would overwrite
        pass

    def exampleAction(e):
        print("This is an example menu item action. Please assign your own.")

    def createMenu(self, text):
        if not self.gui.headless:
            menu = wx.Menu()
            self.gui.MenuBar.Append(menu, text)
            return menu
        else:
            return None

    def createMenuItem(self, menu, text, action=exampleAction, help="", id=wx.ID_ANY):
        if not self.gui.headless:
            item = menu.Append(id, text, help)
            self.gui.frame.Bind(wx.EVT_MENU, action, item)

    def col2num(self, col):
        num = 0
        for c in col:
            if c in string.ascii_letters:
                num = num * 26 + (ord(c.upper()) - ord('A')) + 1
        return num

    def showMessage(self, title, question, styles=wx.OK):
        self.gui.showMessage(title, question, styles)

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
            print("A plugin attempted to open a file picker GUI. This is currently not supported in headless mode.")

    def getDialog(self, title, question):
        return self.gui.getDialog(title, question)

    def getSheetObject(self):
        return self.gui.sheetObject

    def updateSheet(self):
        self.gui.update_sheet()

    def __init__(self, gui, menu):
        self.gui = gui
        self.menu = menu
        self.init()

