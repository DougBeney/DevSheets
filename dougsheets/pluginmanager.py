import os
import sys

class LoadPlugins:
    def list_plugins(self, path):
        for filename in os.listdir(path):
            name, ext = os.path.splitext(filename)
            if ext.endswith(".py"):
                yield name

    def __init__(self, gui, pluginDirs):
        self.gui = gui
        self.enabled_plugins = []
        # Load the plugin directories in Python
        for thepath in pluginDirs:
            lib_path = os.path.abspath(thepath)
            sys.path.append(lib_path)

            # Load the plugins in the plugin directory
            for plugin in self.list_plugins(thepath):
                module = __import__(plugin)
                settings = getattr(module, 'settings')
                if settings:
                    settings['class'](gui, "whatever")
                    self.enabled_plugins.append(
                        settings.get('name', plugin) + " " + settings.get('version', '')
                   )

