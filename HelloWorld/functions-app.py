def greet(first_name, last_name): # functions start with def
    print(f"Hi there {first_name} {last_name}")
    print("Welcome aboard")

greet("Shay", "Miya")

# greet(input("First Name: "), input("Last Name: "))

# types of functions:
# 1- perform a task
# 2- Return a value

def get_greeting(name):
    return f"Hi {name}"

message = get_greeting("Shay")
print(message)

# file = open("content.txt", "w") # open a file and Write on it
# file.write(message)

# keyword arguments
def increment(number, by=1): # add default values on the function here! NOTE that after the first default there can't be any required parameters WITHOUT definition! 
    return number + by

result = increment(2,1)
print(result)
# OR
print(increment(4, by=5)) # keywording!

print(increment(2))

# xargs
def multiply(*numbers): # to add no cap to the arguments, replace x, y etc with '*numbers'
    print(numbers)
    total = 1
    for number in numbers:
        total *= number
    return total # be mindful of the indantations?? the spaces thing


print(multiply(2, 3, 4, 5))

# list: [1, 2, 3, 4]