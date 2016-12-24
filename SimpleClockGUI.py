import Tkinter
from Geometry import *

# Define
w = 400;
h = 400;

x = 0;
y = 100 * sqrt(2);
radius = y + 10;
cx = w / 2
cy = h / 2
secVec = Vec2d(x, y)
minVec = Vec2d(x, y * (4.0 / 5.0))
hourVec = Vec2d(x, y * (3.0 / 5.0))
secCounter = 0
minCounter = 0
theta = -360 / 60

def clockTask():
    global secCounter, minCounter
    canvas.delete("all")
    canvas.create_oval(cx - radius, cy - radius, cx + radius, cy + radius)
    canvas.create_line(cx, cy, cx + secVec.x, cy - secVec.y)
    canvas.create_line(cx, cy, cx + minVec.x, cy - minVec.y, width=2)
    canvas.create_line(cx, cy, cx + hourVec.x, cy - hourVec.y, width=4)
    secCounter += 1
    if secCounter >= 60:
        secCounter = 0
        minVec.rotate(theta)
        minCounter += 1
    if minCounter >= 60:
        minCounter = 0
        hourVec.rotate(theta)
    secVec.rotate(theta)
    root.after(1000, clockTask)


# Create instance
root = Tkinter.Tk()
# Set parameters
root.title("My GUI")

# Define canvas
canvas = Tkinter.Canvas(root, width=w, height=h)
canvas.pack()
root.after(1000, clockTask)
# Start the loop
root.mainloop()
