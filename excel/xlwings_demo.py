import xlwings as xw
# https://zhuanlan.zhihu.com/p/23998083
# 连接到 excel

workbook = xw.Book("myexcel.xlsx") # 连接到excel 文件

# 连接到指定单元格
data_range = workbook.sheets('sheet1').range("A1")

# 写入数据 
data_range.value = [1,2,3]

# 保存

workbook.save()

