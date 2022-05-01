# unordered collection of unique elements

# sets are mutable, but their items are immutable

# to make one quickly, we can do
s = {1, 2, 3, 4}

# as empty {} makes an empty dictionary, we need to use the set ctor to make an empty set
empty_set = set()

# we can use the ctor to create one from any iterable, duplicates are discarded
unique_nums = set([1, 1, 2, 2, 3, 3]) # yields {1, 2, 3}

# we can again use the "in" and "not in" operators to test for membership

# to add an element use the set.add(item) call, if it exists nothing happens

s.add(5) # {1, 2, 3, 4, 5}
s.add(1) # {1, 2, 3, 4, 5}

# to add multiple elements, use the set.update() method

# to remove an element use set.remove(item)

s.remove(5) # {1, 2, 3, 4 }

# if we call this again, we'll get a KeyError if it doesn't exist
# there is a gentle version, called set.discard(item) which won't error out if the element doesn't exist

s.discard(5) # nothing happens, but it's okay

# to create copies we can use set(old_set) or old_set.copy()

# sets have a bunch of intersection calls, they are very useful
# a.union(b), a.intersection(b), a.difference(c) and even a.symmetric_difference(b) which is basically NOR (either in A or B but not both)

# we also have a.issubset(b), so everything in a is in b
# and a.issuperset(b), so everything in b is in a
# and finally a.isdisjoint(b) to see if a and b have nothing in common