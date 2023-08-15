import openpyxl, pprint

print("Opening workbook...")
wb = openpyxl.load_workbook("C:\\Users\\marvi\\Downloads\\censuspopdata.xlsx")
sheet = wb['Population by Census Tract']
countryData = {}

print('reading rows...')
for row in range(2, sheet.max_row + 1):
    state = sheet['B' + str(row)].value
    country = sheet['C' + str(row)].value
    pop = sheet['D' + str(row)].value

    #make sure that the state exists
    countryData.setdefault(state, {})
    #make sure that the state key exists for this state
    countryData[state].setdefault(country, {'tracts': 0, 'pop': 0})

    #each row represents one census tract, so increment by one
    countryData[state][country]['tracts'] += 1
    #Increase the country pop by the pop in this census tract
    countryData[state][country]['pop'] += int(pop)

print('writing result...')
resultFile = open('census2010.py', 'w')
resultFile.write('allData = ' + pprint.pformat(countryData))
resultFile.close()
print("Done")