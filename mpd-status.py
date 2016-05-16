#!/usr/bin/python
from time import sleep
import os
import sys
import signal
import time


def signal_handler(sig, frame):
	print('You pressed Ctrl+C!!!!')
	datei.close()
	sys.exit(0)
	
signal.signal(signal.SIGINT, signal_handler)
ncards = 5
power = 0
smps = 0
lstactive = [0,0,0,0,0]

lstmatrix = ['07','16','08','05','06']

while 1:
	time.sleep(2)
	sys.stdout.flush()
	for i in range(ncards):
		power = 0
		card = open('/proc/asound/card' + str(i) + '/stream0', "r")
		if card.read().find("Running") <> -1:
			lstactive[i] = 5
			power = 1
			datei = open('/media/ramdisk/' + lstmatrix[i], "w")
			datei.close()
		else:
			if lstactive[i]:
				lstactive[i] = lstactive[i] - 1
			else:
				if os.path.isfile('/media/ramdisk/' + lstmatrix[i]):
					os.remove('/media/ramdisk/' + lstmatrix[i])
				
		card.close()
	
	if power:
		smps = 10
		datei = open("/media/ramdisk/01", "w")
		datei.close()
	else:
		if smps:
			smps = smps - 1
		else:
			if os.path.isfile("/media/ramdisk/01"):
				os.remove("/media/ramdisk/01")
			