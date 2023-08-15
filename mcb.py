#mcb.pyw - Saves and load piece of text to the clipboard

#Usage - py.exe mcb.pyw save <keyword> - Saves clipbord to keyword
#py.exe mcb.pyw <keyword> - Load Keyword to clipboard
#py.exe mcb.pyw list - Load all keywords to clipboard

import shelve, pyperclip,sys

mcbShelf = shelve.open('mcb')

# ToDo: save clipboard content
if len(sys.argv) == 3 and sys.argv[1] == "save":
    mcbShelf[sys.argv[2]] = pyperclip.paste()
elif len(sys.argv) == 2:


    # TODO: List keyword and load content
    if sys.argv[1].lower() == 'list':
        pyperclip.copy(str(list(mcbShelf.keys())))
    elif sys.argv[1] in mcbShelf:
        pyperclip.copy(mcbShelf[sys.argv[1]])
mcbShelf.close()