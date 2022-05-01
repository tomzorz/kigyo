# generator functions

# iterables defined by functions
# uses the "yield" keyword

def gen123():
    yield 1
    yield 2
    yield 3

# we'll get StopIterator exception when we call next() on a gen123 instance the 4th time

# the code always executes until the next yield function, nothing runs by creating the generator function

# we can store state in generator functions

# a more complex example, will show off lazy evaluating too

def take(count, iterable):
    counter = 0
    for item in iterable:
        if counter == count:
            return
        counter += 1
        yield item


def distinct(iterable):
    seen = set()
    for item in iterable:
        if item in seen:
            continue
        yield item
        seen.add(item)


def run():
    items = [4, 8, 8, 2, 1, 1]
    for item in take(3, distinct(items)):
        print(item)


run()

# we can put a list() call anywhere, like c# .ToList() to exhaust an iterable

# generator expressions are also a thing, except we use () instead of [] or {}
# formula is: (expression(item) for item in iterable)
# so basically the same.

# e.g. to get the first 10000 square numbers
f10ksq = (i*i for i in range(1, 10001))

# f10ksq is right now just a generator reference, nothing has been evaluated yet
# we can make that happen with
results = list(f10ksq)

# important to remember that generators are single-use, if we want the results again we have to recreate them

# if we pass a generator expression into a function as a parameter, we can leave out the parens

# also important, that generator expressions are also capable of using filters