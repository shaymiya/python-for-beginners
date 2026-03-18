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

# iterables