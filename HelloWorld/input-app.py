# type conversions
x = input("x: ") # ask user for an input -> always a string!
y = int(x) + 1
print(type(x)) # get the type of x
print(f"x: {x}, y: {y}")

# int(x)
# float(x)
# bool(x)
# str(x)

# Falsy values
# "" (empty hyphens)
# 0
# None

# Booleans
# bool(0) = false
# bool(1) = true
# bool(-1) = true
# bool(5) = true
# bool("False") = true
# bool("") = false