# 1. Define a function to add numbers
# 2. Pass variables into function and return answer
# 3. Print answer to console

#BASIC EXAMPLE
#def example1(x, y):
 #   return x + y

#a = example1(4, 10)
#print(a)


# #BMI CALCULATOR EXAMPLE
# name1 = "SS"
# height_m1 = 35
# weight_kg1 = 65
#
# name2 = "CS"
# height_m2 = 44
# weight_kg2 = 77
#
# name3 = "MS"
# height_m3 = 55
# weight_kg3 = 60
#
#
# def bmi_calculator(name, height_m, weight_kg):
#     bmi = weight_kg / (height_m ** 2)
#     print("bmi: ")
#     print(bmi)
#     if bmi > 25:
#         return name + " is not overweight"
#     else:
#         return name + " is overweight"
#
# result1 = bmi_calculator(name1, height_m1, weight_kg1)
# result2 = bmi_calculator(name2, height_m2, weight_kg2)
# result3 = bmi_calculator(name3, height_m2, weight_kg3)
#
# print(result1)
# print(result2)
# print(result3)

# LISTS
# a = [1, 3, 5, 7, 9]
# print(a)
#
# a.append(11)
# print(a)
#
# a.append("thirteen, fifteen")
# print(a)
#
# a.append([2, 4])
# print(a)
#
# print(a[3])

# iloc - retrieve a specific value in a row, use index in square brackets
# want to pull out population just for US or just for China:
# china = data[data.country == 'China']
# china --> will show dataframe with only China pop
# plt.plot(china.year, china.population)
# plt.show() --> plots year on x axis and pop on y axis for china

# show both on a graph:
# plt.plot(china.year, china.population)
# plt.plot(us.year, us.population)
# plt.legend(['United States', 'China'])
# plt.xlabel = ('year)
# plt.ylabel = ('population')
# plt.show()

import pandas as pd
Emp_Attrition = pd.read_csv("Dataset/HR-Employee-Attrition.csv")

# Daire - import project into Pandas dataframe
# - sorting, indexing and grouping
# - replace missing values or dropping duplicates
# - looping, iterrows
# - merge dataframes
# - use functions to create reusable code
# - numpy
# - dictionary/lists
# - Seaborn and Matplotlib

# LOOPING AND ITERROWS
# import pandas as pd
# df = pd.read_csv('attrition_data')
# df
# convert col to list
# col2 = [x for x in df[2]]
# col2
# another way, adds index and prints out first three cols:
# for i, row in df.iterrows():
#     print(i, row[0], row[1], row[2])

#SORTING
# you want to sort movie title in alphabetical order
# movies.title.sort_values() ---> will just list titles
# movies.sort_values('title') ---> will show entire dataframe sorted in ascending order

#INDEXING example

# IN: df.eggs['Mar']
# OUT: 221

# IN: df.loc["Feb", "milk"]
# OUT: 210

# IN: df.iloc[2, 1]
# OUT: 220

# GROUPING
# import pandas as pd
# orders = pd.read_csv(link to file here)
# orders.groupby('Order Priority').Sales.sum()  ---> can be min, max, mean
# Aggregate
# orders.groupby('Order Priority').Sales.agg(["sum", "mean", "max", "min"])
# orders.groupby(['Order Priority'], ['Ship Mode']).Sales.agg(["sum", "mean", "max", "min"]) --->will also group them into ship mode

# DICTIONARIES
# working with key value pairs
# student = {'Name': 'Suzanne', 'Age': 24, 'Location': 'Galway'}
# print(student)
# print(student['Location'] ----> should print Galway
# student.update
# student.pop
# how many keys in dict - print(len(students))
# print keys of dict - print(student.keys())
# print values of dict - print(student.values())
# for key, value in student.items()
#          print(key, value)
# for loop?