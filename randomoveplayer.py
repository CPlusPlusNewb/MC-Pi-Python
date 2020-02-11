from mcpi.minecraft import Minecraft
from mcpi import block
from time import sleep
import random
from picraft import World

def init(ip):
	mc = Minecraft.create("192.168.7.%s" % ip, 4711)
	#mc.setting("world_immutable", False)
	#mc.player.setting('autojump', False)
	#x, y, z = mc.player.getPos()        
	return mc
    
def randommove_player(mc, x, y, z, ip):
	w = World("192.168.7.%s" % ip, 4711)
	#rotation = mc.player.getRotation()
	mc.postToChat("You are going to be moved in:")
	mc.postToChat("5")
	sleep(1)
	mc.postToChat("4")
	sleep(1)
	mc.postToChat("3")
	sleep(1)
	mc.postToChat("2")
	sleep(1)
	mc.postToChat("1")
	sleep(1)
	for i in range (0,10):
		newx = x + (random.randint(1, 20))
		newy = y + (random.randint(1, 20))
		newz = z + (random.randint(1, 20))
		mc.player.setPos(newx, newy, newz)
		mc.postToChat("x = %s, y = %s, z = %s" % (str(newx), str(newy), str(newz)))
		#mc.camera.setNormal(random.randint(0, 2))
		w.camera.third_person(w.player)
		sleep(0.5)
		
	w.camera.first_person(w.player)

def main():	
	ipaddy = input("Please input the DESIRED ipadress ENDING (192.169.7.NUMBERHERE): ")
	mc = init(ipaddy)
	x,y,z = mc.player.getPos()
	mc.player.setPos(x,y,z)
    #x = x -20
    
    #boomerstatus(mc)
    #typestuff(mc)
	randommove_player(mc, x, y, z, ipaddy)

    
    #mc.postToChat("Boomer -->")
    #matrixY(mc,x,y,z)

if __name__ == "__main__":
	main()
