import inspect
import beyond_10_collections

# so this is python's name for reflection

# in python both "object" and "type" are circular subclasses of each other

# direct comparison of type objects is not recommended
# but type() gets us them.
# it's like c# obj.GetType() (as typeof() works on classes)

# dir() gives us attributes
# methods are attributes, just callables

i = 1337

type(i) # class int

dir(i) # int's attributes

conjm = getattr(i, "conjugate")

callable(conjm) # true

i.conjugate.__class__.__name__ # builtin_function_or_method

# getattr can throw AttributeError
hasattr(i, "index") # False

# internally hasattr uses an exception, so just YOLO call things and handle with an exception - it's the faster way
# [sad static typing noises]

globals() # dictionary of the global scope
# we can add stuff to it, as if we'd be defining a variable

locals() # here it's the same as globals

def my_method(arg):
    x = 1234
    locals() # here it'll have arg and x
    pass

# this is how format and method args work

inspect.ismodule(beyond_10_collections)

inspect.getmembers(beyond_10_collections, inspect.isclass)
# this is basically reflection for just classes in an assembly BUT this will include anything that was imported
# without an easy way of stopping it

inspect.getmembers(beyond_10_collections.SampleCollection, inspect.isfunction) # gets all methods in a class

init_sig = inspect.signature(beyond_10_collections.SampleCollection.__init__) # this is a signature object
init_sig.parameters # list of method params!