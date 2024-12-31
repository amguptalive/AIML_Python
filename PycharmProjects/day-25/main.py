# with open("weather_data.csv") as data_file:
#     data = data_file.readlines()
# print(data)
# import csv
#
# with open("weather_data.csv") as data_file:
#     data = csv.reader(data_file)
#     temperatures = []
#     for row in data:
#         if row[1] != "temp":
#             temperatures.append(int(row[1]))
#     print(temperatures)
import pandas

data = pandas.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")
red_squirrel_count = len(data[data["Primary Fur Color"] == "Cinnamon"])
gray_squirrel_count = len(data[data["Primary Fur Color"] == "Gray"])
black_squirrel_count = len(data[data["Primary Fur Color"] == "Black"])
print(red_squirrel_count)
print(gray_squirrel_count)
print(black_squirrel_count)
data_dict = {
    "Fur Color": ["Cinnamon", "Gray", "Black"],
    "Count": [red_squirrel_count, gray_squirrel_count, black_squirrel_count]
}
df = pandas.DataFrame(data_dict)
df.to_csv("squirrel_count.csv")

# print(data["Primary Fur Color"].groupby("Primary Fur Color").mean())
# print(data["temp"])
# print(type(data))  # will print pandas.core.frame.DataFrame
# print(type(data["temp"]))  # will print pandas.core.series.Series
#
# data_dict = data.to_dict()
# print(data_dict)
#
# temp_list = data["temp"].to_list()
# print(temp_list)
#
# total_temp = 0
# for i in range(len(temp_list)):
#     total_temp += temp_list[i]
# avg_temp = total_temp / len(temp_list)
# print(avg_temp)
#
# avg_temp = sum(temp_list) / len(temp_list)
# print(avg_temp)
#
# print(data["temp"].mean())
#
# print(data["temp"].max())
