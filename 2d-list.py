# Base project format.
# Documentation https://github.com/raspberrypilearning/getting-started-with-minecraft-pi/blob/master/worksheet.md
from mcpi.minecraft import Minecraft
from mcpi import block
from time import sleep
import random

def init(ip):
    mc = Minecraft.create("192.168.7.%s" % ip, 4711)
    #mc.setting("world_immutable",True)
    #x, y, z = mc.player.getPos()        
    return mc

def matrixZ(mc,x,y,z):
            
    m = [[0,0,0,0,0,0,0,0,0,0],
         [0,0,0,1,1,1,1,0,0,0],
         [0,0,1,1,1,1,1,1,0,0],
         [0,1,1,1,0,0,1,1,1,0],
         [0,1,1,0,0,0,0,1,1,0],
         [0,1,1,0,0,0,0,1,1,0],
         [0,1,1,1,0,0,1,1,1,0],
         [0,0,1,1,1,1,1,1,0,0],
         [0,0,0,1,1,1,1,0,0,0],
         [0,0,0,0,0,0,0,0,0,0]]
        
         
    for k in range (0,10):
        for l  in range (0,10):
            #print(m[k][l],end="")
            theBlock = m[k][l]
            if (theBlock == 1):
                theBlock = 246;
            if (theBlock == 4):
                theBlock = 14;
            mc.setBlock(x,29+y-k,z+l,theBlock)
            
    m = [[0,0,0,0,0,0,0,0,0,0],
         [0,0,0,1,1,1,1,0,0,0],
         [0,0,1,1,1,1,1,1,0,0],
         [0,1,1,1,0,0,1,1,1,0],
         [0,1,1,0,0,0,0,1,1,0],
         [0,1,1,0,0,0,0,1,1,0],
         [0,1,1,1,0,0,1,1,1,0],
         [0,0,1,1,1,1,1,1,0,0],
         [0,0,0,1,1,1,1,0,0,0],
         [0,0,0,0,0,0,0,0,0,0]]
         

    for k in range (0,10):
        for l  in range (0,10):
            #print(m[k][l],end="")
            theBlock = m[k][l]
            if (theBlock == 1):
                theBlock = 246;
            if (theBlock == 4):
                theBlock = 14;
            mc.setBlock(x,19+y-k,z+l,theBlock)
            
    m = [[0,0,0,0,0,0,0,0,0,0],
         [0,0,1,1,1,1,1,1,1,0],
         [0,0,1,1,1,1,1,1,1,0],
         [0,0,1,1,0,0,0,0,0,0],
         [0,0,1,1,1,1,1,1,1,0],
         [0,0,1,1,1,1,1,1,1,0],
         [0,0,1,1,0,0,0,0,0,0],
         [0,0,1,1,0,0,0,0,0,0],
         [0,0,1,1,0,0,0,0,0,0],
         [0,0,0,0,0,0,0,0,0,0]]
            
    for k in range (0,10):
        for l  in range (0,10):
            #print(m[k][l],end="")
            theBlock = m[k][l]
            if (theBlock == 1):
                theBlock = 246;
            if (theBlock == 4):
                theBlock = 14;
            mc.setBlock(x,9+y-k,z+l,theBlock)
    
    #print()
    
#def typestuff(mc):
#    mc.postToChat("Console: Any one like minecraft?")

def matrixY(mc,x,y,z):
            
    m = [[0,0,0,0,0,0,0,0,0,0],
         [0,0,0,1,1,1,1,0,0,0],
         [0,0,1,1,1,1,1,1,0,0],
         [0,1,1,1,0,0,1,1,1,0],
         [0,1,1,0,0,0,0,1,1,0],
         [0,1,1,0,0,0,0,1,1,0],
         [0,1,1,1,0,0,1,1,1,0],
         [0,0,1,1,1,1,1,1,0,0],
         [0,0,0,1,1,1,1,0,0,0],
         [0,0,0,0,0,0,0,0,0,0]]

    for k in range (0,10):
        for l  in range (0,10):
            #print(m[k][l],end="")
            theBlock = m[k][l]
            if (theBlock == 1):
                theBlock = 246;
            if (theBlock == 4):
                theBlock = 14;
            mc.setBlock(x,y-k,9+z+l,theBlock)
            
    m = [[0,0,0,0,0,0,0,0,0,0],
         [0,0,0,1,1,1,1,0,0,0],
         [0,0,1,1,1,1,1,1,0,0],
         [0,1,1,1,0,0,1,1,1,0],
         [0,1,1,0,0,0,0,1,1,0],
         [0,1,1,0,0,0,0,1,1,0],
         [0,1,1,1,0,0,1,1,1,0],
         [0,0,1,1,1,1,1,1,0,0],
         [0,0,0,1,1,1,1,0,0,0],
         [0,0,0,0,0,0,0,0,0,0]]
         

    for k in range (0,10):
        for l  in range (0,10):
            #print(m[k][l],end="")
            theBlock = m[k][l]
            if (theBlock == 1):
                theBlock = 246;
            if (theBlock == 4):
                theBlock = 14;
            mc.setBlock(x,y-k,19+z+l,theBlock)
            
    m = [[0,0,0,0,0,0,0,0,0,0],
         [0,0,1,1,1,1,1,1,1,0],
         [0,0,1,1,1,1,1,1,1,0],
         [0,0,1,1,0,0,0,0,0,0],
         [0,0,1,1,1,1,1,1,1,0],
         [0,0,1,1,1,1,1,1,1,0],
         [0,0,1,1,0,0,0,0,0,0],
         [0,0,1,1,0,0,0,0,0,0],
         [0,0,1,1,0,0,0,0,0,0],
         [0,0,0,0,0,0,0,0,0,0]]
            
    for k in range (0,10):
        for l  in range (0,10):
            #print(m[k][l],end="")
            theBlock = m[k][l]
            if (theBlock == 1):
                theBlock = 246;
            if (theBlock == 4):
                theBlock = 14;
            mc.setBlock(x,y-k,29+z+l,theBlock)

def matrixxpreeat(mc, x, y, z, i):
    matrixZ(mc,x + i,y,z)
    sleep(0.05)
    mc.player.setPos(x,y,z)
    
def matrixypreeat(mc, x, y, z, i):
    matrixY(mc,x + i,y,z)
    sleep(0.05)
    mc.player.setPos(x,y,z)

def main():
    ipaddy = input("Please input the DESIRED ipadress ENDING (192.169.7.NUMBERHERE): ")
    mc = init(ipaddy)
    x,y,z = mc.player.getPos()
    for i in range (0, 40):
        if (i == 0 or i == 10 or i == 20 or i == 30 or i == 40):
            matrixxpreeat(mc, x, y, z, i)
    for i in range (0, 40):
        if (i == 0 or i == 10 or i == 20 or i == 30 or i == 40):
           matrixxpreeat(mc, x, y, z, i)
    for i in range (0, 40):
        if (i == 0 or i == 10 or i == 20 or i == 30 or i == 40):
            matrixxpreeat(mc, x, y, z, i)
            
            
    for i in range (0, 40):
        if (i == 0 or i == 10 or i == 20 or i == 30 or i == 40):
            matrixypreeat(mc, x, y, z, i)
    for i in range (0, 40):
        if (i == 0 or i == 10 or i == 20 or i == 30 or i == 40):
            matrixypreeat(mc, x, y, z, i)
    for i in range (0, 40):
        if (i == 0 or i == 10 or i == 20 or i == 30 or i == 40):
            matrixypreeat(mc, x, y, z, i)
    #x = x -20
    #typestuff(mc)
    #matrixY(mc,x,y,z)
    
    truefalse = False

    #mc.postToChat('Console: connected to ip - 192.168.7.%s' % str(ipaddy))
    while (truefalse != True):
        text = input("Say what you would like to say: ")
        if (text == ''):
            #mc.postToChat('Console: disconnected from ip - 192.168.7.%s' % str(ipaddy))
            truefalse = True
        else:
            mc.postToChat(text)

if __name__ == "__main__":
    main()

# multiple line comment
"""
AIR                   0
STONE                 1
GRASS                 2
DIRT                  3
COBBLESTONE           4
WOOD_PLANKS           5
SAPLING               6
BEDROCK               7
WATER_FLOWING         8
WATER                 8
WATER_STATIONARY      9
LAVA_FLOWING         10
LAVA                 10
LAVA_STATIONARY      11
SAND                 12
GRAVEL               13
GOLD_ORE             14
IRON_ORE             15
COAL_ORE             16
WOOD                 17
LEAVES               18
GLASS                20
LAPIS_LAZULI_ORE     21
LAPIS_LAZULI_BLOCK   22
SANDSTONE            24
BED                  26
COBWEB               30
GRASS_TALL           31
WOOL                 35
FLOWER_YELLOW        37
FLOWER_CYAN          38
MUSHROOM_BROWN       39
MUSHROOM_RED         40
GOLD_BLOCK           41
IRON_BLOCK           42
STONE_SLAB_DOUBLE    43
STONE_SLAB           44
BRICK_BLOCK          45
TNT                  46
BOOKSHELF            47
MOSS_STONE           48
OBSIDIAN             49
TORCH                50
FIRE                 51
STAIRS_WOOD          53
CHEST                54
DIAMOND_ORE          56
DIAMOND_BLOCK        57
CRAFTING_TABLE       58
FARMLAND             60
FURNACE_INACTIVE     61
FURNACE_ACTIVE       62
DOOR_WOOD            64
LADDER               65
STAIRS_COBBLESTONE   67
DOOR_IRON            71
REDSTONE_ORE         73
SNOW                 78
ICE                  79
SNOW_BLOCK           80
CACTUS               81
CLAY                 82
SUGAR_CANE           83
FENCE                85
GLOWSTONE_BLOCK      89
BEDROCK_INVISIBLE    95
STONE_BRICK          98
GLASS_PANE          102
MELON               103
FENCE_GATE          107
GLOWING_OBSIDIAN    246
NETHER_REACTOR_CORE 247
"""
