import xlwt
import xlrd
import xlutils

# 打开excel文件
workbook = xlrd.open_workbook("myexclee.xls")

worksheet = workbook.sheet_by_index(0)

data = worksheet.cell_value(0,0)

wb = xlwt.Workbook()

# 新建excel

wb = xlwt.Workbook()

sh = wb.add_sheet('Sheet1')

sh.write(0,0,'data')

wb.save('myexcel.xls')

