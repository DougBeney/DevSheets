import os
import sys

class LoadPlugins:
    def list_plugins(self, path):
        for filename in os.listdir(path):
            name, ext = os.path.splitext(filename)
            if ext.endswith(".py"):
                yield name

    def import_plugin(self, plugin):
        m = __import__(plugin)

    def __init__(self, gui, pluginDir):
        self.gui = gui

        lib_path = os.path.abspath(pluginDir)
        sys.path.append(lib_path)

        for plugin in self.list_plugins(pluginDir):
            module = __import__(plugin)
            settings = getattr(module, 'settings')
            settings['class'](gui, "whatever")

