
import smtplib
from email.MIMEMultipart import MIMEMultipart
from email.MIMEBase import MIMEBase
from email.MIMEText import MIMEText
from email import Encoders
import os
       
def send_mail_with_attachment(from_user,from_password,to, subject, text,html, attach):
    msg = MIMEMultipart()
    msg['From'] = from_user
    msg['To'] = to
#     ", ".join(to)
    msg['Subject'] = subject
    msg.attach(MIMEText(text,'plain'))
    msg.attach(MIMEText(html,'html'))
    attachments = attach.split(',')
    for filename in attachments:
            f = filename
            part = MIMEBase('application', "octet-stream")
            part.set_payload( open(f,"rb").read() )
            Encoders.encode_base64(part)
            part.add_header('Content-Disposition', 'attachment; filename="%s"' % os.path.basename(f))
            msg.attach(part)
    mailServer = smtplib.SMTP("smtp.gmail.com", 587)
    mailServer.ehlo()
    mailServer.starttls()
    mailServer.ehlo()
    mailServer.login(from_user, from_password)
    mailServer.sendmail(from_user, to.split(','), msg.as_string())
    mailServer.close()
          
# send_mail_with_attachment("klautomation@moolya.com", "klmoolya#automate123", "yatheendra@moolya.com", "Sample", "Hi", "F:\\Repository\\SampleRfTest\\TestSuites\\sample_results\\report.html,F:\\Repository\\SampleRfTest\\TestSuites\\sample_results\\log.html")







