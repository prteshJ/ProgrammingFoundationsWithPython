import turtle

def draw_square(some_turtle):
        for _ in range(4):
            some_turtle.forward(100)
            some_turtle.right(90)
    

def draw_polygons():
    window = turtle.Screen()
    window.setup(562,640)
    window.bgpic("bg.gif")
    window.bgcolor("darkgreen")
    
    brad = turtle.Turtle()
    brad.penup()
    brad.setx(-245)
    brad.sety(85)
    brad.shape("turtle")
    brad.color("purple")
    brad.speed(4)

    brad.pendown()
    draw_square(brad)

    wiggly = turtle.Turtle()
    wiggly.penup()
    wiggly.setx(50)
    wiggly.sety(-135)
    wiggly.speed(10)
    wiggly.shape("turtle")
    wiggly.color("orange")
    wiggly.pendown()
    for _ in range(1,37):
        draw_square(wiggly)
        wiggly.right(10)
    
    angie = turtle.Turtle()
    angie.shape("arrow")
    angie.color("blue")
    angie.speed(2)
    angie.circle(100)
    
    pixar = turtle.Turtle()
    pixar.penup()
    pixar.setx(-245)
    pixar.sety(85)
    pixar.shape("arrow")
    pixar.color("red")
    pixar.pendown()
    pixar.forward(100)
    pixar.left(120)
    pixar.forward(100)
    pixar.left(120)
    pixar.forward(100)
    
    window.exitonclick()
    
draw_polygons()

