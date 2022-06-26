import traceback

# let's do advanced error handling

# catching ALL exceptions is a very bad idea, it'll cause catching even the keyboard interrupt
# lesson: always specify the exception type

# exceptions are arranged in an inheritance hierarchy
# ..., ..., Exception, BaseException, builtin.object
#            > everything comes from Exception
#                       > except for system exiting ones, those come from BaseException (generator exit, keyboard interrupt, system exit)
#            > makes it seem nice to catch all "Exception" but this will also catch SyntaxError, ImportError, NameError and AssertionError as well

# python docs have the entire exception hierarchy

# exception payloads, most stuff accepts a string for extra information (technically args can be anything, but a single string is recommended)

# most typical exception would be ValueError (c# argumenterror) when we're validating
# but other specific errors will have specific attributes that help us debug things

# defining our own exceptions
import math


class MyException(Exception):
    pass

class MyAdvancedException(Exception):

        def __init__(self, text, data):
            super().__init__(text) # we need to call manually
            self._data = data

        @property
        def data(self):
            return self._data


# we can chain exceptions, kinda like InnerException in C#

# if an exception happens while handling an exception, that's implicit chaining
# the outer exception's dunder context will have the inner exception in it

# we can deliberately do this using explicit chaining

class InclinationError(Exception):
    pass

def inclination(dx, dy):
    try:
        return math.degrees(math.atan(dy / dx))
    except ZeroDivisionError as e:
        raise InclinationError("Vertical slope!") from e # notice the "from e" language here
        # instead of dunder context, we'll get dunder cause here!


# tracebacks (or c# stack traces)

# exceptions will have a dunder traceback
# but we can also call traceback separately if we want

# print vs format in traceback: print to print, format to get a string
# also DO NOT keep references to the traceback object, as it has closure over literally anything before it basically, and it'll lead to epic memory leaks
# so basically render it out to a string if we need to keep it

# python has asserting in it
# assert condition [, message]

# assert False, "the condition was false"
# this would yell at us!

# best to place these at e.g. else paths or assumptions

def mod_three(n):
    r = n % 3
    if r == 0:
        print("multiple of 3")
    elif r == 1:
        print("remainder 1")
    else:
        assert r == 2, "remainder is not 2" # better than commenting
        print("remainder 2")

# running python with -O option will run without assertions

# don't use assertions for checking arguments