
# bytes are kinda like strings, except we have bytes instead of unicode code points
# kinda like char[] in c#? or byte[]

# to make one
bytes = b"data"

# they support most of the same operations as strings
data = b"foo bar"
data.split() # this will yield [b"foo", b"bar"]

# to move to/from strings we need an encoding

hungarian = "Árvíztűrő tükörfúrógép"
hudata = hungarian.encode('utf8')
backtohungarian = hudata.decode('utf8')