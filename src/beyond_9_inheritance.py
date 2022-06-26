# as discussed earlier python can do inheritance
# per basics_10_polymorphism and beyond_5_inheritance

# python can do multiple inheritance

class BaseClassA:
    pass

class BaseClassB:
    pass

class ChildClass(BaseClassA):
    pass

# python type check via isinstance()

isinstance("asd", str) # will be True

# we can supply a tuple of stuff to check if instance of any
x = []
isinstance(x, (float, dict, list)) # will be true due to x being a list

# python subclass check via issubclass()
issubclass(ChildClass, BaseClassA) # will be True


# let's make a multiple inheritance class
class MultiClass(BaseClassA, BaseClassB):
    # no conflicts in names are no issue
    # if there is a conflict, we get the 'Method Resolution Order' or MRO
    pass

    # for calling init of base classes, multi inheritance classes only call the first one's

# dunder bases is a tuple of base classes

# so let's talk MRO
# dunder mro stores mro for an object (list of base classes pretty much in order)
# MRO will look at base classes in order until it finds a match and calls it

# super() actually calls the next resolved method per MRO, not the base class
# hence in multiple-inheritance method-name collision cases, super() in base A will call into base B even if base A does not inherit base B

# class-bound super proxies
super(BaseClassA, MultiClass) # will yield MRO results from after BaseClassA, so here builtin.object only (can only call static stuff on it)

# instance-bound super proxies
ic = MultiClass()
super(BaseClassA, ic) # will yield instance of MRO after BaseClassA, so builtin.object in our case (but now we can call instance methods on it, e.g. .foo() if builtin.object would have that)

