import turtle

def draw_initials():
    window = turtle.Screen()
    window.bgcolor("black")

    pencil = turtle.Turtle()
    pencil.setx(-150)
    pencil.sety(85)
    pencil.shape("turtle")
    pencil.color("red")

    for _ in range(3):
        pencil.forward(100)
        pencil.left(90)

    pencil.forward(200)

    pencil.penup()
    pencil.setx(10)
    pencil.sety(45)

    pencil.color("purple")
    pencil.pendown()

    for _ in range(1,4):
        pencil.forward(45)
        pencil.left(60)
        
    pencil.forward(180)
    
    pencil.right(90)
    pencil.forward(65)
    pencil.left(180)
    pencil.penup()
    pencil.forward(65)
    pencil.pendown()
    pencil.forward(65)

    window.exitonclick()

draw_initials()
