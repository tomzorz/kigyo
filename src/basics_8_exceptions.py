# somewhat similar to c#

# here we have "try" and "except"

try:
    ded = 1/0
except ZeroDivisionError:
    print("you tried to divide by zero")

# similarly to c# again, we can have multiple "except" blocks for various exception types
# we can also group exceptions into tuples

try:
    d = {}
    v = d[0]
except (KeyError, TypeError):
    print("we had an exception")

# to support empty "oh well" except blocks, we use the "pass" method

# we can name the exception objects too

try:
    d = {}
    v = d[0]
except KeyError as k:
    print(f"we had an exception {k!r}")

# we can use the "raise" keyword in an "except" block to re-throw the exception

# we can add a "Raises:" part to the docstrings to indicate what exceptions a method can raise

# standard exception types
# call "raise Exception()"
# for invalid arguments, but right type -> ValueError
# for invalid types -> TypeError
# sequence out of bounds -> IndexError
# lookup fails -> KeyError

# it's recommended not to catch TypeErrors
# python tenet: "easier to ask forgiveness than permission" -> try do the happy path, handle all errors after

# python also has "finally" which always runs

try:
    ze = 1/0
    print("we made it past division by zero")
finally:
    print("this gets calls anyway")