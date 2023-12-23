import os
from email.message import EmailMessage as Emailmsg
import ssl
import smtplib
import csv
email_sender = 'anushkajhingran30@gmail.com'
email_password = 'oopl vzbd aalo cnta'
#email_password = os.environ.get('email_password')
#email_receiver = 'anushkajhingran@gmail.com'
subject = 'testing email sender'
body = '''
<h1>Just started making email sender.</h1>
'''
with open('sendemail.csv', 'r') as csvfile:
  reader = csv.reader(csvfile)
  for line in reader:
    text = 'Congratulations'+line[1]+', you are selected.'
    email_receiver = line[0]
    em = Emailmsg()
    em['From'] = email_sender
    em['To'] = email_receiver
    em['Subject'] = subject