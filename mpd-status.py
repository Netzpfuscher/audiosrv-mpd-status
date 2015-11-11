#!/usr/bin/python
import mpd
from time import sleep
import os
import sys
import signal
import time


def signal_handler(sig, frame):
	print('You pressed Ctrl+C!!!!')
	sys.exit(0)
	
signal.signal(signal.SIGINT, signal_handler)

client = mpd.MPDClient()
client.timeout = 10
client.connect('localhost','6600')
counter1 =0
counter2 =0
counter3 =0
counter4 =0
while 1:
	time.sleep(2)
	sys.stdout.flush()
	status = client.outputs()
	play = client.status()
	if (status[0].get('outputenabled') == "1" and play.get('state') == "play") or os.path.isfile("/media/ramdisk/stereo1"):
		datei = open("/media/ramdisk/05", "w")
		datei.close()
		counter1 = 10
	else:
		if counter1:
			counter1 = counter1 - 1
	if (status[1].get('outputenabled') == "1" and play.get('state') == "play") or os.path.isfile("/media/ramdisk/stereo2"):
		datei = open("/media/ramdisk/06", "w")
		datei.close()
		counter2 = 10
	else:
		if counter2:
			counter2 = counter2 - 1
	if (status[2].get('outputenabled') == "1" and play.get('state') == "play") or os.path.isfile("/media/ramdisk/stereo3"):
		datei = open("/media/ramdisk/07", "w")
		datei.close()
		counter3 = 10
	else:
		if counter3:
			counter3 = counter3 - 1
	if (status[3].get('outputenabled') == "1" and play.get('state') == "play") or os.path.isfile("/media/ramdisk/stereo4"):
		datei = open("/media/ramdisk/08", "w")
		datei.close()
		counter4 = 10
	else:
		if counter4:
			counter4 = counter4 - 1
	if counter1 == 0:
		if os.path.isfile("/media/ramdisk/05"):
			os.remove("/media/ramdisk/05")
	if counter2 == 0:
		if os.path.isfile("/media/ramdisk/06"):
			os.remove("/media/ramdisk/06")
	if counter3 == 0:
		if os.path.isfile("/media/ramdisk/07"):
			os.remove("/media/ramdisk/07")
	if counter4 == 0:
		if os.path.isfile("/media/ramdisk/08"):
			os.remove("/media/ramdisk/08")
	if (counter1 == 0 and counter2 == 0 and counter3 == 0 and counter4 == 0):
		if os.path.isfile("/media/ramdisk/01"):
			os.remove("/media/ramdisk/01")	
	else:
		datei = open("/media/ramdisk/01", "w")
		datei.close()	



client.disconnect
    
