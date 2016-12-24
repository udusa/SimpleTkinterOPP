"""
http://zetcode.com/gui/tkinter/drawing/
"""

import Tkinter as tk
from Geometry import Vec2d
from math import *

class MyClock(tk.Tk):

    theta = 360/60

    def __init__(self,w,h):
        tk.Tk.__init__(self)
        self.cx = w/2
        self.cy = h/2
        self.initGUI()
        self.initLogic()
        self.startLoop()

    def initGUI(self):
        geometry = str(self.cx*2)+"x"+str(self.cy*2)
        self.geometry(geometry)
        canvas = tk.Canvas(self)
        canvas.pack()
        self.canvas = canvas

    def initLogic(self):
        #center
        self.cVec = Vec2d(self.cx, self.cy)
        norm = min(self.cx,self.cy)-10
        self.radius = norm
        #time
        self.sVec = Vec2d(0,-norm)
        #counter
        self.sCounter = 0

    def clockLoop(self):
        self.canvas.delete("all")
        self.drawCircle()
        sVec = self.sVec.getInstance()
        sVec.plus(self.cVec)
        self.drawVector(sVec)
        self.sVec.rotate(MyClock.theta)
        self.after(1000,self.clockLoop)

    def drawCircle(self):
        self.canvas.create_oval(self.cx-self.radius,self.cy-self.radius,self.cx+self.radius,self.cy+self.radius)

    def drawVector(self,vec):
        self.canvas.create_line(self.cx,self.cy,vec.x,vec.y);

    def startLoop(self):
        self.after(1000, self.clockLoop)
        self.mainloop()


app = MyClock(200,200)

