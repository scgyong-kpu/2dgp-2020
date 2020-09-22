import turtle
import jamo

# def move_to(x, y):
# 	t.penup()
# 	t.goto(x, y)
# 	t.pendown()

jamo.move_to(-300, 200)

jamo.draw_kiyeok()
# jamo.draw_dbl_bieup()
jamo.draw_i()
# jamo.draw_final(jamo.draw_kiyeok)
jamo.draw_final(jamo.draw_mieum)

jamo.draw_kiyeok()
jamo.draw_i()
jamo.draw_final()

jamo.draw_ieung()
jamo.draw_yo()
jamo.draw_final(jamo.draw_ieung)

turtle.exitonclick()