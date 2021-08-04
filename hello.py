# msg="Hello World!"
# print(msg)


# # follow the indentation,
# # there should be space before
# if 5>2:
#     print("5 is greater than 2!!")


# # variables
# x = 5
# y = "John"    
# print(x, y)

# x = 4
# x = "Sally"
# print(x)

# print("###--Casting--###")
# x = str(3)
# y = int(3)
# z = float(3)
# print(x, y, z)

# print("###--Get the Type--###")
# x = 5
# y = "john"
# print(type(x))
# print(type(y))

# print("###--Assign multiple value--###")
# x, y, z = "Orange", "Apple", "Mango"
# print(x)
# print(y)
# print(z)

# print("###--Global varibale--###")
# print("1st without global function")
# x = "Awesome"

# def myfunc():
#     x = "fantastic"
#     print("python is " + x)

# myfunc()

# print("Python is " + x)

# print( "2nd with global function")

# def myfunc():
#     # declare global
#     global x
#     x = "fantastic"

# myfunc()

# print("Python is " + x)

print("###--Random Number--###")
import random

x = random.randrange(1, 10)
print(x)
