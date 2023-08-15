# renameDates.py - renames filenames with american MM-DD-YYY date formats
# to European DD-MM-YYY
import shutil, os, re

datePattern = re.compile(r"""^(.*?)
    ((0|1)?\d)-
    ((0|1|2|3)?\d)-
    ((19|20)\d\d)
    (.*?)$
    """, re.VERBOSE)

# loop over the file in the working directory
for amerFilename in os.listdir('.'):

    mo = datePattern.search(amerFilename)

    # Skip files without a date
    if mo == None:
        continue

beforePart = mo.group(1)
monthPart = mo.group(2)
dayPart = mo.group(4)
yearPart = mo.group(6)
afterPart = mo.group(8)

datePattern = re.compile(r"""^(1)
      (2 (3) )-
      (4 (5) )-
      (6 (7) )
      (8)$
      """, re.VERBOSE)

euroFilename = beforePart + dayPart + '-' + monthPart + '-' + yearPart + afterPart

# get the full, absolute file path
absWorkingDir = os.path.abspath('.')
amerFilename = os.path.join(absWorkingDir, amerFilename)
euroFilename = os.path.join(absWorkingDir, euroFilename)

print(f'Renaming " {amerFilename}" to "{euroFilename}...')
# shutil.move(amerFilename, euroFilename)
