from turtle import *


#we want to paint house
width(7)
color("purple")
speed(30)
#step 1:  draw a square
forward(200)
left(90)

forward(200)
left(90)

forward(200)
left(90)

forward(200)
left(90)


#end of square

#drawing a door
begin_fill()
forward(70)
color("yellow")
left(90)



forward(120)
right(90)
forward(60)
right(90)
forward(120)
end_fill()
penup()
goto(200, 200)
pendown()
begin_fill()
color("red")
right(150)
forward(200)
left(120)
forward(200)
end_fill()

right(60)
penup()
goto(30,150)
pendown()
color("brown")
width(3)
right(180)
forward(40)

left(90)
forward(35)
left(90)

forward(40)
left(90)
forward(35)

penup()
goto(130,150)
pendown()

left(90)
forward(40)
left(90)
forward(35)
left(90)
forward(40)
left(90)
forward(35)





exitonclick()