# Question 4 - Password Strength Checker 

password = input("Enter your password: ")

has_letter = False
has_number = False
has_special = False
special_chars = "@#$%&"


for ch in password:
    if ch in "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ":
        has_letter = True
    elif ch in "0123456789":
        has_number = True
    elif ch in special_chars:
        has_special = True


if len(password) < 6 or not has_letter:
    print("Password Strength: Weak")
elif len(password) >= 6 and has_letter and has_number:
    if len(password) >= 8 and has_special:
        print("Password Strength: Strong")
    else:
        print("Password Strength: Moderate")
else:
    print("Password Strength: Weak")
