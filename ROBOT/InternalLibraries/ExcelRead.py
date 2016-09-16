'''
Created on 23-Sep-2015

@author: 
'''
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
                    value2=sheet.row_values(i,0)
    values = []
    for value in value2:
        if type(value) is float:
            values.append(int(value))
        else:
            value = value.encode('ascii', 'ignore').decode('ascii')
            values.append(str(value))
    return values
                        
def uniquedata(xlsname,sheetname):
    book = open_workbook(xlsname)
    sheet = book.sheet_by_name(sheetname)
    rows = sheet.nrows
    value = []
    for j in range(2,rows):
        disburse=sheet.cell_value(j,0)
        value.append(disburse)
    return value

def rowscount(xlsname,sheetname):
    book = open_workbook(xlsname)
    sheet = book.sheet_by_name(sheetname)
    rows = sheet.nrows
    return rows
                    
                    
                

        
    



#value2=Excel('C:/Python27/Scripts/Novopay/Novobank/New/Data.xls', 'Login','TO')
#print "values :" ,value2


    