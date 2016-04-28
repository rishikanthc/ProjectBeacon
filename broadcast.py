from pushbullet import Pushbullet
import requests
import sys
import time
import subprocess
from netifaces import interfaces, ifaddresses, AF_INET
import socket

ip = subprocess.check_output("/sbin/ifconfig eth0 | grep 'inet addr:' | cut -d: -f2 | awk '{ print $1}'", shell=True)

time.sleep(10)

def getip():
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        s.connect(('gmail.com',0))
        return s.getsockname()[0]

def push(msg):

	api_key="kO3wYXQB6WQlQp7A5AN7WcPqdMOWy1Xx"
	pb = Pushbullet(api_key)
#	ip = subprocess.check_output("/sbin/ifconfig eth0 | grep 'inet addr:' | cut -d: -f2 | awk '{ print $1}'", shell=True)
	devlist=[x.nickname.encode('UTF-8') for x in pb.devices]
	if 'Rpi' not in devlist:
		pb.new_device('Rpi')
	for dev in pb.devices:
			push = dev.push_note('Rpi is up! ',msg)

push(getip())
#push(sys.argv[1])
