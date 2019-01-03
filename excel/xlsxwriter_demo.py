# coding=utf-8

import xlsxwriter as xw
from time import strftime, gmtime
timestr = strftime("-%d-%m-%Y",gmtime())

file_name = "周报-姚文强" + timestr + ".xlsx"
workbook = xw.Workbook(file_name)

worksheet = workbook.add_worksheet()

worksheet.write("A1","你好")

workbook.close()
