import webbrowser, sys, pyperclip

if len(sys.argv) > 1:
    address = ''.join(sys.argv[1:])
else:
    #Get address from command line
    address = pyperclip.paste()

webbrowser.open("https://www.google.com/maps/place/" + address)
