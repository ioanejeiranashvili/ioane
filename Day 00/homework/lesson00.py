from turtle import *



#we want to paint a house


#step 1: draw a square
shape("turtle")
speed(777777)
width(7)
color("orange")
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


forward(70)
color("yellow")
left(90)

forward(120)          #height of the door
right(90)


forward(60)
right(90)

forward(120)

penup()
goto(200, 200)
pendown()

color("red")
begin_fill()
right(150)
forward(200)
left(120)
forward(200)
end_fill()

penup()
goto(70,140)
pendown()
begin_fill()
right(150)
forward(40)
right(90)
forward(50)
right(90)
forward(50)
right(90)
forward(50)
right(90)
forward(10)
end_fill()
exitonclick()