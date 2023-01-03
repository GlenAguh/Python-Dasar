# import turtle

# s = turtle.Screen()
# t = turtle.Turtle()

# s.bgcolor('#262626')
# t.pencolor('#540d6e')
# t.speed(100)
# col = ('#ee4266', '#ffd23f', '#3bceac', '#0ead69')

# for n in range(5):
#     for x in range(8):
#         t.speed(x+10)
#         for i in range(2):
#             t.pensize(2)
#             t.circle(80+n*20,90)
#             t.lt(90)
#         t.lt(45)
#     t.pencolor(col[n%4])
# s.exitonclick()

# from turtle import *
# import random

# drawing_area = Screen()
# drawing_area.setup(width=750, height=500)

# shape('square')
# width(2)
# colors = ['red', 'orange', 'yellow', 'green', 'blue', 'indigo', 'violet']

# for i in range(75):
#     color(random.choice(colors))
#     right(20 + i)
#     forward(1 + (i * 5))
#     right(40 + i)

# done()


from turtle import *
import random

drawing_area = Screen()
drawing_area.setup(width=750, height=500)

shape('square')
width(2)
colors = ['red', 'orange', 'yellow', 'green', 'blue', 'indigo', 'violet']


def draw_triangle(length=150):
    color(random.choice(colors))
    for i in range(3):
        forward(length)
        left(120)


for i in range(40):
    draw_triangle()
    right(10)

done()