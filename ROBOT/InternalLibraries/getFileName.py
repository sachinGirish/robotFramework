
import os
from os import listdir
from os.path import isfile,expanduser

def New_File_In_Directory(previousFiles,laterFiles):
    newFileName = ''
    for file in laterFiles:
        if file not in previousFiles:
            newFileName = str(file)
            break
    return newFileName


def Get_User_Home_Directory_Path():
    home = expanduser("~")
    return str(home)