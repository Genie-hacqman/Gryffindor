# Import Regular Expressions
import re


# email = input("Enter your email")
# pattern = re.search("@", email)
# print(pattern.span())



# OOP- Object Oriented Programming




def mydecorator(f):
    def wrapper():
        print("start")
        f()
        print("end")
    return wrapper() 

@mydecorator   
def square():
    return 2**2
print(square)   









