import turtle as t

size = 30
count = 5

def turn(left):
	if left:
		t.left(90)
	else:
		t.right(90)

def draw(left):
	t.forward(count * size)
	turn(left)
	t.forward(size)
	turn(left)

# t.speed(0)

for o in range(2):
	for i in range(count // 2 + 1):
		for b in [ True, False ]:
			draw(b)

	t.undo()
	t.undo()
	t.left(180)

t.exitonclick()