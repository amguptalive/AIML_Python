# from turtle import Turtle, Screen
# # import another_module
# # print(another_module.another_variable)
#
# timmy = Turtle()
# print(timmy)
# timmy.shape("turtle")
# timmy.color("orange")
# timmy.forward(100)
#
# my_screen = Screen()
# print(my_screen.canvheight)
# my_screen.exitonclick()
# import prettytable
from prettytable import PrettyTable, DEFAULT, MARKDOWN, ORGMODE


table = PrettyTable()

table.add_column("Pokemon Name", ["Pikachu", "Squirtle", "Charmander"])
table.add_column("Type", ["Electric", "Water", "Fire"])
# table.attributes(
#     {"Key1": "Value1",
#      "Key2": "Value2"
#      }
# )
table.max_width = 300
table.align = "l"
# table.header = False
# table.border = False
table.sortby = "Pokemon Name"
table.reversesort = True
table.set_style(MARKDOWN )
print(table)




def dict_to_table(dictionary):
    table1 = PrettyTable()
    table1.field_names = dictionary.keys()
    table1.add_row(dictionary.values())
    table1.set_style(ORGMODE)
    return table1


my_dict = {"Name": "Alice", "Age": 30, "City": "Wonderland"}
print(dict_to_table(my_dict))

