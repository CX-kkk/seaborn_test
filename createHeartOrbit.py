#### Create a heart orbit ####
import math
import maya.cmds as cmds



def linspace(a, b, n=100):
    if n < 2:
        return b
    diff = (float(b) - a)/(n - 1)
    return[diff * i + a for i in range(n)]    
    
    
def createHeartOrbit(pointNum):
    t = linspace(-math.pi, math.pi, pointNum)
   
    # Move knok to right position
    for count,i in enumerate(t):
        x = 16 * math.sin(i) * math.sin(i) * math.sin(i)
        y = 0
        z = 13 * math.cos(i) - 5 * math.cos(2*i) - 2 * math.cos(3*i) - math.cos(4*i)
        obj = cmds.polySphere(r=1,sx=20,sy=20,ax=(0,1,0),cuv=2,ch=1)
        cmds.xform(obj,r=False,t=(x,y,z))

        


if __name__=='__main__':
    createHeartOrbit(100)