import turtle as t

t.speed(0)

size = 10
count = 15
linelength = count * size

t.penup()
t.goto(-300, 200)
t.pendown()

def line(start, end):
	t.penup()
	t.goto(*start)
	t.pendown()
	t.goto(*end)

x1, y1 = t.pos()
x2, y2 = x1 + linelength, y1 + linelength

for i in range(count + 1):
	n = i * size
	line((x1, y1 + n), (x2, y1 + n))
	line((x1 + n, y1), (x1 + n, y2))

t.exitonclick()