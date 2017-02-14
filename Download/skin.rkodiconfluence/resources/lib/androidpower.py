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
	os.system("su -c 'reboot recovery'")
	os.system("sleep -1")

def bootloader():
	xbmc.executebuiltin("XBMC.ReloadSkin()")
	xbmc.executebuiltin("XBMC.Quit()")
	os.system("sleep 2")
	os.system("su -c 'reboot bootloader'")
	os.system("sleep -1")
	
def reboot():
	xbmc.executebuiltin("XBMC.ReloadSkin()")
	xbmc.executebuiltin("XBMC.Quit()")
	os.system("sleep 3")
	os.system("su -c 'reboot'")
	os.system("sleep -1")

if sys.argv[1] == 'shutdown':
	shutdown()
elif sys.argv[1] == 'sleep':
	sleep()
elif sys.argv[1] == 'reboot':
	reboot()
elif sys.argv[1] == 'bootloader':
	bootloader()
