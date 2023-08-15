import openpyxl

wb = openpyxl.load_workbook('C:\\Users\\marvi\\Downloads\\example.xlsx')
sheet = wb['Sheet1']

for rowOfCellObject in sheet['A1' : 'C3']:
    for cellObj in rowOfCellObject:
        print(cellObj.coordinate, cellObj.value)
    print('---END OF ROW---')