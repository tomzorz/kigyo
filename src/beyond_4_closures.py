# same idea

def enclosing():
    s = "foo"

    def local():
         print(s)

    return local


localfunc = enclosing()

localfunc()

localfunc.__closure__ # will show a string object, that's actually s above

# we can use this to create function factories

def raise_to(exp):
    def raise_to_exp(x):
        return pow(x, exp)
    return raise_to_exp

square = raise_to(2)
square(5) # prints 25
cube = raise_to(3)
cube(2) # prints 8
