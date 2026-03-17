print("Hello World 😎")
print("*" * 10) #print * ten times

students_count = 1000
rating = 4.99
is_published = False
course_name = "Python Programming"
print("Student's Count: ", students_count)
print(course_name, rating)

# long messages -> triple quotes
message = """
Hi John,

I hope this message finds you well.
"""

print(message)

# len = lenght of the string
print(len(course_name))
print(course_name[0])

# print(course_name[-1]) returns the LAST character!

print(course_name[0:4])
print(course_name[0:])
print(course_name[:3])
print(course_name[:])

# \"
# \'
# \\
# \n <- new line
course_name = "   \"Python\" Programming"
print(course_name)

# "parsing" text
first_name = "Shay"
last_name = "Miya"
#full_name = first_name + " " + last_name
full_name = f"{first_name} {last_name}" # formatted string: f"{x} {y}" = x + " " + y HOX! the amount of spaces matters!
print(full_name)
full_name = f"{len(first_name) * 2} {message}" # you can put any expression between the prackets
print(full_name)

# everything in python is an object!
print(course_name.upper())
print(course_name.lower())
print(course_name.title())
print(course_name.strip()) # delete white spaces from the start of the string
print(course_name.find("pro")) # returns -1 if the string isn't found
print(course_name.find("Pro")) # returns the index of where if the string is found
print(course_name.replace("P", "J"))
print("Pro" in course_name) # checks if the characters exists in string -> returns boolean
print("Swift" not in course_name) # returns a boolean

# numbers in python
x = 1
x = 1.1
x = 1 + 2j # a + bi python understands complex numbers, such as imaginary!

print