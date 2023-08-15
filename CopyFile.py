import send2trash

baconFile = open('careerwise.txt', 'a')   # create the file
baconFile.write("Bacon is not a vegetable")
baconFile.close()
print(send2trash.send2trash('careerwise.txt'))
