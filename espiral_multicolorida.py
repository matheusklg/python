#espiral_multicolorida


import turtle

turtle.bgcolor('black')   #cor de fundo
p = turtle.Pen()

cores = ['red', 'yellow', 'blue', 'green']

for x in range(100):
    p.pencolor(cores[x % 4])
    p.circle(x * 5)
    p.left(91)

    
