# import openpyxl module
import openpyxl
unilist = '/Users/shfaria/Documents/Overall Monthly NOC report/2022/October 2022/alluniversities.xlsx'

wb_obj = openpyxl.load_workbook(unilist)
# sheet_obj = wb_obj.active
x = wb_obj.worksheets[1]
 
# print the total number of rows
print(x)