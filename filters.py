import string
import wx

import copy

# The Global Window Object
the_window = None

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

def col2num(col):
    num = 0
    for c in col:
        if c in string.ascii_letters:
            num = num * 26 + (ord(c.upper()) - ord('A')) + 1
    return num

# ####################################### #
# ================FILTERS================ #
# ####################################### #

def delete_patterned_rows(event):
    userinput = the_window.getDialog("Domain Quality Filter", "What column holds your URLS?")
    if userinput:
        url_col = int(col2num(userinput)) - 1
        if url_col == None or url_col < 0:
            the_window.showMessage("Failure", "Can't run filter. Please make sure you've provided proper input.")
        else:
            newSheetObject = []

            sheetObject = the_window.sheetObject

            for col in sheetObject:
                newSheetObject.append(
                    [str(col[0]), []]
                )
            print(newSheetObject)
            counter = 0
            for url in sheetObject[url_col][1]:
                if not contains_bad_pattern(url):
                    for i in range(0, len(newSheetObject)):
                        newSheetObject[i][1].append(sheetObject[i][1][counter])
                counter += 1

            print("============OLD===============")
            print(the_window.sheetObject[3][1][0])
            print("============NEW===============")
            print( newSheetObject[3][1][0] )
            the_window.sheetObject = newSheetObject.copy()
            the_window.update_sheet()

FUNCTION_LIST = [
    {
        "title": "Domain Quality",
        "function": delete_patterned_rows
    }
]
