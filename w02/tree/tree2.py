import turtle as t
import random

ANGLE = 20
MIN_LENGTH = 5
REDUCE_RATE = 0.7
WIDTH_RATE = 0.1
RANDOM_RATE_MIN = 0.9
RANDOM_RATE_MAX = 1.1

def tree(length):
	rate = random.uniform(RANDOM_RATE_MIN, RANDOM_RATE_MAX)
	len = length * rate
	t.width(len * WIDTH_RATE)
	t.forward(len)
	if len > MIN_LENGTH:
		sub = len * REDUCE_RATE
		t.left(ANGLE)
		tree(sub)
		t.right(2 * ANGLE)
		tree(sub)
		t.left(ANGLE)
	t.backward(len)


t.speed(0)
t.penup()
t.goto(0, -200)
t.pendown()
t.setheading(90)

tree(120)

t.exitonclick()
