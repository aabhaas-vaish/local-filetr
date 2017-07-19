#Creation of random_access
#Run this on a machine with Python 2.7.x only. Python 3 might show some problems!
#Should be run on a machine connected to the sender through a local network such as a WiFi router. This should provide an IP of the form 192.168.x

import socket, os, time

s = socket.socket()
my_ip = socket.gethostbyname(socket.gethostname())
s.bind((my_ip, 44000))
s.listen(1)

print "Please input this IP in the sender program: " + my_ip

print("Waiting for connection...")
sc, addr = s.accept()
print("Connection Successful!")

print("Waiting for the incoming file...")
q = sc.recv(12800000)
print("File Received!")

save = raw_input("Please name the received file: ")

if '.' not in save:
    save = save + '.txt'
else:
    pass

t = open(save,'w')
t.writelines(q)
t.close()

print "File received! Check present working folder"
time.sleep(2)
s.close()

quit()
