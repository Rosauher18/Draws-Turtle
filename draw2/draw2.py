from turtle import *
import colorsys

tracer(3)
h = 0.7
bgcolor('black')
pensize(1)

for i in range(190):
    c = colorsys.hsv_to_rgb(h, 1, 1)
    color(c)
    h += 0.004
    circle(180 - i, 90)
    lt(75)
    lt(15)
    circle(180 - i, 90)
    lt(18)
done()
