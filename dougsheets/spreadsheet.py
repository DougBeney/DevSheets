import os
import wx
import wx.grid
import pyexcel as pe

from . import pluginmanager
from . import repl


class NewWindow:
    def init_window(self):
        self.MainPanel = wx.Panel(self.frame)
        self.sheetWidget = wx.grid.Grid(self.MainPanel)
        self.sheetWidget.CreateGrid(1, 1)
        self.sheetWidget.EnableEditing(False)
        # self.sheetWidget.SetDefaultCellBackgroundColour(wx.Colour(255, 255, 255))
        # self.sheetWidget.SetDefaultCellTextColour(wx.Colour(48, 48, 48))
        sizer = wx.BoxSizer(wx.VERTICAL)
        sizer.Add(self.sheetWidget, 1, wx.EXPAND)
        self.MainPanel.SetSizer(sizer)


    def init_menu(self):
        if not self.headless:
            # Menu Bar
            self.MenuBar = wx.MenuBar()
            self.frame.SetMenuBar(self.MenuBar)

            # File Menu
            self.menu_file = wx.Menu()
            self.MenuBar.Append(self.menu_file, '&File')

            # Edit Menu
            self.menu_edit = wx.Menu()
            self.MenuBar.Append(self.menu_edit, '&Edit')

            # Filter Menu
            self.menu_filter = wx.Menu()
            self.MenuBar.Append(self.menu_filter, 'F&ilters')
        else:
            self.menu_file = None
            self.menu_edit = None
            self.menu_filter = None

    def clear_sheet(self, rows, cols):
        cur_rows = self.sheetWidget.GetNumberCols()
        cur_cols = self.sheetWidget.GetNumberRows()
        self.sheetWidget.DeleteCols(0, cur_cols)
        self.sheetWidget.DeleteRows(0, cur_rows)
        self.sheetWidget.AppendCols(cols)
        self.sheetWidget.AppendRows(rows)


    def load_sheet(self, filename):
        # loaded_sheet = pe.get_dict(file_name=filename)
        self.sheetObject = pe.get_array(file_name=filename)
        if not self.headless:
            self.update_sheet()

    def update_sheet(self):
        sheetObject = self.sheetObject

        amount_of_rows = len(sheetObject)
        amount_of_cols = 1

        for col in sheetObject:
            if len(col) > amount_of_cols:
                amount_of_cols = len(col)
        self.clear_sheet(amount_of_rows, amount_of_cols)
        for r in range(0, len(sheetObject)):
            for c in range(0, len(sheetObject[r])):
                self.sheetWidget.SetCellValue(r, c, str(sheetObject[r][c]))

    def getDialog(self, title, text):
        dlg = wx.TextEntryDialog(self.frame, text, title)
        if dlg.ShowModal() == wx.ID_OK:
            dlg.Destroy()
            return dlg.GetValue()
        else:
            dlg.Destroy()
            return None

    def showMessage(self, title, text, styles=wx.OK):
        wx.MessageBox(str(text), str(title), styles)

    def __init__(self, filename, pluginDirs, headless=False):
        self.headless = headless
        if not headless:
            # Enter GUI Mode
            app = wx.App()
            self.frame = wx.Frame(None, -1, filename)
            # Setting size twice to avoid sheet glitch
            self.frame.SetSize((500, 600))
            self.frame.Show()
            self.frame.SetSize((800, 600))

            self.init_window()
            self.init_menu()
            self.filename = filename
            self.load_sheet(filename)
            self.pluginmanager = pluginmanager.LoadPlugins(self, pluginDirs)
            self.frame.Show()
            self.frame.Center()
            app.MainLoop()
        else:
            # Enter Headless Mode
            # It is worth noting that in headless mode, the terminology of a 'menu' change
            # A 'menu' is no longer a visual menu in a GUI, but instead a set of commands
            # accessible by the CLI.
            self.init_menu()
            self.filename = filename
            self.load_sheet(filename)
            self.pluginmanager = pluginmanager.LoadPlugins(self, pluginDirs)
            repl.CreateREPL(self)
