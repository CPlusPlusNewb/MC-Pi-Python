import os

def main():
	os.system("sudo ifconfig wlan0 192.168.7.220 netmask 255.255.255.0")
	os.system("sudo dhclient wlan0")
	
main()
