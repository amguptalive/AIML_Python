# import colorgram
# colors = colorgram.extract('image.jpg', 30)
# # colorgram.extract returns Color objects, which let you access
# # RGB, HSL, and what proportion of the image was that color.
# # first_color = colors[0]
# # rgb = first_color.rgb # e.g. (255, 151, 210)
# rgb_colors = []
# for color in colors:
#     r = color.rgb.r
#     g = color.rgb.g
#     b = color.rgb.b
#     tuple_rgb = (r, g, b)
#     rgb_colors.append(tuple_rgb)

# print(first_color)
# print(rgb_colors)
import turtle as t
import random

tim = t.Turtle()
t.colormode(255)
tim.speed("fastest")
tim.penup()
tim.hideturtle()
color_list = [(212, 82, 64), (214, 152, 91), (231, 220, 87), (57, 91, 144), (25, 27, 41), (150, 70, 59),
              (106, 167, 205), (43, 22, 16), (42, 25, 33), (141, 68, 95), (192, 136, 159), (82, 163, 88),
              (208, 74, 93), (123, 179, 134), (55, 132, 92), (21, 41, 28), (151, 180, 60), (56, 54, 96),
              (229, 169, 184), (97, 46, 67), (57, 157, 185), (102, 44, 39), (230, 175, 163), (89, 122, 175),
              (169, 208, 177), (34, 77, 47)]
# tim.color(color_list[0])

tim.setheading(225)
tim.forward(300)
tim.setheading(0)
no_of_dots = 100

for dot_count in range(1, no_of_dots + 1):
    tim.dot(20, random.choice(color_list))
    tim.forward(50)
    if dot_count % 10 == 0:
        tim.setheading(90)
        tim.forward(50)
        tim.setheading(180)
        tim.forward(500)
        tim.setheading(0)

screen = t.Screen()
screen.exitonclick()

# RGB and HSL are named tuples, so values can be accessed as properties.
# These all work just as well:
# red = rgb[0]
# red = rgb.r
