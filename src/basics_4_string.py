
# strings are immutable

# we can use single quotes and double quotes

s1 = 'hello'
s2 = "hello"

# this is useful to incorporate the other into a string

s3 = "that's me"
s4 = 'quoted saying "that is not me" yesterday'

# we can also put two strings next to each other and that's ok for some reason (wtf python moment 1)

s5 = "foo" "bar" # this will be "foobar"

# multi line strings

multi1 = """this
will
have 
line breaks
in it"""

multi2 = "this\nwill\n have\nline breaks\nin it"

# newline terminators will be automagically transformed to their platform appropriate ones, see PEP-278
# see python docs for all escape sequences, but it's relatively similar to C#

# we have raw strings, this is like c# @
path = r"C:\Windows\System32\drivers\afd.sys"

# we can also make strings out of other things

so1 = str(5)
so2 = str(5.6)

# strings are "sequence types"

sequence = "sequence"
sequence[0] # this is s

# important to note, there is no "char" equivalent in python, it's all strings

# strings are UTF-8 by default

# strings can be multiplied by ints to get them repeated
lines = '-' * 10 # will be ----------

# to find the length of a string, use the len() call

len("hello") # evals to 5

# to "modify" strings, I mean, to create new strings, we can

m1 = "add " + "them " + "together"
m2 = "add"
m2 += " them"
m2 += " together"

# for large concats use separator.join(strings)
# so for a comma separated list of numbers

numberlist = ", ".join([1, 2, 3, 4]) # will yield "1, 2, 3, 4"

# the other way we have str.split(separator)

numberlist.split(", ") # we'll get [1, 2, 3, 4]

# a useful new method is "partition", splits things by "before the separator", "the separator" and "after the separator"

"makkoshotyka".partition("hoty") # will yield the tuple ("makkos", "hoty", "ka")

start, _, end = "12:00-14:00".partition("-")

# string formatting, similar to c#
# field names can be omitted if we only use them once and in order
formatted = "{0} start, {1} end".format("12:00", "14:00")
fnamed = "positions is {lat} {lon}".format(lat = 47.2, lon = 19.8)

# we also have string interpolation, thank you PEP-498
interpolated = f"{'12:00'} start, {'14:00'} end"

# also similarly to c# we can do number formats, e.g. 3 decimal places

numberformat = f"{3.14157:.3f} is the value of pi"

# if we put "!r" after an expression, we get the REPL version of the object
