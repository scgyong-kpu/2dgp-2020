import turtle
import random

MAX_LEVEL = 7

def adjustColorValue(v):
	v = int(v * random.uniform(0.8, 1.2))
	if v > 255: v = 255
	return v

def setColor(level):
	if level <= 2:
		(r, g, b) = (80, 255 - level * 30, 80)
	else:
		bright = level - 2
		(r, g, b) = (180 - 20 * level, 120 - 10 * level, 80 - 8 * level)

	r = adjustColorValue(r)
	g = adjustColorValue(g)
	b = adjustColorValue(b)

	turtle.color((r, g, b))

def leaf():
	size = random.uniform(10, 15)
	turtle.width(1)
	turtle.right(45)
	turtle.begin_fill()
	turtle.circle(size, 90)
	turtle.left(90)
	turtle.circle(size, 90)
	turtle.end_fill()
	turtle.left(135)

def tree(level, leavesOnly = False):
	length = level * random.uniform(17, 23)
	setColor(level)
	if level == 1:
		leaf()
		# turtle.left(180)
		# turtle.stamp()
		# turtle.right(180)
	elif not leavesOnly:
		turtle.width(level * 3 - 2)
		turtle.pendown()
		turtle.forward(length)
	if (level > 1):
		branchCount = random.randint(2, 3)
		step = 60 / branchCount
		angle = random.uniform(-25, -15)
		turtle.right(angle)
		for _ in range(branchCount):
			tree(level - 1)
			a = (40.0 / (branchCount - 1)) * random.uniform(0.9, 1.1)
			turtle.right(a)
			angle += a
		turtle.left(angle)
	if level != 1 and not leavesOnly:
		turtle.penup()
		turtle.backward(length)
	if level in range(3, 7) and random.random() < 0.3:
		tree(2, True)

turtle.speed(0)
turtle.penup()
turtle.left(90)
turtle.backward(300)
turtle.pendown()
turtle.colormode(255)

tree(MAX_LEVEL)

turtle.exitonclick()
