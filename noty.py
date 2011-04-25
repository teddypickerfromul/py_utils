#!/usr/bin/python

import os
import subprocess


stat = os.statvfs("/")
amount = (((stat.f_bsize * stat.f_bavail)/1024)/1024)
#if(amount < 600):
msg = "Where are only "+str(amount)+" Mb"
subprocess.call(['notify-send',"Ahtung!!!",msg,"-i"," notification-message-warning","-t","-3000"])
	#if(amount < 100):
		#head = "Oh SHI~"  
		#subprocess.call(['notify-send',head,msg, "-t","-3000"])
		


