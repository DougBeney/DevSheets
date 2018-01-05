from dougsheets import plugin


class Info(plugin.Plugin):
    def about_menu(self, e):
        text = "DougSheets v.0.0.1\n" +\
        "Created by Doug Beney\n" +\
        "dougie.io\n" +\
        "\n" +\
        "Enabled Plugins:"

        for plugin in self.gui.pluginmanager.enabled_plugins:
            text += "\n- " + plugin
        self.showMessage("About DougSheets:", text)

    def init(self):
        helpmenu = self.createMenu("Help")
        self.createMenuItem(helpmenu, "About", self.about_menu)

settings = {
    "class": Info
}

