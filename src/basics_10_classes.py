# defining a class

# by convention, python uses CamelCase for class names
# "class" like "def" is a statement

class MyClass:

    def __init__(self, sample):
        # this dunder init is python's "constructor", BUT the object already exists when it's called, so it's an "initializer" - hence the name
        # we have to pass "self" to it first, but it can take other arguments after

        self._data = sample # we can just use anything here and it'll automagically get defined
        # important that in python we can't have params and methods with the same name
        # also convention calls that implementation details start with an _

        # these shouldn't return anything
        pass

    # in python, instance methods need a "hidden" first argument, that is called "self" by convention
    # this replaces "this" from c# and similar
    def ident(self):
        return "i am myclass " + self._data

    # calling methods from within the class always require the use of "self."

# there are no access modifiers in python
# oh well

# to create an instance, we call the ctor (without "new" !)
mc = MyClass("asd")
mc.ident() # notice how I don't need to pass in "mc" -> that's what I meant by hidden

# BUT we can do
MyClass.ident(mc) # which does the same as the above. although don't do this.

