import re
import pyexcel as pe
import os

class CreateREPL:
    def cmd_help(self, dict):
        print("DougSheets CLI Help Menu:")
        for cmd in self.commandlist:
            print("> ", cmd['cmd'])
            if cmd.get('help', False):
                print('   ', cmd['help'])

    def cmd_quit(self, dict):
        self.running = False
        print("Bye, bye! ;)")

    def cmd_clear_screen(self, dict):
        if os.name == 'nt':
            os.system('cls')
        else:
            os.system('clear')

    def cmd_sheet(self, dict):
        sheet = pe.get_sheet(array=self.gui.sheetObject)
        print(sheet)

    def getCommandInfo(self, command):
        for cmd in self.commandlist:
            curcmd = cmd['cmd']
            if type(curcmd) is list:
                for cmdvariation in curcmd:
                    if cmdvariation == command:
                        return cmd
            else:
                if curcmd == command:
                    return cmd
        print("Command not found :(")
        return None


    def Array2Dict(self, object):
        dict = {"arguments": []}

        # Safetly get index in array
        def get(index, array):
            try:
                data = array[index]
            except IndexError:
                data = None
            return data

        skiplist = []
        for i in range(0, len(object)):
            if i is 0:
                dict.update({"first_word": object[i]})
            else:
                if i not in skiplist:
                    if get(i+1, object) == "=":
                        dict.update({
                            object[i]: object[i+2]
                        })
                        skiplist.append(i+1)
                        skiplist.append(i+2)
                    elif object[i] is not "=":
                        dict['arguments'].append(object[i])
        if len(dict['arguments']) == 0:
            dict['arguments'] = None
        return dict


    def Input2Array(self, user_input):
        if user_input:
            sections = []
            curword = ""
            quotemode = False
            for char in user_input:
                if char is " " and not quotemode:
                    if curword.replace(' ', '') is not "":
                        sections.append(curword)
                    curword = ""
                elif char is "=" and not quotemode:
                    if curword.replace(' ', '') is not "":
                        sections.append(curword)
                    if sections[len(sections)-1] is not "=":
                        sections.append("=")
                    curword = ""
                elif char is "'" or char is '"':
                    quotemode = not quotemode
                else:
                    curword += char
            if curword.replace(' ', '') is not "":
                sections.append(curword)
            return sections
        else:
            return None

    def REPL_LOOP(self):
        while self.running:
            try:
                user_input = input('➜ ')
                object = self.Input2Array(user_input)
                dict = None
                command = None
                if object:
                    dict = self.Array2Dict(object)
                    if dict:
                        command = self.getCommandInfo(dict['first_word'])
                if command:
                    command['action'](dict)

            except(KeyboardInterrupt, EOFError):
                print('')
                self.running = False

    def __init__(self, gui):
        # Note: 'gui' is simply a reference to the spreadsheet class
        #       and not actually a referenc to a GUI.
        print('Welcome to DougSheets CLI!')
        print("sheet: " + str(gui.filename))
        self.gui = gui
        self.commandlist = [
            {
                "cmd": "help",
                "action": self.cmd_help
            },
            {
                "cmd": ['clear', 'cls', 'c'],
                "action": self.cmd_clear_screen
            },
            {
                "cmd": ['quit', 'exit', 'bye', 'q'],
                "action": self.cmd_quit
            },
            {
                "cmd": "sheet",
                "action": self.cmd_sheet
            },
        ]

        self.running = True
