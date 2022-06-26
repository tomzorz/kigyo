import contextlib
from contextlib

# we've seen the basics_11_contextmanager

# with context-manager as x:
#     context-manager.begin()
#     body
#     context-manager.end()

# we'll refer to the 2 methods as Enter and Exit
# could be allocate / deallocate, setup / teardown and others...

# so while originally we said it's like IDisposable
# it has more common uses in python

# see example above
# 1. context-manager expression is evaluated, this has to return a context-manager interfaced callable
# 2. dunder enter is called without arguments:
# - if throws an exceptions we End here
# - if it doesn't we continue
# - if it returns a value, it'll be bound to x
# 3. expression body is called
# 4. dunder exit is called afterwards
# - if the expression body had no exceptions we get no arguments
# - if it did have exceptions the exception information gets passed along

class MyContextManager:
    def __enter__(self):
        print("CM enter")
        return "you're in a CM"

    def __exit__(self, exc_type, exc_val, exc_tb):
        print(f"CM exit: {exc_type}, {exc_val}, {exc_tb}")
        return

with MyContextManager() as x:
    print(x)
    raise Exception("welp")


# typical CMs return themselves on dunder enter

# typical CM exits are responsible for clean up
# they also re-raise exceptions to propagate them along
# if dunder exit returns False, the exception is propagated

class MyTypicalContextManager:
    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        if exc_type is None:
            return True
        else:
            print(f"CM exit: {exc_type}, {exc_val}, {exc_tb}")
            return False

# this also means, we should just return False and NEVER explicitly re-raise an exception
# so only raise an exception when something goes wrong within the dunder exit itself

# PEP-343 describes what exactly is happening with the with statement

# contextlib package helps us with with, ha ha

@contextlib.contextmanager
def my_context_manager():
    # ENTER
    try:
        yield True # enter return value
        # regular EXIT
    except:
        # exceptional EXIT
        raise # if we don't do this, we will swallow the exceptions (so this is kinda the opposite of the built-in way)

with my_context_manager() as y:
    pass

# we can use multiple context managers:
with my_context_manager() as a, my_context_manager() as b:
    pass
# same as
with my_context_manager() as i:
    with my_context_manager() as j:
        pass
# exceptions propagate throughout as expected

# don't pass a list of context managers as a context manager.
# use line continuation if needed
with my_context_manager(), \
    my_context_manager(), \
    my_context_manager():
    pass