
# properties are a thing YAY

class PropertyHolder:

    # property decorator, yay
    @property
    def celsius(self):
        return self._celsius

    # through some magic, the celsius method is now replaced with a non-method thing that acts like a getter

    # this is only a getter though, if we want a setter, we have to do that separately.
    # it's also done via the already set up property getter

    # getter.setter
    @celsius.setter
    def celsius(self, value):
        self._celsius = value


    def __init__(self):
        self._celsius = 0.0

    # overriding property getters is straightforward, we just redefine the property
    # overriding setters is harder...



class ChildOverrideHolder(PropertyHolder):

    # so this is a valid way of doing it, except if we want to use additional logic from the parent or something

    @PropertyHolder.celsius.setter
    def celsius(self, value):
        self._celsius = value
        # super() doesn't work here!

    # the recommended way is for the parent setter to call into an internal _set_property(value) method
    # and then in the child class we can override only that _set_property(value) method (and easily call super())