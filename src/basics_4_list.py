
# lists are mutable sequences of objects

l1 = [1, 2, 3]
l2 = ["foo", "bar"]

# it's okay to mix types
l3 = ["alice", 0, "bob"]

# an empty list
l4 = []

# to put something in it
l4.append("something")

# to make one out of text
l5 = list("text")
# this gets us ['t', 'e', 'x', 't']

# we can multi-line define
l6 = ["foo",
      "bar",
      "and",
      "more"]