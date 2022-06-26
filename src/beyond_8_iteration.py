# multi input comprehension

l = [i * 2 for i in range(10)]

# we can use many inputs and if clauses

# later fors are nested in earlier ones
coords = [(x, y) for x in range(5) for y in range(3)]

values = [x / (x-y)
          for x in range(50)
          if x > 50
          for y in range(100)
          if x-y != 0]

# we can go meta

vals = [[y * 3 for y in range(x)] for x in range(10)]

# set/dict/generator work all the same


# and now, map (c# select)

unicodepoints = map(ord, 'árvíztűrő tükorfúrógép')

# map() is lazy, only does things on iteration

# map takes any args, function first and any other following ones are func args

def add(a, b):
    return a + b

l1 = [1, 2, 3]
l2 = [4, 5, 6]

sums = list(map(add, l1, l2)) # [5, 7, 9]

# map will terminate as soon as any input terminates



# and now, filter (c# where)

# filter(func, list)
# we can use lambdas yay

positives = filter(lambda x: x > 0, [-1, -2, 0, 2, 3]) # 2, 3



# and now, functools.reduce() (c# aggregate)

# repeatedly apply function until single result remains

from functools import reduce
import operator

total = reduce(operator.add, [1, 2, 3, 4, 5])

# empty input results in fail, can pass a 3rd argument as default initial


# and now, our own iterables

# first iter() is called to create, then next() for items, next will raise StopIteration when it runs out

# iterable is anything that implements dunder iter

# alternatively, dunder getitem for consecutive integer indexing

# iter(callable, sentinel), this stops when callable yields the same as sentinel