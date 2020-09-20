import turtle
import numpy
import bezier

def drawCurve(beg, ctrl, end, step):
    turtle.penup()
    turtle.goto(*beg)
    turtle.pendown()
    nodes = [
        [ beg[0], ctrl[0], end[0] ], 
        [ beg[1], ctrl[1], end[1] ]
    ]
    curve = bezier.Curve(nodes, degree=2)

    interval = 1.0 / step
    progress = interval

    for i in range(step):
        arr = curve.evaluate(progress)
        pt = (arr[0][0], arr[1][0])
        turtle.goto(*pt)
        progress += interval

    turtle.penup()
    for pt in (beg, ctrl, end):
        print(pt)
        turtle.goto(*pt)
        turtle.stamp()
    turtle.pendown()

def movePt(pt, mv):
    return (pt[0] + mv[0], pt[1] + mv[1])

turtle.colormode(255)
size = 100
beg = (-size,-size)
ctl = (-2*size, -size//2)
end = (0,size)
dx = 100
colors = [ (255, 0, 0), (0, 255, 0), (0, 0, 255), (255, 127, 0) ]
steps = [ 5, 10, 20, 30 ]
turtle.speed(0)

for i in range(len(steps)):
    turtle.color(colors[i])
    drawCurve(beg, ctl, end, steps[i])
    beg = movePt(beg, (dx, 0))
    ctl = movePt(ctl, (dx, 0))
    end = movePt(end, (dx, 0))

turtle.exitonclick()