# functions are objects, can be passed around

# dunder call lets us call classes

class CallableSample:

    def __call__(self, *args, **kwargs):
        pass

    # args here is an array of passed arguments
    # kwargs is a dictionary of named arguments

    # if there are matched args they will be resolved into the formal argument list

    # this also means that "functions" can have methods

# dunder init is basically a callable as well, that acts as a constructor

# to check if something is callable just pass it to callable
cs = CallableSample()
callable(cs) # will evaluate to True


# we can use the *args and **kwargs to forward arguments

def trace(f, *args, **kwargs):
    print("args: ", args)
    print("kwargs: ", kwargs)
    result = f(*args, **kwargs)
    print("result: ", result)
    return result


int("ff", base=16)

trace(int, "ff", base=16)

# the *args can also be used to transpose table data

data = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

transposed = list(zip(*data))