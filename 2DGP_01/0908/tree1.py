import turtle as t

ANGLE = 20
MIN_LENGTH = 5
REDUCE_RATE = 0.7
WIDTH_RATE = 0.1

def tree(length):
	t.width(length * WIDTH_RATE)
	t.forward(length)
	if length > MIN_LENGTH:
		sub = length * REDUCE_RATE
		t.left(ANGLE)
		tree(sub)
		t.right(2 * ANGLE)
		tree(sub)
		t.left(ANGLE)
	t.backward(length)


t.speed(0)
t.penup()
t.goto(0, -200)
t.pendown()
t.setheading(90)

tree(120)

t.exitonclick()
