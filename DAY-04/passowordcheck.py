# #password strength checker 
# def check_password_strength(password):
#     if len(password)<8:
#         print("Password too short! Must be at least 8 characters.")
#         return False
#     if not any (char.isupper() for char in password):
#         print("Password must contain at least one uppercase letter.")
#         return False
#     if not any (char.islower() for char in password):
#         print("Password must contain at least one lowercase letter.")
#         return False
#     if not any (char.isdigit() for char in password):
#         print("Password must contain at least one digit.")
#         return False
#     print("Password is strong!")
#     return True
# user_password=input("Enter your password to check strength: ")
# check_password_strength(user_password)

import re

def pass_check(password):
    if len(password)<7:
        print("small")
    elif not re.search(r'[A-Z]',password):
        print("need one uppercase")
    elif not re.search(r'\d',password):
        print("need digit")
    elif not re.search(r'[a-z]',password):
        print("need lowercase")
    else:
        print("strong password")
password=input("enter the password  ")
pass_check(password)        
           




