import turtle

def square(len):
  for i in range(4):
    turtle.forward(len)
    turtle.right(90)

def triangle(len):
  for i in range(3):
    turtle.forward(len)
    turtle.left(120)

def houce(len):
    square(len)
    triangle(len)

def main():
  turtle.speed(1)
  turtle.color("red")
  houce(100)
  turtle.penup()
  turtle.forward(200)
  turtle.color("blue")
  turtle.pendown()
  houce(50)

main()
turtle.screen().exitonclick()