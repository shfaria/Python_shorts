import pandas as pd

# All university list
alllist = '/Users/shfaria/Documents/Overall Monthly NOC report/2022/October 2022/alluniversities.xls'

universitiesAvailabilty = pd.read_excel(alllist, sheet_name= 'apublic')
universitiesBandwidth = pd.read_excel(alllist, sheet_name= 'bpublic')
universitiesZoom = pd.read_excel(alllist, sheet_name= 'zpublic')


# uni_pub = pd.read_excel(alllist, sheet_name= 'zpublic')
# uni_pub = pd.read_excel(alllist, sheet_name= 'zpublic')
# uni_pub = pd.read_excel(alllist, sheet_name= 'zpublic')

# # Availabilty
# availfile = str(input("Please enter the absolute path of the Availability file: "))
# avai_sheet = str(input("Please enter the name of the sheet of the Availability file: "))
# availabilityReport = pd.read_excel(availfile, sheet_name = avai_sheet, index_col = 0)
# avail = pd.merge(universitiesAvailabilty, availabilityReport, how = 'outer', on = 'Name')
# avail.to_excel("/Users/shfaria/Documents/Overall Monthly NOC report/2022/December 2022/availability-december.xlsx")
# # # Bandwidth
# bandfile = str(input("Please enter the absolute path of the Bandwidth file: "))
# band_sheet = str(input("Please enter the name of the sheet of the Bandwidth file: "))
# bandwidthReport = pd.read_excel(bandfile, sheet_name = band_sheet, index_col = 0)
# band = pd.merge(universitiesBandwidth, bandwidthReport, how = 'outer', on = 'Name')
# band.to_excel("/Users/shfaria/Documents/Overall Monthly NOC report/2022/December 2022/bandwidth-december.xlsx")
# # Zoom
zfile = str(input("Please enter the absolute path of the Zoom file: "))
zoom_sheet = str(input("Please enter the name of the sheet of the Zoom file: "))
vfile = str(input("Please enter the absolute path of the Vsession file: "))
vsess_sheet = str(input("Please enter the name of the sheet of the Vsession file: "))

zoomReport = pd.read_excel(zfile, sheet_name = zoom_sheet, index_col = 0)
vsessReport= pd.read_excel(vfile, sheet_name = vsess_sheet, index_col = 0)

f3 = pd.merge(zoomReport, vsessReport, how = 'outer', on = 'Name').fillna(0)
f3.to_excel("Zoom-summary.xlsx")

zoomSummary = '/Users/shfaria/Documents/Django-projects/python projects/Zoom-summary.xlsx'
zoomReportFinal = pd.read_excel(zoomSummary, sheet_name = 'Sheet1', index_col = 0)

zoomReportFinal['TotalClasses'] = zoomReportFinal['Number of Meeting']  + zoomReportFinal['Total_Class_Taken'] 
zoomReportFinal['TotalClasses'].head()

zoomReportFinal['Totalhours'] = zoomReportFinal['Sum of Duration']  + zoomReportFinal['Total_Hours'] 
zoomReportFinal['Totalhours'].head()

zoomReportFinal['TotalParticipants'] = zoomReportFinal['Sum of Participants']  + zoomReportFinal['Total_Participants'] 
zoomReportFinal['TotalParticipants'].head()

zoomReportFinal.to_excel("testzoom.xlsx")

zoomReportFinal0 = pd.read_excel("testzoom.xlsx", sheet_name = 'Sheet1', index_col = 0)

f4 = pd.merge(universitiesZoom, zoomReportFinal0, how = 'outer', on = 'Name')
f4.to_excel("Vcon-november.xlsx")
