import pandas as pd

alllist = '/Users/shfaria/Documents/Overall Monthly NOC report/2022/October 2022/alluniversities.xls'
uni_pub = pd.read_excel(alllist, sheet_name= 'zpublic')

# availfile = str(input("Please enter the absolute path of the Availability file: "))
# avai_sheet = str(input("Please enter the name of the sheet of the Availability file: "))
# avail = pd.read_excel(availfile, sheet_name = avai_sheet, index_col = 0)

bandfile = '/Users/shfaria/Documents/Overall Monthly NOC report/2022/October 2022/Monthly Bandwidth Usage Report of October - 2022.xlsx'
band = pd.read_excel(bandfile, sheet_name = 'Sheet1', index_col = 0)
zfile = '/Users/shfaria/Documents/Overall Monthly NOC report/2022/October 2022/Processed zoom October 2022.xlsx'
vfile = '/Users/shfaria/Documents/Overall Monthly NOC report/2022/October 2022/vSession_2022_10.xlsx'
zoom = pd.read_excel(zfile, sheet_name = 'Sheet2', index_col = 0)
vsess= pd.read_excel(vfile, sheet_name = 'Sheet1', index_col = 0)

f3 = pd.merge(zoom, vsess, how = 'outer', on = 'Name')
f3.to_excel("totalZoom.xlsx")
totalzoomfile = '/Users/shfaria/Documents/Django-projects/python projects/totalZoom.xlsx'
totalzoom = pd.read_excel(totalzoomfile, sheet_name = 'Sheet1', index_col = 0)
f3 = pd.merge(uni_pub, totalzoom, how = 'outer', on = 'Name')
f3.to_excel("Vcon.xlsx")
