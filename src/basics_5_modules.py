"""Module docstrings should be placed at the immediate beginning of the module

Usage:
    do thing
"""

# a source code file is often called a module

# these can be imported by just using the filename without the extension

# module code is only executed once on the first import

# it's good practice to always have executable code in your modules for testing, and always separate out main code, like so...

def main():
    # to do
    return None

if __name__ == "__main__":
    main()

# PEP-8 recommends one line breaks for logical breaks, and 2 line breaks between top level functions

# technically PEP-257 is the recommendation for documentation but it's not really adopted apparently

def something(arg):
    pass


def sample(arg):
    """Does something with an argument than returns it

        Args:
            arg: the argument

        Returns:
            The argument passed in
    """
    something(arg)
    return arg