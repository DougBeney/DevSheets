import wx
import pyexcel
from dougsheets import plugin

class FileOperations(plugin.Plugin):
    def save(self, e):
        save_dest = self.gui.filename
        pyexcel.save_as(array=self.gui.sheetObject, dest_file_name=save_dest)

    def saveas(self, e):
        if self.hasCLIArguments(e):
            save_file_path = e['arguments'][0]
        else:
            save_file_path = self.getFilePath(self.SAVE_PROMPT, "Save as")

        if save_file_path is not None:
            self.gui.filename = save_file_path
            self.save(None)
            if self.isHeadless():
                print("Saved!")

    def exit(self, e):
        self.gui.frame.Close()

    def init(self):
        self.createMenuItem(self.gui.menu_file, "Save", self.save, id=wx.ID_SAVE)
        self.createMenuItem(self.gui.menu_file, "Save as", self.saveas, id=wx.ID_SAVEAS)
        self.createMenuItem(self.gui.menu_file, "Exit", self.exit, id=wx.ID_EXIT)

settings = {
    "class": FileOperations
}

