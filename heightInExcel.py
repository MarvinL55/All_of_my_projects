import openpyxl

wb = openpyxl.Workbook()
sheet = wb.active
sheet['A1'] = 'tall row'
sheet['A2'] = 'wide row'

sheet.row_dimensions[1].height = 70
sheet.column_dimensions['B'].width = 20
wb.save("C:\\Users\\marvi\\Downloads\\dimensions.xlsx")