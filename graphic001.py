import turtle as t
t.shape('turtle')
t.circle(120)
n=60
t.speed('fastest')

for i in range(n):
	t.circle(120)
	t.right(360/n)

for i in range(300):
	t.forward(i)
	t.right(91)
