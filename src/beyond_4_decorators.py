import functools

# modify and enhance functions

# takes a func and returns a func basically
# we can replace, enhance or modify functions

# @decorator
# def my_function():
#   pass

def decorator(f):
    pass
    return f

@decorator
def function():
    pass

# a more specific example

def escape_unicode(f):
    def wrap(*args, **kwargs):
        x = f(*args, **kwargs)
        return ascii(x)

    return wrap


@escape_unicode
def hungarian():
    return "űáőúíéüó"


# see how we can use decorator for
# - injecting
# - error handling

# we can also use classes as decorators

class DecoratorClass:
    def __init__(self, f):
        print("decorator init")
        self.f = f
        self.count = 0

    def  __call__(self, *args, **kwargs):
        self.count += 1
        return self.f(*args, **kwargs)

# applying the class as a decorator will create a new instance

@DecoratorClass
def hey(name):
    print(f"hello {name}")

# we can also use class instances as decorators

class Trace:
    def __init__(self):
        self.enabled = True

    def __call__(self, f):
        def wrap(*args, **kwargs):
            if self.enabled:
                print(f"Calling {f}")
            return f(*args, **kwargs)
        return wrap


tracer = Trace()

@tracer
def heyo(name):
    print(f"heyo {name}")

# we can do tracer.enabled = false
# and that'll cause the trace decorator not to do anything

# it's possible to use multiple decorators for a function
# in this case they are processed in reverse order, so closed to the func will be called first.


# important to note, that decorators cause us to lose a lot of metadata
# we can solve that with functools.wraps()
# properly updates metadata

def noop(f):
    @functools.wraps(f)
    def noop_wrapper():
        return f()
    return noop_wrapper

@noop
def asd():
    print("asd asd")


# we can also use decorators to ensure arguments

def non_negative(index):
    def validator(f):
        def wrap(*args):
            if args[index] < 0:
                raise ValueError("must be non-negative")
            return f(*args)
        return wrap
    return validator

@non_negative(1)
def makelist(value, size):
    return [value] * size