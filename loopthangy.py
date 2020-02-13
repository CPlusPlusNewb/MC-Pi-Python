

from mcpi.minecraft import Minecraft
from mcpi import block
from time import sleep
import random

def init(ip):
	mc = Minecraft.create(ip, 4711)
	#mc.setting("world_immutable", False)
	#x, y, z = mc.player.getPos()        
	return mc
    
def LOOPALLIPSANDSAYSTUFF(MC):
	mc.postToChat("Hello all!")

def main(ipaddy):	
	#for i in range (1, 19):
		#istr = ""
		#if (i < 10):
		#	istr = "0" + str(i)
		#else:
		#	istr = str(i)
		#print(istr)
		mc = init(ipaddy)
		x,y,z = mc.player.getPos()
		mc.player.setPos(x,y,z)
		LOOPALLIPSANDSAYSTUFF(mc)
	#mc.camera.setFollow()
	#mc.camera.setNormal(1)
    
    #mc.postToChat("Boomer -->")
    #matrixY(mc,x,y,z)

if __name__ == "__main__":
	main()
