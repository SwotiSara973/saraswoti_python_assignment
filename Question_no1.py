# Question 1 - Type Conversion

decimal_number = float(input("Enter a decimal number: "))

integer_number = int(decimal_number)
string_number = str(decimal_number)

print(f"Original float: {decimal_number}")
print(f"Converted to integer: {integer_number}")
print(f'Converted to string: "{string_number}"')