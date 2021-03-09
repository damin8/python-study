from openpyxl import load_workbook

wb = load_workbook("sample.xlsx")
ws = wb.active

ws.delete_rows(8)  # 8 번째 줄에 있는 데이터 삭제
ws.delete_rows(8, 3)  # 8 번째 줄부터 3줄의 데이터 삭제

ws.delete_cols(2) # 2번째 열 (B) 삭제
ws.delete_cols(2, 2) # 2번째 열 부터 2개의 열 삭제
