from math import *
import numpy as np

class Vec2d(object):

    num_of_vecs = 0

    def __init__(self,_x,_y):
        self.x = _x
        self.y = _y
        Vec2d.num_of_vecs += 1

    @classmethod
    def from_string(cls,string,delimer):
        x,y = string.split(delimer)
        return cls(x,y)

    def dot(self,vec2d):
        return sqrt(self.x*self.x+self.y*self.y)

    def rotate(self,thetaDeg):
        theta = radians(thetaDeg)
        #np.array
        rotMat = np.matrix\
            ([[cos(theta),-sin(theta)]
             ,[sin(theta),cos(theta)]])
        myvec = np.array([self.x,self.y])
        rotvec = rotMat.dot(myvec);
        self.x = rotvec.item(0)
        self.y = rotvec.item(1)

    def plus(self,vec):
        self.x += vec.x
        self.y += vec.y

    def getInstance(self):
        return Vec2d(self.x,self.y)

    def __str__(self):
        return "Vec2d{ "+str(self.x)\
               +" , "+str(self.y)+" }"


class Vec3d(Vec2d):
    def __init__(self,x,y,z):
        super(Vec3d,self).__init__(x,y)
        self.z = z;

    def __str__(self):
        return "Vec2d{ "+str(self.x)\
               +" , "+str(self.y)+" , "+str(self.z)+" }"

    def rotateXY(self,theta):
        self.rotate(theta)

v = Vec3d(0,1,5)
print(v)
v.rotateXY(theta=-90)
print(v)
#v = Vec2d(0,1)
#for i in range(60):
#    v.rotate(-360/60)
#    print v
#Vec2d.rotate(v,45)
#print v
#v2 = Vec2d.from_string("5,6",",")
#print v2
