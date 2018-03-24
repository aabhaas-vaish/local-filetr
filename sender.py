#Creation of random_access
#Run this on a machine with Python 2.7.x only. Python 3 might show some problems!
#This program will terminate should it encounter any errors and after completely sending the file to the receiver

import socket
import time

local = raw_input("Please input the receiver IP: ")
s = socket.socket()
print("Connecting to receiver server...")

while True:
    try:
        s.connect((local, 44000))
        break
    except:
        print("Retrying connection to receiver server...")
        time.sleep(1)

print("Connection Successful!")
print("Please select file")
from Tkinter import Tk
from tkFileDialog import askopenfilename

Tk().withdraw()
filename = askopenfilename()
filename = list(filename)

for i in range(len(filename)):
    if filename[i] == '/':
        filename[i] = '\\\\'
    else:
        pass

filename = ''.join(filename)

f = open(filename,'r')
message = f.readlines()
data = ''
for i in message:
    data += i
f.close()

print("Sending your file...")
s.send(data)

print("File sent! Receiver has your file!")
s.close()
time.sleep(3)
quit()
