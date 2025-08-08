# def add(a,b):
#     total = a+b
#     return total
from symtable import Function

# add = lambda a,b: a+b
# divide = lambda a,b: a/b
#
#
# print(f"Sum is {add(1,2)}")

#capitalize_letter("Ram") --> "RAM"


# Write a lambda function to find square of the given number






# def greet(first_name= "Lucky", last_name= "User"):
#     print("Hello " + first_name + " " + last_name)
#
# greet("Will", "Smith")
# greet("Rajesh")
# greet()
# greet(last_name="Smith")





# def add(a, b):
#     return a + b


# add = lambda a,b : a + b
#
# print(add(1, 2))




# name ="Ram"
#
# def greet():
#     # global name
#     name ="John"
#     print("Hello " + name)
#
# greet()
# print(name)
#
# Main program
# # name --> John
#
#
# Function
# # name --> John
#
#
#
#
#
#


# x = "global"
# def outer():
#     # x = "enclosing"
#     def inner():
#         # x = "local"
#         print(x)
#     inner()
# outer()  # Output: local


def make_multiplier(factor):
    def multiplier(number):
        return number * factor
    return multiplier


# double = make_multiplier(2)
# triple = make_multiplier(3)
# print(double(5))  # 10
# print(triple(5))  # 15



