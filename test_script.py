# 1. Define a function to add numbers
# 2. Pass variables into function and return answer
# 3. Print answer to console

#BASIC EXAMPLE
#def example1(x, y):
 #   return x + y

#a = example1(5, 10)
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

a = [1, 3, 5, 7, 9]
print(a)

a.append(11)
print(a)

a.append("thirteen, fifteen")
print(a)

a.append([2, 4])
print(a)

print(a[3])