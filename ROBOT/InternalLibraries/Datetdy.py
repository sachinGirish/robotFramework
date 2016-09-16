'''
Created on 14-Dec-2015

@author: USER
'''
import time
import calendar
import pymysql.cursors
from datetime import date
from datetime import datetime
from datetime import datetime
from dateutil.relativedelta import relativedelta
from dateutil import parser
from dateutil.parser import parse


def Datevalue():
    """Format dd mmmm yyyy"""
    now=date.today().__format__("%d %B %Y")
    return  now
def Dateformat2():
    """Format dd/mm/yyyy"""
    format2=date.today().__format__("%d/%m/%Y")
    return  format2

def First_Repay_Date():
    holidays = []
    holidaysList = [];
    connection = pymysql.connect(host='103.230.87.254',
                             user='root',
                             password='mysql',
                             port=6606,
                             database='novobank_mel_auto',
                             cursorclass=pymysql.cursors.DictCursor)
    try:
        with connection.cursor() as cursor:
            print("Getting List of Holidays from DB")
            sql1 = "SELECT `from_date` FROM `m_holiday`;"
            cursor.execute(sql1)
            holidays = cursor.fetchall()
            for holiday in holidays:
                holidaysList.append(holiday['from_date'])
            print("Getting List of Holidays from DB has been completed")
    finally:
        connection.close()
    flag = True
    date_after_month = datetime.today()
    dayOfMonth = date_after_month.day
    monthend = (date_after_month+relativedelta(day=31)).day
    if dayOfMonth >=1 and dayOfMonth <=20:
        date_after_month = date_after_month+relativedelta(day=31)
        date_after_month = date_after_month+relativedelta(days=1)
        weekday = calendar.weekday(date_after_month.year, date_after_month.month, date_after_month.day)
        while flag is True:
            if int(weekday) == 5:
                date_after_month = date_after_month + relativedelta(days=2)
            elif int(weekday) == 6:
                date_after_month = date_after_month + relativedelta(days=1)
            elif holidaysList.__contains__(date_after_month):
                date_after_month = date_after_month + relativedelta(days=1)
            else:
                flag = False
                         
    elif dayOfMonth >=21 and dayOfMonth <=monthend:
        date_after_month = date_after_month+relativedelta(day=31)
        date_after_month = date_after_month+relativedelta(months=1)
        date_after_month = date_after_month+relativedelta(days=1)
        weekday = calendar.weekday(date_after_month.year, date_after_month.month, date_after_month.day)
#         print (date_after_month in holidays.values())
        while flag is True:
            if int(weekday) == 5:
                date_after_month = date_after_month + relativedelta(days=2)
            elif int(weekday) == 6:
                date_after_month = date_after_month + relativedelta(days=1)
            elif holidaysList.__contains__(date_after_month):
                date_after_month = date_after_month + relativedelta(days=1)
            else:
                flag = False
    return date_after_month.strftime('%d %B %Y')

def Date_Operation(mydate,key,value,operation):
    """"mydate=(cdate,custom date format=dd mmmm yyyy) 
        key=(days,months,years)
        value=(number)
        operation=(add,sub)"""
    if mydate=='cdate':
        date_today = datetime.today()
    else:
        date_today=parse(mydate)
    if operation=='add':
        if key=='years':
            date_minus_days = date_today + relativedelta(years=int(value))
        elif key=='months':
            date_minus_days = date_today + relativedelta(months=int(value))
        else:
            date_minus_days = date_today + relativedelta(days=int(value))
    else:
        if key=='years':
            date_minus_days = date_today - relativedelta(years=int(value))
        elif key=='months':
            date_minus_days = date_today - relativedelta(months=int(value))
        else:
            date_minus_days = date_today - relativedelta(days=int(value))
    return date_minus_days.strftime('%d %B %Y')
    
def Date_Operation2(mydate,key,value,operation):
    """"mydate=(cdate,custom date format=dd/mm/yyyy) 
        key=(days,months,years)
        value=(number)
        operation=(add,sub)"""
    if mydate=='cdate':
        date_today = datetime.today()
    else:
        date_today=parse(mydate)
    if operation=='add':
        if key=='years':
            date_minus_days = date_today + relativedelta(years=int(value))
        elif key=='months':
            date_minus_days = date_today + relativedelta(months=int(value))
        else:
            date_minus_days = date_today + relativedelta(days=int(value))
    else:
        if key=='years':
            date_minus_days = date_today - relativedelta(years=int(value))
        elif key=='months':
            date_minus_days = date_today - relativedelta(months=int(value))
        else:
            date_minus_days = date_today - relativedelta(days=int(value))
    return date_minus_days.strftime('%d/%m/%Y')