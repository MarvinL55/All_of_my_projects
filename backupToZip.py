
#backupToZip.py  - Copies an entire folder and it's contents
#a zip file whose file name incerments

import zipfile, os

def backupToZip(folder):

    folder = os.path.abspath(folder)

    number = 1
    while True:
        zipFilename = os.path.basename(folder) + '_' + str(number) + '.zip'
        if not os.path.exists(zipFilename):
            break
        number = number +1

    print(fr'Creating {zipFilename}...')
    backupZip = zipfile.ZipFile(zipFilename, 'w')

    for foldername, subfolder, filenames in os.walk(folder):
        print(f"Adding files in {folder}...")
        #Adding the current folder to the zip file
        backupZip.write(foldername)

        for filename in filenames:
            newBase = os.path.basename(folder) + '_'
            if filename.startswitch(newBase) and filename.endswitch('.zip'):
                continue
            backupZip.write(os.path.join(foldername, filename))
    backupZip.close()
    print("done")
backupToZip("C:\\Zippy")