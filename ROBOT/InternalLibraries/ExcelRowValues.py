
import xlrd
from xlrd.book import Book
from xlrd.sheet import Sheet

def Get_Excel_Row_Values(filepath,sheetName,uniqueValue):
    
    Book = xlrd.open_workbook(filepath)
    Sheet = Book.sheet_by_name(sheetName)
    row_count = Sheet.nrows
    col_count = Sheet.ncols
    for i in range(0,row_count):
        for j in range(0,col_count):
            value = Sheet.cell_value(i, j)
            if value == uniqueValue:
                row_values = Sheet.row_values(i, 0)           
    return row_values