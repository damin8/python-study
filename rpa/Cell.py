from openpyxl import Workbook
from random import *

wb = Workbook()
ws = wb.active
ws.title = "Favian's Sheet"

index = 1

for x in range(1, 11):
    for y in range(1, 11):
        ws.cell(x, y, index)
        index += 1

wb.save("sample.xlsx")
