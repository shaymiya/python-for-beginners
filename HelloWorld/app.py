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
course_name = "\"Python\" Programming"
print(course_name)

# "parsing" text
first_name = "Shay"
last_name = "Miya"
#full_name = first_name + " " + last_name
full_name = f"{first_name} {last_name}" # f"{x} {y}" = x + " " + y HOX! the amount of spaces matters!
print(full_name)
