from mcpi.minecraft import Minecraft
from mcpi import block
from time import sleep
import random

def init(ip):
    mc = Minecraft.create("192.168.7.%s" % ip, 4711)
    #mc.setting("world_immutable", False)
    #x, y, z = mc.player.getPos()        
    return mc

def boomerstatus(mc):
    for i in range (0,1000):
        mc.postToChat("Do you know da wae?")
        sleep(0.5)

def typestuff(mc):
	for i in range (0,20):
		switcher = {
			1:  "Crimson",
			2:  "Logan!!",
			3:  "lblblb!",
			4:  "Bluebur",
			5:  "BenJet1",
			6:  "NoahMcG",
			7:  "hehexd!",
			8:  "TiToniC",
			9:  "kriptic",
			10: "icebowl",
			11: "whithat",
			12: "redhat!",
			13: "DamBruh"
		}
		#print ("joined the game")
		mc.postToChat("%s joined the game" % str(switcher.get(random.randint(1, 13))))
		sleep(0.2)

def main():
    ipaddy = input("Please input the DESIRED ipadress ENDING (192.169.7.NUMBERHERE): ")
    mc = init(ipaddy)
    x,y,z = mc.player.getPos()
    mc.player.setPos(x,y,z)
    #x = x -20
    
    #boomerstatus(mc)
    typestuff(mc)
    #randommove_player(mc, x, y, z)
    
    #mc.postToChat("Boomer -->")
    #matrixY(mc,x,y,z)

if __name__ == "__main__":
    main()
