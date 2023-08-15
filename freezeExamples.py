import openpyxl

wb = openpyxl.load_workbook('C:\\Users\\marvi\\Downloads\\updatedProduceSales.xlsx')
sheet = wb.active
sheet.freeze_panes = 'A2'
wb.save("C:\\Users\\marvi\\Downloads\\produceSales.xlsx")