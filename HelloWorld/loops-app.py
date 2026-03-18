# for-loops
for number in range(1, 10, 2): 
    print("Attempt", number, (number) * ".")

# range(3) runs 3 times, starting from 0
# range(1, 4) runs 3 times, starting from 1 and ending on 4
# range(1, 10, 2) starts from 1, stops at 10 and goes forward 2 steps at a time (1, 3, 5, 7, 9)

# for ... else
successful = True

for number in range(3):
    print("Attempt")
    if successful:
        print("Successful")
        break # stops the loop aka breaks out of the loop
else:
    print("Attempted 3 times and failed")

# nested loops
for x in range (5):
    for y in range(3):
        print(f"({x}, {y})")

# iterables = an object that can be iterated over bruh CAN BE ALSO A STRING?? or a custom object??
print(type(5))
print(type(range(5))) # range is its own object

for x in "Python":
    print(x)

for x in [1, 2, 3, 4]:
    print(x)

# while-loops
number = 100
while number > 0:
    print(number)
    number //= 2

command = ""
while command.lower() != "quit": # allows user to type quit in any way
    command = input(">")
    print("ECHO", command)

# infinite loop
while True:
    command = input(">")
    print("ECHO", command)
    if command.lower() == "quit":
        break

# EXERCISE: Display even numbers between 1-10 and count how many there are

counter = 0

for number in range(1, 10):
    if number % 2 == 0:
        counter += 1
        print(number)
# print("We have", counter, "even numbers")
print(f"We have {counter} even numbers") # remember to use formatted strings!