import turtle as t

scale = 100

def move_to(x, y):
	t.penup()
	t.goto(x, y)
	t.pendown()

def draw_kiyeok(xs = 1):
	x,y = t.pos()
	t.pendown()
	t.setheading(0)
	t.forward(scale * xs)
	t.right(100)
	t.forward(scale / 2)
	move_to(x, y)

def draw_nieun(xs = 1):
	x, y = t.pos()
	t.pendown()
	t.setheading(270)
	t.forward(scale / 2)
	t.left(90)
	t.forward(scale * xs)
	move_to(x, y)

def draw_digeut(xs = 1):
	x, y = t.pos()
	t.setheading(180)
	t.penup()
	t.backward(scale * xs)
	t.pendown()
	t.forward(scale * xs)
	t.left(90)
	t.forward(scale / 2)
	t.left(90)
	t.forward(scale * xs)
	move_to(x, y)

def draw_rieul(xs = 1):
	x, y = t.pos()
	t.pendown()
	t.setheading(0)
	t.forward(scale * xs)
	t.right(90)
	t.forward(scale / 3)
	t.right(90)
	t.forward(scale * xs)
	t.left(90)
	t.forward(scale / 3)
	t.left(90)
	t.forward(scale * xs)
	move_to(x, y)

def draw_mieum(xs = 1):
	x, y = t.pos()
	t.pendown()
	t.setheading(0)
	t.forward(scale * xs)
	t.right(90)
	t.forward(scale / 2)
	t.right(90)
	t.forward(scale * xs)
	t.right(90)
	t.forward(scale / 2)
	move_to(x, y)

def draw_bieup(xs = 1):
	x, y = t.pos()
	t.pendown()
	t.setheading(270)
	t.forward(scale * 0.6)
	t.left(90)
	t.forward(scale * xs)
	t.left(90)
	t.forward(scale * 0.6)
	t.backward(scale * 0.2)
	t.left(90)
	t.forward(scale * xs)
	move_to(x, y)

def draw_siot(xs = 1):
	x, y = t.pos()
	y2 = y - scale * 0.6
	move_to(x, y2)
	t.goto(x + scale * xs / 2, y)
	t.goto(x + scale * xs, y2)
	move_to(x, y)

def draw_ieung(xs = 1):
	x, y = t.pos()
	move_to(x + scale * xs * 0.5, y - scale * 0.8)
	t.setheading(0)
	t.circle(scale * 0.4)
	move_to(x, y)

def draw_jieut(xs = 1):
	x, y = t.pos()
	t.pendown()
	t.setheading(0)
	t.forward(scale * xs)
	y2 = y - scale * 0.6
	move_to(x, y2)
	t.goto(x + scale * xs * 0.5, y)
	t.goto(x + scale * xs, y2)
	move_to(x, y)

def draw_chieut(xs = 1):
	x, y = t.pos()
	y1 = y - scale * 0.2
	move_to(x, y1)
	t.pendown()
	t.setheading(0)
	t.forward(scale * xs)
	y2 = y - scale * 0.6
	move_to(x, y2)
	t.goto(x + scale * xs * 0.5, y1)
	t.setheading(90)
	t.forward(scale * 0.2)
	t.backward(scale * 0.2)
	t.goto(x + scale * xs, y2)
	move_to(x, y)

def draw_kieuk(xs = 1):
	x,y = t.pos()
	t.pendown()
	t.setheading(0)
	t.forward(scale * xs)
	t.right(100)
	t.forward(scale / 2)
	t.penup()
	t.backward(scale / 4)
	t.pendown()
	_, y2 = t.pos()
	t.setheading(180)
	t.goto(x, y2)
	move_to(x, y)

def draw_tieut(xs = 1):
	x, y = t.pos()
	t.setheading(180)
	t.penup()
	t.backward(scale * xs)
	t.pendown()
	t.forward(scale * xs)
	t.left(90)
	t.forward(scale * 0.6)
	t.left(90)
	t.forward(scale * xs)
	y2 = y - scale * 0.3
	move_to(x, y2)
	t.forward(scale * xs)
	move_to(x, y)

def draw_pieup(xs = 1):
	x, y = t.pos()
	x1 = x + scale * xs * 0.3
	x2 = x + scale * xs * 0.7
	y2 = y - scale * 0.6
	t.pendown()
	t.setheading(0)
	t.forward(scale * xs)
	move_to(x, y2)
	t.forward(scale * xs)
	move_to(x1, y)
	t.goto(x1, y2)
	move_to(x2, y)
	t.goto(x2, y2)
	move_to(x, y)

def draw_hieut(xs = 1):
	x, y = t.pos()
	t.penup()
	t.setheading(0)
	t.forward(scale * xs * 0.4)
	t.pendown()
	t.forward(scale * xs * 0.2)
	move_to(x + scale * xs * 0.2, y - scale * 0.1)
	t.forward(scale * xs * 0.6)
	move_to(x + scale * xs * 0.5, y - scale * 0.8)
	t.circle(scale * 0.3)
	move_to(x, y)

def draw_double(cons1, cons2):
	x, y = t.pos()
	cons1(0.5)
	t.setheading(0)
	t.penup()
	t.forward(scale * 0.6)
	cons2(0.5)
	move_to(x, y)

def draw_dbl_kiyeok():
	draw_double(draw_kiyeok, draw_kiyeok)

def draw_dbl_digeut():
	draw_double(draw_digeut, draw_digeut)

def draw_dbl_bieup():
	draw_double(draw_bieup, draw_bieup)

def draw_dbl_siot():
	draw_double(draw_siot, draw_siot)

def draw_dbl_jieut():
	draw_double(draw_jieut, draw_jieut)

def draw_kiyeok_siot():
	draw_double(draw_kiyeok, draw_siot)

def draw_nieun_jieut():
	draw_double(draw_nieun, draw_jieut)

def draw_nieun_hieot():
	draw_double(draw_nieun, draw_hieut)

def draw_rieul_kiyeok():
	draw_double(draw_rieul, draw_kiyeok)

def draw_rieul_mieum():
	draw_double(draw_rieul, draw_mieum)

def draw_rieul_bieup():
	draw_double(draw_rieul, draw_bieup)

def draw_rieul_siot():
	draw_double(draw_rieul, draw_siot)

def draw_rieul_tieut():
	draw_double(draw_rieul, draw_tieut)

def draw_rieul_pieup():
	draw_double(draw_rieul, draw_pieup)

def draw_rieul_hieut():
	draw_double(draw_rieul, draw_hieut)

def draw_bieup_siot():
	draw_double(draw_bieup, draw_siot)

def draw_a():
	x, y = t.pos()
	x2 = x + scale * 1.5
	move_to(x2, y)
	t.goto(x2, y - scale)
	t.setheading(0)
	move_to(x2, y - scale * 0.5)
	t.forward(scale * 0.2)
	move_to(x, y)

def draw_ya():
	x, y = t.pos()
	x2 = x + scale * 1.5
	move_to(x2, y)
	t.goto(x2, y - scale)
	t.setheading(0)
	move_to(x2, y - scale * 0.4)
	t.forward(scale * 0.2)
	move_to(x2, y - scale * 0.6)
	t.forward(scale * 0.2)
	move_to(x, y)

def draw_eo():
	x, y = t.pos()
	x2 = x + scale * 1.5
	move_to(x2, y)
	t.goto(x2, y - scale)
	t.setheading(180)
	move_to(x2, y - scale * 0.5)
	t.forward(scale * 0.2)
	move_to(x, y)

def draw_yeo():
	x, y = t.pos()
	x2 = x + scale * 1.5
	move_to(x2, y)
	t.goto(x2, y - scale)
	t.setheading(180)
	move_to(x2, y - scale * 0.4)
	t.forward(scale * 0.2)
	move_to(x2, y - scale * 0.6)
	t.forward(scale * 0.2)
	move_to(x, y)

def draw_o():
	x, y = t.pos()
	y2 = y - scale * 1.15
	move_to(x, y2)
	t.setheading(0)
	t.forward(scale)
	t.backward(scale * 0.5)
	t.left(90)
	t.forward(scale * 0.2)
	move_to(x, y)

def draw_yo():
	x, y = t.pos()
	y2 = y - scale * 1.15
	move_to(x, y2)
	t.setheading(0)
	t.forward(scale)
	t.backward(scale * 0.6)
	t.left(90)
	t.forward(scale * 0.2)
	move_to(x + scale * 0.6, y2)
	t.forward(scale * 0.2)
	move_to(x, y)

def draw_u():
	x, y = t.pos()
	y2 = y - scale * 1.15
	move_to(x, y2)
	t.setheading(0)
	t.forward(scale)
	t.backward(scale * 0.5)
	t.right(90)
	t.forward(scale * 0.2)
	move_to(x, y)

def draw_yu():
	x, y = t.pos()
	y2 = y - scale * 1.15
	move_to(x, y2)
	t.setheading(0)
	t.forward(scale)
	t.backward(scale * 0.6)
	t.right(90)
	t.forward(scale * 0.2)
	move_to(x + scale * 0.6, y2)
	t.forward(scale * 0.2)
	move_to(x, y)

def draw_eu():
	x, y = t.pos()
	y2 = y - scale * 1.25
	move_to(x, y2)
	t.setheading(0)
	t.forward(scale)
	move_to(x, y)

def draw_i():
	x, y = t.pos()
	x2 = x + scale * 1.5
	move_to(x2, y)
	t.goto(x2, y - scale)
	move_to(x, y)

def draw_ae():
	draw_a()
	t.setheading(0)
	t.penup()
	t.forward(scale * 0.2)
	draw_i()

def draw_yae():
	draw_ya()
	t.setheading(0)
	t.penup()
	t.forward(scale * 0.2)
	draw_i()

def draw_e():
	draw_eo()
	t.setheading(0)
	t.penup()
	t.forward(scale * 0.1)
	draw_i()

def draw_ye():
	draw_yeo()
	t.setheading(0)
	t.penup()
	t.forward(scale * 0.1)
	draw_i()

def draw_wa():
	draw_o()
	draw_a()

def draw_wae():
	draw_o()
	draw_ae()

def draw_oi():
	draw_o()
	draw_i()

def draw_weo():
	draw_u()
	draw_eo()

def draw_we():
	draw_u()
	draw_e()

def draw_wi():
	draw_u()
	draw_i()

def draw_eui():
	draw_eu()
	draw_i()

def draw_final(func = None):
	x, y = t.pos()
	if func != None:
		move_to(x, y - scale * 1.5)
		func()
	move_to(x + scale * 2, y)

chosung = [
	draw_kiyeok, draw_dbl_kiyeok, draw_nieun, draw_digeut, 
	draw_dbl_digeut, draw_rieul, draw_mieum, draw_bieup,
	draw_dbl_bieup, draw_siot, draw_dbl_siot, draw_ieung,
	draw_jieut, draw_dbl_jieut, draw_chieut, draw_kieuk,
	draw_tieut, draw_pieup, draw_hieut
]

joongsung = [
	draw_a, draw_ae, draw_ya, draw_yae,
	draw_eo, draw_e, draw_yeo, draw_ye,
	draw_o, draw_wa, draw_wae, draw_oi,
	draw_yo, draw_u, draw_weo, draw_we,
	draw_wi, draw_yu, draw_eu, draw_eui,
	draw_i
]

jongsung = [
	None, draw_kiyeok, draw_dbl_kiyeok, draw_kiyeok_siot,
	draw_nieun, draw_nieun_jieut, draw_nieun_hieot,
	draw_digeut, draw_rieul, 
	draw_rieul_kiyeok, draw_rieul_mieum, draw_rieul_bieup, draw_rieul_siot, 
	draw_rieul_tieut, draw_rieul_pieup, draw_rieul_hieut,
	draw_mieum, draw_bieup, draw_bieup_siot, 
	draw_siot, draw_dbl_siot, draw_ieung, draw_jieut, draw_chieut, 
	draw_kieuk, draw_tieut, draw_pieup, draw_hieut
]

def draw_ustr(str):
	ox,oy = t.pos()
	for ch in str:
		char = ord(ch)
		if char >= 0xAC00 and char <= 0xDCAF:
			order = char - 0xAC00
			cho = order // (21 * 28)
			joong = order % (21 * 28) // 28
			jong = order % 28
			chosung[cho]()
			joongsung[joong]()
			draw_final(jongsung[jong])
		elif char == 0x0A:
			oy -= 3 * scale
			move_to(ox, oy)
		else:
			x,y = t.pos()
			move_to(x + scale, y)