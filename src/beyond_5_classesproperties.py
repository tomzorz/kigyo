
class ContainerClass:

    staticprop = 1337

    # read this after reading dunder init
    # staticmethod decorator marks a static method
    @staticmethod
    def _get_next_serial():
        result = ContainerClass.staticprop + 1
        ContainerClass.staticprop += 1
        return result

    # classmethod decorator marks a class method
    @classmethod
    def _get_other_serial(cls):
        # convention is to use cls as Class param
        pass

    # we can use this to call a named alternative ctor, e.g.
    @classmethod
    def create_empty(cls):
        return cls("")

    def __init__(self, data):
        self.data = data
        self.instanceprop = ContainerClass._get_next_serial()
        # this line above is BROKEN if we were to inherit from this class and override _get_next_serial()
        # so there's a valid reason to still call static methods via self.static...
        # as that'll eval to the child override if it exists, which is what we'd probably expect


        # self is needed for instance
        # ClassName is needed for static

        # while reading a static attribute with self.attrib works
        # it's important NOT to write to one like that, as that'd create a new instance attribute
        # that'll hide the static one