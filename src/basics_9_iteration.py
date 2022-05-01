# iteration is like IEnumerable in c#

# iterable -> can be passed to iter() to create an...
# iterator -> can be passed to next() to get the next value in a sequence

eiterable = [1, 2, 3, 4]
eiterator = iter(eiterable)
next(eiterator) # gets you 1
next(eiterator) # gets you 2
next(eiterator) # gets you 3
next(eiterator) # gets you 4
next(eiterator) # throws a StopIterator exception

# we can use this to implement stuff, e.g.

def first(iterable):
    iterator = iter(iterable)
    try:
        return next(iterator)
    except StopIteration:
        raise ValueError("iterable is empty")

# this is neat... I guess I can make linq... kinda


# iteration tools are a thing

# itertools.islice() -> perform lazy slicing of any iterator

# from itertools import islice, count
# islice(some_neverending_iter, 1000) <- get first 1000
# count() is the never ending range()

# we also have any() and all()

# e.g.
any(x % 2 == 0 for x in range(0, 10)) # are there any even numbers from 0 to 9?

# we also have zip(), similar to c#, merge to iters into a tuple pairwise
one = [1, 2, 3, 4]
two = ['a', 'b', 'c', 'd']
for item in zip(one, two):
    print(item) # will print (1, 'a') then (2, 'b')...

# zip accepts any number of iterables