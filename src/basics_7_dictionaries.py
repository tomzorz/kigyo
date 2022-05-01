# dicts are at the heart of python

# keys are immutable, values are not

d1 = dict([("a", 1), ("b", 2)])

d2 = dict(a="alpha", b="beta", c="gamma")

empty_dict = {}

literal_dict = {
    "somekey": 1,
    "someotherkey": 2
}

# similarly to lists, copying is shallow
# we can use both dict.copy() or dict(originaldict) to do so

# to mass-add values from one dict to an other, call dict_to_be_updated.update(from_dict)
# if there are matching keys, the values will be updated

# to iterate we can just do
for key in d1:
    print(d1[key])

# or use dict.values() to only iterate on values (there's dict.keys() too)
# or we can do dict.items() to iterate on a Key Value tuple

# but important to note, that none of these are in a specific order

# we can use "in" and "not in" to test for keys
# and like lists we can use del to remove something, e.g.
del d2["a"]

# to quickly pretty print
from pprint import pprint as pp
pp(d2)