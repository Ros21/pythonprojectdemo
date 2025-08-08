"""
if condition:
    # statements
elif condition:
    # statements
else:
    # statements
"""
# age = input("Enter your age: ")
# age = int(age)
# # <18 --> Child
# # >=18 to <=30 Young
# # >30 and <60 Middle age
# # >=60 Senior
#
#
# if 0<=age <18:
#     print("Child")
# # elif age >=18 and age <=40:
# elif 18<=age<=30:
#     print("Young")
# elif 30 < age < 60:
#     print("Middle age")
# elif 60<=age<=150:
#     print("Senior age")
# else:
#     print("Invalid age")


# for i in range(1,101):
#     print(i)

# names = ["Rakhsya", "Priyanka", "Sudip"]
# for name in names:
#     print(name)

# dict1 = {
#     "name": "Rakhsya",
#     "age": 22
# }
# print(dict1.keys())
# # print(dict1.values())
# print(dict1.items())
#
# for key, value in dict1.items(): #('name', 'Rakhsya')
#     print(key, value)

# for key in dict1.keys():
#     print(key)

# range         (start, stop, condition)
# for num in range(10):
#     print(num)

# phone_numbers = [ 11,21,33, 121,55]
# search_number =33
#
# for phone_number in phone_numbers:
#     if phone_number == search_number:
#         print("Phone number is in the database")
#         break
# else:
#     print("Phone number is not in the database")

# count = 0
# for num in range(1, 21, 2):
#     if num==9:
#         continue
#     print(num)
#     count += 1
#     if count>=5:
#         break
#     if num==17:
#         break


# even_numbers = []
# numbers = [1,22, 11, 5, 31, 6, 88, 31]
# for number in numbers:
#     if number % 2 == 0:
#         even_numbers.append(number)
# print(even_numbers) # 22,6,88


numbers = [1,22, 11, 5, 31, 6, 88, 31]
even_numbers = [number for number in numbers if number % 2 == 0]
print(even_numbers)

dict1 = {x:x*x for x in range(1,5)}
print(dict1)




