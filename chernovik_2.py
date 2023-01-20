import xlrd
import xlwt

workbook = xlrd.open_workbook('/Users/macbook/Downloads/GB - Motis.xlsx')

# Open the worksheet
sheet = workbook.sheet_by_index(0)

# Iterate the rows and columns
# for i in range(0, rows):
#     for j in range(0, column):
#         # Print the cell values with tab space
#         print(worksheet.cell_value(i, j), end='\t')
#     print('')

data = [sheet.cell_value(0, col) for col in range(sheet.ncols)]

workbook = xlwt.Workbook()
sheet = workbook.add_sheet('test')

for index, value in enumerate(data):
    sheet.write(0, index, value)

workbook.save('/Users/macbook/Downloads/output.xls')
