# also known as, duck typing
# sad me noises

# no inheritance or interfaces
# we only learn if something will break during runtime
# BIG SAD

# python uses "late binding"
# inheritance in python is mostly used to share implementation between classes

class ClassBase:
    def commonMethod(self):
        pass

class Foo(ClassBase): # in python we define inheritance by adding "(ParentClass)" right after the class name
    pass

class Bar(ClassBase):
    pass


