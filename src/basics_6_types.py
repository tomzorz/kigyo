# types are only evaluated at runtime

def add(a, b):
    return a + b

add(1, 2) # returns 3
add("foo", "bar") # returns "foobar"

add(42, "answer") # this will yield a TypeError - python generally doesn't do implicit type conversions (except for if/while bool expressions)