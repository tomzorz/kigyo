# lists are, well, lists

# we can index from the end using negative indices, this is neat
# and c# totally borrowed it haha

mylist = [1, 2, 3, 4]
last_item = mylist[-1] # will be 4

# -0 is same as 0, so negative indexing is essentially 1 based instead of 0 based!

# slicing is getting us portions

middle = mylist[1:3] # first element INCLUSIVE, last element EXCLUSIVE
# in this case, that's the same as
middle2 = mylist[1:-1]

# both start and stop positions are optional, they'll go to the start/end without
# omitting both is a handy way to create a copy of a list
copy_list = mylist[:]

# we can also copy by list.copy() or list(originallist)
# these are all of course shallow copies, the references inside are the same

# lists can also do the whole multiply operator, realistically it's used to get a list of X same value, e.g. to get [0, 0, 0, 0]
zero_list = [0] * 4 # but it's important to note that repetition will repeat the reference

# to find the index of something, use list.index()
second_list = [0, 1, 2, 3, 4]
index_of_2 = second_list.index(2)

# if the element is missing, you get a ValueError! (unlike in c# where you get -1)

# to remove an element from a list, use del list[index]
del second_list[2] # this is like c# list.RemoveAt(2)

# to remove by value, use list.remove(item)
second_list.remove(0) # also raises a ValueError if the item is missing!

# to add an element, use list.insert(item)
second_list.insert(0, 0)

# the + operator will create a new list
third_list = [1, 2, 3] + [4, 5, 6]

# the += operator will modify in place
third_list += [7, 8, 9] # also same as list.extend(otherlist)

# in-place modifications
third_list.reverse()
third_list.sort()

# sort accepts a named parameter "key" which is a callable function
["a", "ab", "cba", "aaaa"].sort(key=len) # this will sort by length

# there are non-in-place versions list.sorted() and list.reversed() (although reversed will create a reversed ITERATOR that we have to pass to a list ctor to make a list out of it)