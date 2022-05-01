# tuples are immutable sequences or arbitrary objects

t = ("Hungary", 36)

# to access an element we index

country = t[0]
countrycode = t[1]

# to concatenate we use the "+" operator
# only tuples to tuples can be concatenated!
expanded_t = t + ("Hungarian", "Europe")

# we can also repeat a tuple

repeated_t = t * 3

# tuples can have tuples in them, we just index twice

nested = ((1, 2), (3, 4))

one = nested[0][0]

# we can create single element tuples, this is done by the trailing comma operator - as a regular paren would be just an expression

single_tuple = (123,)

# we can make empty tuples, just use

empty = ()

# we can often even omit the parens, just do

omit = 1, 2, 3, 4, 5

# this can also be used to return multiple values from a function, e.g.

def minmax(items):
    return min(items), max(items)

# will yield (1, 4) for the input [1, 2, 3, 4]

# tuples can be deconstructed / unpacked into named values

minval, maxval = minmax([1, 2, 3, 4])

# now minval is 1, maxval is 4

# unpacking also works with nested tuples

(a, (b, c)) = (1, (2, 3))

# we can use this to flip variable values

a = "foo"
b = "bar"

a, b = b, a # now foo and bar are flipped

# we can make tuples from anything than can be iterated over

fromlist = tuple([1, 2, 3, 4])

# we can use the "in" operator to check for contains

5 in (1, 3, 5, "apple") # evals to True

2 not in (1, 3, 5, 7) # evals to True