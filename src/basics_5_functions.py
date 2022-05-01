
# functions are a thing

def square(x):
    return x * x


# functions don't have to return things
# but all functions implicitly return None unless you return something


# special functions have __ and __ at the beginning and end respectively
# "dunder" is a portmanteau of double underscore
# so e.g. __name__ shall be referred to as dunder name


# def is actually a statement -> the def will run when importing
# this also explains why ordering matters


# parameters and returns are always passed by reference


# we can use default argument values, they have to be last like in c#

def pad(message, elem=' '):
    pass # pass is a magic function that does nothing, a no-op

# when calling, we can name the argument - they are matched by name, so we can change the order, similar to c#

pad("asd") # is valid
pad("asd", "-") # is valid
pad("asd", elem="*") # is valid and preferred

# Important, that the default values are only evaluated ONCE, WHEN the def statement runs. So e.g. a default value of the current time won't update with each call!
# This also means, that mutable values are mutated with each subsequent call, e.g.

def addfoo(l=[]):
    l.append("foo")
    return l

addfoo(["asd", "bar"]) # will return ["asd", "bar", "foo"]

addfoo() # will return ["foo"] as expected
addfoo() # will return ["foo", "foo"] !
addfoo() # will return ["foo", "foo", "foo"] !!

# so anyway, always use immutable objects for default values!