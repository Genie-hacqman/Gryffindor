"""
* working with json files
*password generator
TODO

- use of functional programmming
- seperate logics if possible
  - a function to generate passoword
  -- a function  to load => modity => save json file
  ----
"""

import json  # 
from json import JSONDecodeError
# jsonDecodeError is part of json module used working with json files
import string   # module holding add characters
import secrets  # generator


def main():
    
    
    ou = user_signup()
    print(ou)


def password_generator():

    upper = string.ascii_uppercase
    lower = string.ascii_lowercase
    digits = string.digits
    symbols = "!@#$%^&*()-_=?"    # i only want these symbols TODO => i will use string.punction 
    
    all_characters = upper + lower + digits + symbols
    
    while True:
        try:
            length = int (input("enter password length: \n"))
            if length >= 8:
                break
            else:
                print("must be 8 ")
                continue
        except ValueError:
            print("invalid input")
            continue
    
    password = ''.join(secrets.choice(all_characters)for _ in range(length))
    return password
    




def user_signup():
    
    first_name = input("enter first name: \n" ).strip().title()
    middle_name = input( "enter middle name: \npress 'enter-key' to skip\n" ).strip().title()
    middle_name = middle_name if middle_name else None
    last_name = input ("enter last name: \n").strip().title()
    date_of_birth = input ("enter Date of Birth: \n eg. 13 05 1995\n").split() 

    # Phone Number MUST be 10 and valid 
    
    try:
        phone_number = int(input("enter phone number:\n"))
        if len(phone_number) == 10:
            phone_number
            
        else:
            print("number should be 10")
            
    except (TypeError, ValueError, UnboundLocalError):
        print("enter correct ")
            

    email = input ("enter email: \n").strip().lower()
    username = input ("enter your username: \n (its case-sensitive)\n").strip()

    while True:
        password = input("enter password:\nPassword Must be more than 8 charaters \nPress 'p' to Generate Password\n")
        match password:
            case 'p':
                password = password_generator()
                password
                break
            case _:
                if len(password) < 8:
                    continue
                else:
                    password
                    break


    data_input = {
        "first_name" : first_name,
        "middle_name" : middle_name,
        "last_name" : last_name,
        "date_of_birth" : date_of_birth,
        "phone_number" :phone_number,
        "email" : email,
        "username" : username,
        "password" : password
    }


    
# working with json files follows ===> load -> Modify -> save
# i will use try and except to help prevent errors 
# you can not modify json files directly like txt you have to load to python first, append and save/dump back

#load file into python
    try:
        with open("config.json", "r", encoding="utf-8") as file:
            data = json.load(file) 
    except (JSONDecodeError, FileNotFoundError):
        data = []
#json file in python list now 

    data.append({username:data_input}) # data modified 

#save the file back
    with open("config.json", "w", encoding="utf-8") as file:
        json.dump(data, file, indent=4)


# front logic
def user_main():
    message = input(f"\n{"="*5} welcome to Logcast {"="*5} \nSELECT OPTION\n1: sign Up \n2: Login \n3: Generate Password \npress 'n' to exit program").strip()
    
    match message:
        case 'n' | "N":
            return "Program Exited ...."
        case "1":
            return user_signup()
        case "2":
            return user_login()
        case "3":
            return password_generator()
        case _:
            return "invalid user choice"




# if user already has account, he can login here
def user_login():
    pass


if __name__ == "__main__":
    main()