import turtle

turtle = turtle.Turtle()

def square(length,angle):
  turtle.forward(length)
  turtle.forward(angle)
  turtle.forward(length)
  turtle.forward(angle)
  turtle.forward(length)
  turtle.forward(angle)
  turtle.forward(length)
  turtle.forward(angle)

  square(120,90)
  