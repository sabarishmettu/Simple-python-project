import turtle
wn = turtle.Screen()
wn.bgcolor("#f3eef0")

flower = turtle.Turtle()

flower.color("#ff00ff")
flower.shape("turtle")

flower.left(0)
flower.forward(0)
flower.right(90)

for i in range(4,44):
    flower.forward(50)
    flower.right(50)

flower.right(90)
flower.forward(0)
flower.left(0)
flower.forward(0)

wn.exitonclick()
