import turtle



t = turtle.Turtle()

turtle.bgcolor("black")

coffee1 = "#6D4C41"

coffee2 = "#5D4037"

coffee3 = "#4E342E"

coffee4 = "#3E2723"

green1 = "#00FF00"

green2 = "#229954"

green3 = "#006600"

white = "white"

yellow1 = "#FFEB3B"

yellow2 = "#FFCA28"

yellow3 = "#FFA000"

red1 = "#FF0000"

red2 = "#E53935"

red3 = "#B71C1C"



def square(color):

    t.pencolor(color)

    t.fillcolor(color)

    t.begin_fill()

    t.seth(0)

    t.forward(30)

    t.seth(90)

    t.forward(30)

    t.seth(180)

    t.forward(30)

    t.seth(270)

    t.forward(30)

    t.end_fill()

    

def go(x,y):

    t.penup()

    t.goto(x,y)

    t.pendown()

    

def maceta(x, y):

    go(x, y)

    square(coffee1) 

    go(x+30, y)

    square(coffee2) 

    go(x+60, y)

    square(coffee3)

    go(x+90, y)

    square(coffee3)

    go(x+120, y)

    square(coffee3)

    go(x+150, y)

    square(coffee4)

    

    go(x, y+30)

    square(coffee1) 

    go(x+30, y+30)

    square(coffee1) 

    go(x+60, y+30)

    square(coffee2)

    go(x+90, y+30)

    square(coffee1)

    go(x+120, y+30)

    square(coffee3)

    go(x+150, y+30)

    square(coffee4)

    

    go(x, y+60)

    square(coffee1) 

    go(x+30, y+60)

    square(coffee1) 

    go(x+60, y+60)

    square(coffee1)

    go(x+90, y+60)

    square(coffee2)

    go(x+120, y+60)

    square(coffee3)

    go(x+150, y+60)

    square(coffee4)

    

    go(x, y+90)

    square(coffee1) 

    go(x+30, y+90)

    square(coffee1) 

    go(x+60, y+90)

    square(coffee2)

    go(x+90, y+90)

    square(coffee3)

    go(x+120, y+90)

    square(coffee2)

    go(x+150, y+90)

    square(coffee4)

    

    go(x, y+120)

    square(coffee1) 

    go(x+30, y+120)

    square(coffee2) 

    go(x+60, y+120)

    square(coffee1)

    go(x+90, y+120)

    square(coffee1)

    go(x+120, y+120)

    square(coffee3)

    go(x+150, y+120)

    square(coffee2)

    

    go(x, y+150)

    square(coffee1) 

    go(x+30, y+150)

    square(coffee1) 

    go(x+60, y+150)

    square(coffee1)

    go(x+90, y+150)

    square(coffee2)

    go(x+120, y+150)

    square(coffee1)

    go(x+150, y+150)

    square(coffee2)

    

maceta(-210, -300)



go(-150, -120)

square(green1)

go(-150, -90)

square(green1)

go(-120, -90)

square(green2)

go(-150, -60)

square(green1)

go(-120, -60)

square(green2)

go(-180, -30)

square(green2)

go(-150, -30)

square(green1)

go(-120, -30)

square(green2)

go(-90, -30)

square(green2)

go(-210, 0)

square(green2)

go(-180, 0)

square(green1)

go(-150, 0)

square(green1)

go(-150, 30)

square(green1)

go(-150, 60)

square(green1)

go(-120, 60)

square(green2)



go(-180, 90)

square(white)

go(-150, 90)

square(white)

go(-120, 90)

square(white)

go(-210, 120)

square(white)

go(-180, 120)

square(white)

go(-150, 120)

square(white)

go(-120, 120)

square(white)

go(-90, 120)

square(white)

go(-240, 150)

square(white)

go(-210, 150)

square(white)

go(-180, 150)

square(yellow2)

go(-150, 150)

square(yellow1)

go(-120, 150)

square(yellow3)

go(-90, 150)

square(white)

go(-60, 150)

square(white)

go(-240, 180)

square(white)

go(-210, 180)

square(white)

go(-180, 180)

square(yellow1)

go(-150, 180)

square(yellow1)

go(-120, 180)

square(yellow2)

go(-90, 180)

square(white)

go(-60, 180)

square(white)

go(-240, 210)

square(white)

go(-210, 210)

square(white)

go(-180, 210)

square(yellow2)

go(-150, 210)

square(yellow1)

go(-120, 210)

square(yellow1)

go(-90, 210)

square(white)

go(-60, 210)

square(white)

go(-210, 240)

square(white)

go(-180, 240)

square(white)

go(-150, 240)

square(white)

go(-120, 240)

square(white)

go(-90, 240)

square(white)

go(-180, 270)

square(white)

go(-150, 270)

square(white)

go(-120, 270)

square(white)



maceta(90, -300)



go(150, -120)

square(green3)

go(180, -120)

square(green3)

go(90, -90)

square(green3)

go(120, -90)

square(green3)

go(150, -90)

square(green3)

go(180, -90)

square(green3)

go(60, -60)

square(green3)

go(90, -60)

square(green3)

go(150, -60)

square(green1)

go(180, -60)

square(green3)

go(210, -60)

square(green3)

go(240, -60)

square(green3)

go(150, -30)

square(green1)

go(150, 0)

square(green1)

go(150, 30)

square(green1)

go(90, 60)

square(red1)

go(120, 60)

square(green3)

go(150, 60)

square(green3)

go(60, 90)

square(red1)

go(90, 90)

square(red1)

go(120, 90)

square(red1)

go(150, 90)

square(red1)

go(180, 90)

square(red3)

go(60, 120)

square(red1)

go(90, 120)

square(red2)

go(120, 120)

square(red3)

go(150, 120)

square(red2)

go(180, 120)

square(red1)

go(210, 120)

square(red3)

go(90, 150)

square(red1)

go(120, 150)

square(red2)

go(150, 150)

square(red3)

go(180, 150)

square(red1)

go(210, 150)

square(red2)

go(150, 180)

square(red3)

go(180, 180)

square(red3)



t.hideturtle()

turtle.done()
