# ranges are an arithmetic progression of integers

r1 = list(range(5)) # gets us [0, 1, 2, 3, 4]
# same as range(0, 5)

# we can supply a step argument
r2 = list(range(0, 10, 2)) # gets us [0, 2, 4, 6, 8]

# range does NOT support keyword arguments

# we have "enumerate" if we need an index-value pair
# using range(len(list)) is "unpythonic"

t = ["foo", "bar", "asd"]
for p in enumerate(t):
    print(p) # this will print (0, "foo") then (1, "bar")

# we can also use tuple unpacking in the for syntax, this is kinda neat
for index, value in enumerate(t):
    print(f"[{index}] is {value}")


