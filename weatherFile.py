import sys, pyperclip,webbrowser

if len(sys.argv) > 1:
   weather = ''.join(sys.argv[1:])
else:
    weather = pyperclip.paste()

webbrowser.open("https://weather.com/weather/today/" + weather)