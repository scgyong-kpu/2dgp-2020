import turtle

turtle.speed(0)
amount = 10
for i in range(200):
	turtle.forward(amount)
	turtle.left(91)
	amount += 2

turtle.exitonclick()
