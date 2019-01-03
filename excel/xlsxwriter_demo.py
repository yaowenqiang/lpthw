import xlsxwriter as xw

workbook = xw.Workbook("mybook.xlsx")

WORKSHEEt = workbook.add_worksheet()

worksheet.write("A1",1)

workbook.close()
