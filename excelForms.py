import openpyxl

wb = openpyxl.load_workbook('C:\\Users\\marvi\\Downloads\\example.xlsx')
sheet = wb['Sheet1']

print(list(sheet.columns)[1])

for cellObj in list(sheet.columns)[1]:
    print(cellObj.value)