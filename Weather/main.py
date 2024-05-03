# content = []

# with open(file="weather_data.csv",mode="r") as file:
#     for data in  file.readlines():
#         content.append(data.strip())

# print(content)

import csv

# Appedning only temparature data from csv file to temparatures list

# with open(file="weather_data.csv",mode="r") as file:
#     data = csv.reader(file)
#     temparatures = []
#     for row in data:
#         if row[1] == "temp":
#             continue
#         else:
#             temparatures.append(int(row[1]))

# print(temparatures)


import pandas as pd

data = pd.read_csv("weather_data.csv")
# print(type(data))
# print(data)

data_dict = data.to_dict()
#print(data_dict)

print("mean :", data["temp"].mean())
print("Max :",data["temp"].max())

#Printing the row with maximum temparature

print(data[data["temp"] == data["temp"].max()])

# converting celsuis to farehnheit for only day Monday
monday_temp_f = (data[data["day"] == "Monday"]["temp"])*(9/5)+32
monday_temp_c =data[data["day"] == "Monday"]["temp"]

monday_temp_c = monday_temp_c.values[0]
monday_temp_f =monday_temp_f.values[0]

print(monday_temp_c,"celsuis","=",monday_temp_f," Fareihnheit" )


