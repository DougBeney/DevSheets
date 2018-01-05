import wx
from dougsheets import plugin

class FileOperations(plugin.Plugin):
    def save(self, e):
        pass

    def saveas(self, e):
        pass

    def init(self):
        self.createMenuItem(self.gui.menu_file, "Save", self.save, id=wx.ID_SAVE)
        self.createMenuItem(self.gui.menu_file, "Save as", self.saveas, id=wx.ID_SAVEAS)
        pass
settings = {
    "class": FileOperations
}

