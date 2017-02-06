import xbmc
import os

def logoff():
	xbmc.executebuiltin("System.Logoff()")
	
def sleep():
	xbmc.executebuiltin("XBMC.ReloadSkin()")
	xbmc.executebuiltin("XBMC.Quit()")
	os.system("sleep 2")
	os.system("su -c 'echo 0 > /sys/class/display/display0.HDMI/enable'")
	os.system("sleep 5")
	os.system("su -c 'echo 1 > /sys/class/display/display0.HDMI/enable'")
	
def shutdown():
	xbmc.executebuiltin("XBMC.ReloadSkin()")
	xbmc.executebuiltin("XBMC.Quit()")
	os.system("sleep 2")
	os.system("su -c 'echo 0 > /sys/devices/virtual/display/display0.HDMI/enable'")
	os.system("sleep -1")
	
def reboot():
	xbmc.executebuiltin("XBMC.ReloadSkin()")
	xbmc.executebuiltin("XBMC.Quit()")
	os.system("sleep 2")
	os.system("su -c 'reboot'")

if sys.argv[1] == 'shutdown':
	shutdown()
elif sys.argv[1] == 'sleep':
	sleep()
elif sys.argv[1] == 'reboot':
	reboot()

