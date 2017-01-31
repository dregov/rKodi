import xbmc
import os

def logoff():
	xbmc.executebuiltin("System.Logoff()")
	
def sleep():
	os.system("su -c 'echo 0 > /sys/devices/virtual/display/display0.HDMI/enable'")
	os.system("su -c 'read'")
	os.system("su -c 'echo 1 > /sys/devices/virtual/display/display0.HDMI/enable'")
	
def shutdown():
	os.system("su -c 'echo 0 > /sys/devices/virtual/display/display0.HDMI/enable'")

def reboot():
	os.system("su -c 'reboot'")

if sys.argv[1] == 'shutdown':
	shutdown()
elif sys.argv[1] == 'sleep':
	sleep()
elif sys.argv[1] == 'reboot':
	reboot()

