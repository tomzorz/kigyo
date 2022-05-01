
# int
# arbitrarily large integers
i = 42

# integers are immutable in python
# when assigning a number to a variable, a new int will be created and the reference will change, the prev one will be garbage collected

# ints can be defined by binary, octal and hex representations
binary = 0b10 # this is 2
octal = 0o10 # this is 8
hexa = 0x10 # this is 16

# we can also make them from other things
fromfloat1 = int(3.5) # this rounds towards 0, so it'll be 3
fromfloat2 = int(-3.5) # also rounds towards 0, so it'll be -3
fromstring1 = int("123") # will be 123
fromstring2 = int("10000", 3) # will convert from base 3, so it'll be 81

# float
# 64 bit precision floating point numbers (like c# double)
f = 4.2

# floats can be defined by scientific notation too
morefloat1 = 3e8
morefloat2 = 1.616e-35

# we can also make them from other things
evenmorefloat1 = float(7)
evenmorefloat2 = float("3.1415")

# spcial floating point "numbers"
notanumber = float("nan")
posinf = float("inf")
neginf = float("-inf")

# any calculation between int and float will become a float

# null object
n = None

# boolean values
b = True or False

# python has "and" and "or" for boolean expressions

# values can be falsy and truthy
# the bool constructor is only necessary when declaring something, as python will auto-convert the expression when bool is expected
truthyexample = bool(3245)

# for integers, 0 is falsy and everything else is truthy
# for floats, 0.0 is falsy and everything else is truthy
# for collections, empty is falsy and everything else is truthy
# for strings, empty strings are falsy and everything else is truthy