import turtle as t
import random

ANGLE = 20
MIN_LENGTH = 5
REDUCE_RATE = 0.7
WIDTH_RATE = 0.1
RANDOM_RATE_MIN = 0.9
RANDOM_RATE_MAX = 1.1
COLOR_LEAF  = (0.7, 0.5, 0.0)
COLOR_SPRIG = (0.4, 0.3, 0.1)
COLOR_BRANCH = (0.3, 0.1, 0.1)

def random_value(value):
	return value * random.uniform(RANDOM_RATE_MIN, RANDOM_RATE_MAX)

def color_near(color):
	r, g, b = color
	return (
		random_value(r),
		random_value(g),
		random_value(b)
	)

def tree(length):
	len = random_value(length)
	w = len * WIDTH_RATE
	if w < 1:
		t.color(color_near(COLOR_LEAF))
	elif w < 2:
		t.color(color_near(COLOR_SPRIG))
	else:
		t.color(color_near(COLOR_BRANCH))
	# print(w, t.pencolor())
	t.width(w)
	t.pendown()
	t.forward(len)
	if len > MIN_LENGTH:
		angle_left = random_value(ANGLE)
		angle_right = random_value(ANGLE)
		sub = len * REDUCE_RATE
		t.left(angle_left)
		tree(sub)
		t.right(angle_left + angle_right)
		tree(sub)
		t.left(angle_right)
	t.penup()
	t.backward(len)


t.speed(0)
t.penup()
t.goto(0, -200)
t.pendown()
t.setheading(90)

tree(120)

t.exitonclick()
