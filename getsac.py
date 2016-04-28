# Echo client program
import socket
import os
import re
import textwrap

id = "sac"
#HOST = socket.gethostbyname('ec2-52-34-55-230.us-west-2.compute.amazonaws.com')
HOST = '52.34.55.230'    # The remote host
PORT = 1025              # The same port as used by the server
print HOST
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((HOST, PORT))
s.sendall(id)
data = s.recv(1024)
s.close()
print data
#print re.sub("(.{2})", " ", data, 0, re.DOTALL)
#os.popen("sh ble.sh"+' '+data)
final_data= ' '.join(textwrap.wrap(data, 2))
print final_data
fobj=open("cmd.txt", 'w')
fobj.write(final_data)
#os.popen("sudo sh try.sh")
#os.popen("cd bluez/bluez-5.11/ ")
#os.popen("sudo tools/hciconfig hci0 up")
#os.popen("sudo tools/hciconfig hci0 leadv 3")
#os.popen("sudo tools/hciconfig hci0 noscan")
#command = "sudo tools/hcitool -i hci0 cmd 0x08 0x0008 1E 02 01 1A 1A FF 4C 00 02 15 "+final_data
#os.popen(command>cmd.txt)
#print 'Received', repr(data)
