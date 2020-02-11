from mcpi.minecraft import Minecraft
from mcpi import block
from time import sleep
import random

def init(ip):
    mc = Minecraft.create("192.168.7.%s" % ip, 4711)
    #mc.setting("world_immutable",True)
    #x, y, z = mc.player.getPos()        
    return mc
    
def main():
	truefalse = False
	ipaddy = input("Please input the DESIRED ipadress ENDING (192.169.7.NUMBERHERE): ")
	mc = init(ipaddy)

	mc.postToChat('Console: connected to ip - 192.168.7.%s' % str(ipaddy))
	while (truefalse != True):
		text = input("Say what you would like to say: ")
		if (text == ''):
			mc.postToChat('Console: disconnected from ip - 192.168.7.%s' % str(ipaddy))
			truefalse = True
		else:
			mc.postToChat(text)


if __name__ == "__main__":
    main()
