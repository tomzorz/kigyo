import math

# if we have an object, we can call id() to get essentially the reference ID of it, kinda like a pointer? or a hash?

a = 1
b = 2

id(a) # this'll be some number
id(b) # this'll be a different number

b = a
id(b) # now this'll be the same as id(a)

a is b # this'll be true, it tests identity equivalence

p = [1, 2, 3]
q = [1, 2, 3]
p == q # is true
p is q # is false



# Basically everything is an object in python, even functions

type(math) # shows the type of the object

dir(math) # lists all attributes of an object

dir(math.factorial) # can be called for a method too, kinda like reflection