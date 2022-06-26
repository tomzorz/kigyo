
class ParentClass:

    @staticmethod
    def _static_sample():
        print("I'm static parent")

    @classmethod
    def class_sample(cls, *args, **kwargs):
        print("made via parent named ctor")
        return cls(*args, **kwargs)
        # we can use the above to call parent class defined named ctors call into a child class's main ctor that expects params


class ChildClass(ParentClass):

    # in python we can overwrite static methods in child classes
    @staticmethod
    def _static_sample():
        print("I'm static child")

    def __init__(self, data):
        # in python base class ctors are not called automatically, so we need to use super
        super().__init__()

    # this design also means that we can set data from outside of childclass


# this works regularly
child_regular = ChildClass("data")

# this also works with passing stuff along
child_via_parent = ChildClass.class_sample(data = "data")