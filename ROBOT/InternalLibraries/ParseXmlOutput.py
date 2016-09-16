
import xml.etree.ElementTree as ET
from __builtin__ import str
import smtplib
from email.MIMEMultipart import MIMEMultipart
from email.MIMEBase import MIMEBase
from email.MIMEText import MIMEText
from email import Encoders
import os

def Process_XML_Output_For_Email_Subject(filepath):
    root = ET.parse(filepath)
    testCaseName = []
    status = []
    total = 0
    pass_count = 0
    fail_count = 0
    for element in root.findall('.//suite'):
        total+=1
        testCaseName.append(element.attrib.get('name'))
        print testCaseName
        stat = element.find('./status').attrib.get('status')
        element.find('./')
        status.append(stat)
        if stat == 'PASS' :
            pass_count+=1
        if stat == 'FAIL':
            fail_count+=1
    value = " Total : "+str(total)+", Pass : "+str(pass_count)+", Fail : "+str(fail_count)
    return value

def Process_XML_Output_For_Email_Text(filepath):
    root = ET.parse(filepath)
    suitName = {}
    testCaseName = []
    status = []
    string = "\n"
    htmlText="""\
    <html>
        <body>
            <table border="1" style="width:100%">
                <th>
                    <td><h3>Suit Name</h3></td>
                    <td><h3>Total</h3></td>
                    <td><h3>Pass</h3></td>
                    <td><h3>Fail</h3></td>
                </th>
    """
    sname = ""
    for elementSuite in root.findall('.//suite'):
        sname=elementSuite.attrib.get('name')
        total = 0
        pass_count = 0
        fail_count = 0
        for elementTest in elementSuite.findall('test'):
            total+=1
            stat = elementTest.find('./status').attrib.get('status')
            status.append(stat)
            if stat == 'PASS' :
                pass_count+=1
            if stat == 'FAIL':
                fail_count+=1
        if(total!=0 and not str(sname).startswith("None")):
            htmlText=htmlText+"<tr><td>*</td><td>"+sname+"</td><td>"+str(total)+"</td><td>"+str(pass_count)+"</td><td>"+str(fail_count)+"</td></tr>"
            suitName[sname] = " Total : "+str(total)+", Pass : "+str(pass_count)+", Fail : "+str(fail_count)
            string = string+str(sname)+" - "+suitName[sname]+"\n"
    htmlText=htmlText+"</table></body></html>"
    return htmlText

def Process_XML_Output_For_Email_hari(filepath):
    root = ET.parse(filepath)
    suite = []
    for elementSuite in root.findall('./suite'):
        suite.append(elementSuite.attrib.get('name'))
    return suite

# Process_XML_Output_For_Email_Subject("C:\Users\novopay-pc\AppData\Local\Temp\RIDEf1fggk.d\\output.xml")
         
