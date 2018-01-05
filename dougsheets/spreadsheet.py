import wx
import wx.grid
import pyexcel as pe

from . import pluginmanager


class NewWindow:
    def init_window(self):
        self.MainPanel = wx.Panel(self.frame)
        self.sheetWidget = wx.grid.Grid(self.MainPanel)
        self.sheetWidget.CreateGrid(1, 1)
        self.sheetWidget.EnableEditing(False)
        self.sheetWidget.SetDefaultCellBackgroundColour(wx.Colour(255, 255, 255))
        self.sheetWidget.SetDefaultCellTextColour(wx.Colour(48, 48, 48))
        sizer = wx.BoxSizer(wx.VERTICAL)
        sizer.Add(self.sheetWidget, 1, wx.EXPAND)
        self.MainPanel.SetSizer(sizer)


    def init_menu(self):
        # Menu Bar
        self.MenuBar = wx.MenuBar()
        self.frame.SetMenuBar(self.MenuBar)

        # File Menu
        self.menu_file = wx.Menu()
        self.MenuBar.Append(self.menu_file, '&File')
        save = self.menu_file.Append(wx.ID_SAVE, 'Save')
        saveas = self.menu_file.Append(wx.ID_SAVEAS, 'Save as')
        fitem = self.menu_file.Append(wx.ID_EXIT, 'Quit', 'Quit application')
        self.frame.Bind(wx.EVT_MENU, self.OnQuit, fitem)

        # Filters Menu
        self.menu_filter = wx.Menu()
        self.MenuBar.Append(self.menu_filter, 'Filters')

    def clear_sheet(self, rows, cols):
        cur_rows = self.sheetWidget.GetNumberCols()
        cur_cols = self.sheetWidget.GetNumberRows()
        self.sheetWidget.DeleteCols(0, cur_cols)
        self.sheetWidget.DeleteRows(0, cur_rows)
        self.sheetWidget.AppendCols(cols)
        self.sheetWidget.AppendRows(rows)


    def load_sheet(self, filename):
        loaded_sheet = pe.get_dict(file_name=filename)
        self.sheetObject = list(loaded_sheet.items())
        self.update_sheet()

    def update_sheet(self):
        sheetObject = self.sheetObject

        max_cols = len(sheetObject)
        max_rows = 1
        for col in sheetObject:
            if len(col[1]) > max_rows:
                max_rows = len(col[1])+1
        self.clear_sheet(max_rows, max_cols)
        for col_index in range(0, len(sheetObject)):
            self.sheetWidget.SetCellValue(0, col_index, sheetObject[col_index][0])
            for row_index in range(0, len(sheetObject[col_index][1])):
                self.sheetWidget.SetCellValue(row_index+1, col_index, str(sheetObject[col_index][1][row_index]))


    def OnQuit(self, e):
        self.Close()

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

    def __init__(self, filename, pluginDir="~/.config/dougsheets"):
        app = wx.App()
        self.frame = wx.Frame(None, -1, filename)
        # Setting size twice to avoid sheet glitch
        self.frame.SetSize((500, 600))
        self.frame.Show()
        self.frame.SetSize((800, 600))

        self.init_window()
        self.init_menu()
        self.load_sheet(filename)
        pluginmanager.LoadPlugins(self, pluginDir)
        self.frame.Show()
        self.frame.Center()
        app.MainLoop()
