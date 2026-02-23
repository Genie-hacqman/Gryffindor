#Finishing Conditions , if statement , control flows modulo , match
"""
    using the operators in python to come up with condition 
    a == b 
    a >  b
    5 >= 5
    5 != 5

"""

"""
if conditions:

    if condition :
        pass
        
    if a == b :
        pass
    if a :
        pass
         4
    
# """
# def check_num():
#     value = input("what number do you choose ? : ")
#     if value < "6":
#         print('less than 6')
#     elif value > "20":
#         print("greater than 20")
#     elif value > "50":
#         print("greater than 50")
#     else:
#         print("the number is exactly the same .")

# check_num()


def check_day():
    day = input('enter a day of the week : ')

    match day:
        case "monday":
            print("Monday")
        case "tuesday":
            print("tuesday")
        case _:
            print("You need prayers")



# def parity():
#     user_input = int(input("enter a number : "))
#     if  user_input % 2 == 0:
#         print("Even")
#     else: 
#         print("Odd")


# def parity():
#     user_input = int(input("enter a number : "))
#     if  user_input % 3 == 0:
#         print("Odd")
#     else: 
#         print("Even")


# # lecture 2 
# i = 0
# while i != 2 :
#     print("meow")
#     i 


# animal = "cat"
# for loop
# for letter in  range(1,len(animal)):
#     print(animal[letter])


#enumerate use case
# for index, letter in enumerate(animal):
#     print(letter, index)

# def print_width():
#     sign = "#"
    
#     for i in range(3):
#         print("#" * 5)


# def calc(width , height):
#     return width  + "\n" + "" + height

# print(calc("###", "###"))

try: 
    print()
except NameError:
    print("This is a Name error") 
