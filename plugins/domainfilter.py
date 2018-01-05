from dougsheets import plugin

bad_patterns = [
    "blogspot",
    "wordpress.com",
    "weebly.com",
    "wix.com",
    ".shopify.com"
]

def contains_bad_pattern(string):
    for pattern in bad_patterns:
        if pattern in str(string):
            return True
    return False

class MyPlugin(plugin.Plugin):
    def domainQualityAction(self, e):
        userinput = self.getDialog("Domain Quality Filter", "What column holds your URLS?")
        if userinput:
            url_col = int(self.col2num(userinput)) - 1
            if url_col == None or url_col < 0:
                self.gui.showMessage("Failure", "Can't run filter. Please make sure you've provided proper input.")
            else:
                newSheetObject = []

                sheetObject = self.gui.sheetObject

                for col in sheetObject:
                    newSheetObject.append(
                        [str(col[0]), []]
                    )
                counter = 0
                for url in sheetObject[url_col][1]:
                    if not contains_bad_pattern(url):
                        for i in range(0, len(newSheetObject)):
                            newSheetObject[i][1].append(sheetObject[i][1][counter])
                    counter += 1

                self.gui.sheetObject = newSheetObject.copy()
                self.gui.update_sheet()

    def init(self):
        gui = self.gui
        self.createMenuItem(gui.menu_filter, "Domain Quality", self.domainQualityAction)

settings = {
    "class": MyPlugin
}

