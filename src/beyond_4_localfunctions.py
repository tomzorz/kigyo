# we can define functions inside functions

# their scope will be limited

def sort_by_last_letter(s):
    # and also this will be defined / re-created with every call to sort_by_last_letter
    def last_letter(s2):
        return s[-1]
    return sorted(s, key=last_letter)

# like lambdas except: multiple expressions and statements

# we can of course return local functions from functions

def outer():
    def inner():
        pass
    return inner

