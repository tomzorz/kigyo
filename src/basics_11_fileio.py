# let's start at the basics

# use open() for reading OR writing

# 3 params
# "file" ! mandatory -> path to the file
# "mode" can be "read", "write", "append" plus "binary" or "text", combine the first letters for proper values, e.g. 'rb' or 'wt'
# "encoding" if in text mode, what encoding to use (if not specified, python will choose a default)

#
# +--------+
# |        | [ universal ] <-- encode() <-- write()
# | a file | [     .     ]
# |        | [  newlines ] --> decode() --> read()
# +--------+
#

import sys
sys.getdefaultencoding() # 'utf-8', is the default, usually...

# let's write some text
f1 = open("first.txt", mode="wt", encoding="utf-8")
f1.write("hello world") # there is no "writeline" in python, it's our responsibility to add a "\n" at the end if needed
f1.write(", this is python \n")
f1.write("foo bar")
f1.close() # important to close the file

# file.write() returns the number of codepoints written NOT the amount of bytes!

# now let's read some text
f2 = open("first.txt", mode="rt", encoding="utf-8")
f2.read(11) # read 11 codepoints, "hello world" in our case - this will yield a string, as we opened the file in text mode
f2.read() # will read the rest of the file
f2.read() # will yield an empty string after reaching the end of the file

# we can return to the beginning of the file (or Stream, as that's what this looks like from the c# world)
f2.seek(0) # Important that in text mode files, seek() can only go to 0 OR any value we get by the "tell()" method - any other values will result in undefined behavior

# thankfully python has nicer methods than reading X codepoints
f2.readline() # will yield "hello world, this is python\n"
f2.readline() # will yield "foo bar" -> end of file if no more newlines
f2.readline() # will yield an empty string after reaching the end of the file

f2.seek(0)

# we can read all lines into memory with
f2.readlines()
f2.close()

f3 = open("first.txt", mode="at", encoding="utf-8")
# there is no "writeline" in python, but there is...
f3.writelines(["first line\n", "second line\n"]) # BUT we have to provide our own line endings.
f3.close()

# file objects support iterator
f4 = open("first.txt", mode="rt", encoding="utf-8")
for line in f4:
    sys.stdout.write(line) # this is the same write as the file.write, it will not add an extra newline unlike print()
f4.close()

# to be nice, we should always use try-finally and close files in finally
try:
    f5 = open("first.txt", mode="rt", encoding="utf-8")
    for line in f5:
        sys.stdout.write(line)
finally:
    f5.close()

# in python we can return from a try block, the finally will be executed anyway


# now let's see binary files
# also at this point we're past "basics_11_contextmanager"

with open("thing.dat", 'wb') as thing:
    thing.write(b"THING") # let's write some magic bytes
    bookmark = thing.tell() # this gets us the current position in the stream
    thing.write(b"\x00\x00") # let's write 2 bytes of zero as a placeholder
    thing.write(b'some data bla bla bla')
    thing.seek(bookmark)
    thing.write(b"05") # use the bookmark to go back and write


# python has "file-like objects", these act like files but might not support all the methods we've seen above
# e.g. urllib request