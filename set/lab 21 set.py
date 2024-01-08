# COMMON SET OPERATIONS
# Using union(), intersection() and difference() functions.

a = {2, 4, 5, 9}
b = {2, 4, 11, 12}
# print(a.union(b))  # Values which exist in a or b
# output {2, 4, 5, 9, 11, 12}
# print(a.intersection(b))  # Values which exist in a and b
# output {2, 4}
# print(a.difference(b))  # Values which exist in a but not in b
# output {9, 5}

# The union() and intersection() functions are symmetric methods:
#
a.union(b) == b.union(a)

a.intersection(b) == b.intersection(a)
True
a.difference(b) == b.difference(a)
False

# If the list values are all integer types,
# use the map() method to convert all the strings to integers.
#
# mm = [5, 4, 3, 2]
# #This code first converts the list mm to a string
# # representation (lis) using join and map functions.
# lis = ' '.join(map(str, mm))
# # the split() method on the string to create a new list (ll).
# ll = lis.split()
# print (ll)
# output = ['5', '4', '3', '2']
#
# newlis = list(map(int,ll))
# print (newlis)
# output = [5, 4, 3, 2]

# CREATING SETS

# myset = {1, 2}# Directly assigning values to a set
# myset = set()  # Initializing a set
# myset = set(['a', 'b']) # Creating a set from a list
# print(myset)
# {'a', 'b'}


# MODIFYING SETS

# Using the add() function:

# print(myset.add('c'))
# print(myset)
# # output = {'a', 'c', 'b'}
# print(myset.add('a')) # As 'a' already exists in the set, nothing happens
# print(myset.add((5, 4)))
# print(myset)
# output = {'a', 'c', 'b', (5, 4)}

# Using the update() function:

# myset.update([1, 2, 3, 4]) # update() only works for iterable objects
# print(myset)
# # {'a', 1, 'c', 'b', 4, 2, (5, 4), 3}
# myset.update({1, 7, 8})
# print(myset)
# # {'a', 1, 'c', 'b', 4, 7, 8, 2, (5, 4), 3}
# myset.update({1, 6}, [5, 13])
# print(myset)
# {'a', 1, 'c', 'b', 4, 5, 6, 7, 8, 2, (5, 4), 13, 3}

# REMOVING ITEMS

# Both the discard() and remove() functions take a single value as an argument and
# removes that value from the set. If that value is not present, discard() does nothing,
# but remove() will raise a KeyError exception.

# myset.discard(10)
# print(myset)
# # {'a', 1, 'c', 'b', 4, 5, 7, 8, 2, 12, (5, 4), 13, 11, 3}
# myset.remove(13)
# print(myset)
# # {'a', 1, 'c', 'b', 4, 5, 7, 8, 2, 12, (5, 4), 11, 3}


# def return_diff(s1, s2):
#     [print(i) for i in sorted(list((s1 ^ s2)))]
#
#
# if __name__ == '__main__':
#     n = int(input("jj"))
#     set1 = set(map(int, input("ii").split()))
#     n1 = int(input("hh"))
#     set2 = set(map(int, input("gg").split()))
#     return_diff(set1, set2)

a = {2, 4, 5, 9}
b = {2, 4, 11, 12}

# The following statement is always true:
a.union(b) == b.union(a)
print(a.union(b))
print(True)
print(False)
