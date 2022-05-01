# the context manager protocol

# it's kinda like IDisposable in c#
# instead of "using" we have "with"

with open("cm.dat", mode="at", encoding="utf-8") as cmf:
    cmf.writelines(["foo\n", "bar\n"])

# this will close the file at the end of the "with" block

# the CM protocol's method is "dunder exit"
# so in a custom class we'd have to add "__exit__()"
# we also have a method for entering, called "dunder enter"

# we can also have a "closing()" method, and use
from contextlib import closing

class UsesCM:
    def something(self):
        pass

    def close(self):
        pass

def use_sample():
    with closing(UsesCM()) as ucm:
        ucm.something()


use_sample()
