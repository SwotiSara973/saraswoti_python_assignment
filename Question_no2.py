# Question 2 - Extract Initials 

full_name = input("Enter your full name: ")

first_initial = full_name[0].upper()
space_index = full_name.find(' ')


if space_index != -1:
    last_initial = full_name[space_index + 1].upper()
    print("Your initials are:", first_initial + "." + last_initial)
else:
    print("Your initials are:", first_initial)
