'''
Created on 23-Sep-2015

@author: Hari Krishna R
'''
import string
import re
def StringValue(str):
    replacevalue=re.sub("[^0-9.]+","",str)
    return replacevalue
