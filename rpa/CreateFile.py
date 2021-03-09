from openpyxl import Workbook

wb = Workbook()
ws = wb.active
ws.title = "Favian's sheet"
wb.save("sample.xlsx")
wb.close()