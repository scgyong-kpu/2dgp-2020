import turtle
import korean

korean.scale = 20
turtle.speed(0)

korean.move_to(-300, 200)

str = '가각안녕하세요\n이것은한글입니다\n김기용만세\n게임프로그래밍\n'
str += '똜깕휎갃떥볞쒊둛걡꽖훯쏐킁코상'
korean.draw_ustr(str)

korean.draw_ustr('김기용')

# korean.draw_dbl_bieup()
# # korean.draw_hieut()
# korean.draw_we()
# korean.draw_final()

# # korean.draw_kiyeok()
# korean.draw_dbl_bieup()
# korean.draw_eui()
# korean.draw_final(korean.draw_dbl_bieup)

# korean.draw_kiyeok()
# korean.draw_ih()
# korean.draw_final()

# korean.draw_ieung()
# korean.draw_yo()
# korean.draw_final(korean.draw_ieung)

turtle.exitonclick()