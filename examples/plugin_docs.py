# Note: This is not a Python file meant to be executed.
# This is just a document that gives you an idea of the
# Plugin class and all of the different things you could
# do with it.

# dougsheets.Plugin class
class Plugin:
    OPEN_PROMPT = wx.FD_OPEN | wx.FD_FILE_MUST_EXIST
    SAVE_PROMPT = wx.FD_SAVE | wx.FD_OVERWRITE_PROMPT

    def init(self):

    def exampleAction(e):

    def createMenu(self, text):

    def createMenuItem(self, menu, text, action=exampleAction, help="", id=wx.ID_ANY):

    def col2num(self, col):

    def showMessage(self, title, question, styles=wx.OK):

    def getFilePath(self, type=OPEN_PROMPT, message="File Dialog", default_directory=None, default_filename=None, wildcard_file_selector="*"):

    def getDialog(self, title, question):

    def getSheetObject(self):

    def updateSheet(self):

    def __init__(self, gui, menu):
        # The init function. You do not typically
        # have to override this.

