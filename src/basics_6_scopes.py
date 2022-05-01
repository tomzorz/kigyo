# there are 4 major scopes in python

# In order of how python will look for a reference:
# L - local, inside current function
# E - inside enclosing functions
# G - global
# B - in the builtins module

# scopes in python DO NOT correspond to source code blocks


# A confusing global example

count = 0

def show_count():
    print(count)

def set_count(c):
    count = c # this line here creates a new local variable called "count" which hides the globally scoped "count" variable

show_count() # print0 0 as expected
set_count(5) # ...
show_count() # prints 0... -> WTF, ok now see line 19

# to fix it

def correct_set_count(c):
    global count # we have to tell the compiler we mean the global count variable, "rebind the global name into a local namespace"
    count = c

# now the 3 lines above will do what we expect them to do