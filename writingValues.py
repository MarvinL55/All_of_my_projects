import openpyxl

wb = openpyxl.Workbook()

sheet = wb['Sheet']
sheet['A1'] = 'Hello, world'
print(sheet['A1'].value)