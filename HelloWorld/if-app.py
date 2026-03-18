# comparison operators in python
print("bag" > "apple") # returns true, since b's # is higher than a's
print("bag" == "BAG") # returns false, since b's # is different from B's

# checking the numeral codes for alphabet
print(ord("b"))
print(ord("a"))
print(ord("B"))

# conditional statements
temperature = 15
if temperature > 30: # : terminates the statement, acts like {
    print("It's warm") # incantations? mark the code block for if statement
    print("Drink water")
elif temperature > 20:  # elif = else if
    print("It's nice")
else:
    print("It's cold")
print("Done") # runs no matter what

# ternary operator
age = 22

if age >= 18:
    message = "Eligible"
else:
    message = "Not eligible"

print(message)

# OR

message = "Eligible" if age >= 18 else "Not eligible" # this is called ternary operator!
print(message)

# logical operators : and, or & not
high_income = False
good_credit = True
student = True

if (high_income or good_credit) and not student:
    print("Eligible")
else:
    print("Not eligible")

# chaining comparison operators:
# age should be between 18 and 65

age = 22
if age >=18 and age < 65:
    print("Eligible")
# OR CLEANER
if 18 <= age < 65: # chaining comparison operators
    print("Eligible")