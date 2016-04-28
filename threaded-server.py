
from socket import *
from datetime import datetime
import thread
import subprocess
import os
import zlib

beacon = {}
b_data = {}

BUFF = 1024
HOST = ''# must be input parameter @TODO
PORT = 1025 # must be input parameter @TODO

#command = """curl https://www.googleapis.com/urlshortener/v1/url?key=AIzaSyBvMF4EHOR0i03n-ayNjKpw2k-9kXLIQ-I   -H 'Content-Type: application/json'   -d '{"longUrl": "http:/{0}"}"""

l = []
beacon_name = []
file="data.txt"
with open(file) as f:
	content = f.readlines()
print len(content)
for i in range(len(content)):
	n=str(content[i]).split(':')
	b_data[n[0]]=n[1].split('\n')[0]
	print n[0]
	print n[1]
#print len(content)
#print content
print b_data
#print n

def response(key):
    print str(b_data[key])
    return str(b_data[key])
    #return 'this_is_the_return_from_the_s'

def handler(clientsock,addr):
    #while 1:
        data = clientsock.recv(BUFF)
        print 'data:' + repr(data)
	#print addr
	print "display"
	if data not in beacon_name:
		beacon_name.append(data)
		b_data.setdefault(data,[])
		beacon.setdefault(data,[])
		beacon[data].append(addr)
		#print beacon
		now = datetime.now()
		beacon[data].append(str(now.hour)+':'+str(now.minute)+':'+str(now.second))
		#del beacon[" "]
	else:
		del beacon[data]
		beacon.setdefault(data, []).append(addr)
		#beacon[data]=(addr)
		now = datetime.now()
		beacon.setdefault(data, []).append(str(now.hour)+":"+str(now.minute)+':'+str(now.second))
	print beacon_name
	print beacon
	t=response(data)
	result = os.popen(""" curl https://www.googleapis.com/urlshortener/v1/url?key=AIzaSyBvMF4EHOR0i03n-ayNjKpw2k-9kXLIQ-I   -H 'Content-Type: application/json'   -d '{"longUrl": "http://"""+t+""""}' > out.txt""").read()
	#(out, err) = proc.communicate()
	print result
	stripped = os.popen("sh split.sh").read()
	#print stripped
	#print stripped.encode("hex")
	clientsock.send(stripped.encode("hex")+"000000000000c800")
	#print 'sent:' + repr(response(''))
        clientsock.close() # - reports [Errno 9] Bad file descriptor as it looks like that socket is trying to send data when it is already closed

if __name__=='__main__':
    ADDR = (HOST, PORT)
    serversock = socket(AF_INET, SOCK_STREAM)
    serversock.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)
    serversock.bind(ADDR)
    i=1
    while 1:
    	serversock.listen(5)
    	while 1:
		with open(file) as f:
        		content = f.readlines()
		print len(content)
		for i in range(len(content)):
        		n=str(content[i]).split(':')
        		b_data[n[0]]=n[1].split('\n')[0]
        		print n[0]
        		print n[1]
		#print len(content)
		#print content
		print b_data
		#print n
		#print (i+1)
        	print 'waiting for connection...'
        	clientsock, addr = serversock.accept()
        	print '...connected from:', addr
		fobj = open("log.txt",'w')
		l.append(addr)
		fobj.write(str(l))
		fobj.close()
        	thread.start_new_thread(handler, (clientsock, addr))
