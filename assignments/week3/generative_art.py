#turtle art
#I tried to recreate the artwork: „The Swan, No. 17“ by Hilma af Klint
# I am aware that the artwork does not meet all the requirements, but it was quite difficult for me to apply the learned aspects from class to turtle and implement the specific requirements.

# import turtle
from turtle import *
import random
shape("classic")
t = Turtle()
speed(20)


# initial setup: canvas size
canvas_width = 400
canvas_height = 500
setup(canvas_width, canvas_height)

# set background color
farben = ["black", "gray20","hotpink4","lightblue4"]
bgcolor(random.choice(farben))


# draw star
penup()
goto(-80,120)
pendown()

color('lightgoldenrod1')
fillcolor('lightgoldenrod1')
begin_fill()
steps = 36
for i in range(steps):
    forward(150)
    left(170)
end_fill()

# draw first circle
penup()
goto(-5,75)
pendown()

fillcolor("darkgoldenrod3")
begin_fill()
circle(50, 360) # radius & angle
end_fill()

#draw second circle
penup()
goto(-5,46)
pendown()

width(10)
pencolor("lightslateblue")
circle(80)

# draw triangle
penup()
goto(-135,-190)
pendown()

width(2)

##first line
pencolor("lightpink1")
forward(260) # draw from starting point, go forward
left(115)

##second line
pencolor("royalblue")
forward(310)
position()
left(130)

##third line
pencolor("khaki1")
forward(308)
left(140)


# quite with click
exitonclick()