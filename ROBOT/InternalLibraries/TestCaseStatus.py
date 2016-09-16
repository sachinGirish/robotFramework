


from xlrd import open_workbook

def Excel(filepath,Sheetname,uniq):

    wrkbook = open_workbook(filepath)
    sheet = wrkbook.sheet_by_name(Sheetname)
    rows = sheet.nrows
    cols = sheet.ncols

    for i in range(0,rows):
        for j in range(0,cols):
                value1 = sheet.cell_value(i,j)
                values = []
                if value1 == uniq:
                    value3=sheet.cell_value(i,1)
                    if value3 =="No":
                        return  value3





