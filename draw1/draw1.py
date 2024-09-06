import turtle

turtle.speed(10)
fondo = turtle.Screen()
fondo.bgcolor("yellow")

for i in range(400):
  turtle.forward(100)
  turtle.right(90)
  for j in range(1):
     turtle.forward(100)
     turtle.right(80)


turtle.exitonclick()