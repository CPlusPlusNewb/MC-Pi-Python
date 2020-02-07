from mcpi.minecraft import Minecraft
from mcpi import block
from time import sleep
import random

def init():
    mc = Minecraft.create("192.168.7.226", 4711)
    mc.setting("world_immutable",True)
    #x, y, z = mc.player.getPos()        
    return mc

def boomerstatus(mc):
    for i in range (0,1000):
        mc.postToChat("Do you know da wae?")
        sleep(0.1)

def typestuff(mc):
	for i in range (0,20):
		switcher = {
			1:  "Crimson",
			2:  "Logan!!",
			3:  "lblblb!",
			4:  "Bluebur",
			5:  "BenJet1",
			6:  "NoahMcGe",
			7:  "hehexd!",
			8:  "TiToniC",
			9:  "kriptic",
			10: "icebowl",
			11: "whithat",
			12: "redhat!"
		}
		#print ("joined the game")
		mc.postToChat("%s joined the game" % str(switcher.get(random.randint(1, 12))))
		sleep(0.2)

def main():
    mc = init()
    x,y,z = mc.player.getPos()
    mc.player.setPos(x,y,z)
    #x = x -20
    boomerstatus(mc)
    #typestuff(mc)
    #mc.postToChat("Boomer -->")
    #matrixY(mc,x,y,z)

if __name__ == "__main__":
    main()
