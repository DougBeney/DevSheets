import string
import wx

class Plugin:
    def init(self):
        # This is the method you would overwrite
        pass

    def exampleAction(e):
        print("This is an example menu item action. Please assign your own.")

    def createMenu(self, text):
        menu = wx.Menu()
        self.gui.MenuBar.Append(menu, text)
        return menu

    def createMenuItem(self, menu, text, action=exampleAction, help="", id=wx.ID_ANY):
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
