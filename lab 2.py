# a = [1,2,3,4,5,6,48,78,95,64,25,12,15,23,1,52,5,2]
# a.sort()
# print(a)
#
#
#
# a = [1,2,3,4,5,6,48,78,95,64,25,12,15,23,1,52,5,2]
# m = sorted(a)
# print(m)
#
#
#
#
# my_list = [4, 1, 7, 3, 9, 2]
# my_list.sort()
# print(my_list)
#
#
#
#
# my_list = [4, 1, 7, 3, 9, 2]
# my_list.sort(reverse=True)
# print(my_list)
#
#
#
# my_list = [4,1,7,3,9,2]
# aa = sorted(my_list, reverse=True)
# print(aa)


# Tuple slicing

# my_tuple = [4, 1, 7, 3, 9, 2, 655,6,8,9,33,55,66,77,88,44,1000,5235,56985,512,888,756]
# subset_tuple = my_tuple[1:2000:2]
# subset_tuple.sort()
# print(subset_tuple)
# # Creates a new tuple (2, 'hello')
#
# # Tuple concatenation
# a = [8,9]
# new_tuple = my_tuple + a + ['hello',55]
# print(new_tuple)
# # Results in a new tuple (1, 2, 'hello', 3.5, 4, 5)
#
# # Step 1: Create Tuples
# tuple1 = (1, 2, 3)
# tuple2 = ('a', 'b', 'c')

#  Step 2: Concatenate Tuples
# concatenated_tuple = tuple1 + tuple2
#
# # Step 3: Display the Result
# print(concatenated_tuple)


# my_list = [1, 2, 3, 4, 5]
# my_tuple = tuple(my_list)
# print(my_tuple)


# a = "this parrot is dead"
# print(a[0:4])
#
# string = "Python"
# print(string[1:4])
# Output: yth


# name = input("enter your name ")
# age = input("enter your age ")
# formatted_string = "My name is {} and I am {} years old.".format(name, age)
# print(formatted_string)
# # Output: My name is Alice and I am 25 years old.


# string = "Hello, World!"
# print("World" in string)  # Output: True


# words = ["Hello", "World", "Python"]
# print(words)
# joined_string = " ".join(words)
# print(joined_string)
# Output: Hello World Python

# JOIN AND SPLIT (REVERSE)

# w = ['My', 'name', 'is', 'Alice', 'and', 'I', 'am', '25', 'years', 'old']
# nn = "My name is Alice and I am 25 years old"
# ss = nn[::-1]
# print(ss)
# jj = ' '.join(w)

# aaa = jj.split()[::-1]
# mm = ' '.join(aaa)
# print(mm)

# w = ['My', 'name', 'is', 'Alice', 'and', 'I', 'am', '25', 'years', 'old']
# jj = ' '.join(w)
# print(jj.split(" ")[::-1])
# print(jj.split("  ")[::-1])
# print(jj.strip())
# print(jj)
# print(jj.upper())
# print(w)
# print(" ".join(w))
#
# name2 = 'sangam ''singh'
# print(name2.upper( ))
# a = len(name2)
# print(a)


# capitalize

# a = "my name IS sangam"
# print(a.capitalize())

# casefold

# print(a.casefold())

# center method

# print(a.center(21,"@"))

# count

# a = "my name IS sangam sangam sangam "
# print(a.count("a",1,50))

# find
# aa = "my name IS sangam gsjd sdhfhgh vhfhfh sangam mgjgh bjgjg ghjffyfch"
# print(aa.find("sangam", 15,55))
#
# # endwith method
#
# str = "this is demo text. this is demo text2"
# print(str.endswith("text2",20,45))

# expandtabs() method

# str ="D\te\tm\to\t"
# print(str.expandtabs()) #expend 8 space autometically
# print(str.expandtabs(2)) #expend 2 space
# print(str.expandtabs(4))#expend 4 space

# #index method

# str = "this IS demo text this is demo text2"
#
# print(str.index('i'))
# print(str.index('i',6,44))

#
# # isalnum

# a = '245 raj'
# print(a.isalnum())

# str = "this IS demo text this is demo text2"
# q = str.lower()
# print(q)
# print(q.islower())


# a = "james bond007"
# print(a.isprintable())
#
# b = "this is demo.this is another demo demo demo "
# print(b.replace("demo", "text", -1))
# this is text.this is another text
#
# ss = "this is text.this is another text"
# print(ss.rfind("text",2,15))# last value position
# # output - 29
#
#
# #rejust
#
# str = "American vandal"
# print(str.rjust(25,"*")) # **********American vandal
# print(str.center(25,"@")) # @@@@@American vandal@@@@@
# # output - AAAAAAAAAAAmerican vandal

# str = "football, archary, cricket, squash, hockey, vollyball"
# print(str.rsplit(",",2))  # maxsplit start from zero
# #  output = ['football,archary,cricket,squash', 'hockey', 'vollyball']
#
# # rstrip() method
#
# str = "STRANGER THINGS#"
# print(str.rstrip("#")) # to remove special characters from the END
# # output = STRANGER THINGS

# splitlines()

# str = "one\n,two\n,three\n,four"
#
# print((str.splitlines(True)))
# # #output = ['one\n', ',two\n', ',three\n', ',four']
# #
# # print((str.splitlines(False)))
# # #output =['one', ',two', ',three', ',four']
# #
#
# # startswith

# str = "this is demo. this is another demo"
# print(str.startswith("other",2,100))
# #
# # #
# str2 = "this is demo. this is another demo"
# print(str2.startswith("is",2,100))
# #
# #
# # swapcase
# str2 = "this is DEMO. this is another demo"
# print(str2.swapcase())
# # OUTPUT = THIS IS demo. THIS IS ANOTHER DEMO
#
#
#
# name = "sangam"
# name1 = "yh"
# print(id(name))
# print(id(name1))
#
# m = name.lower()
# print(m)
#
# a = name.upper()
# print(a)
#
#
# # swapcase
# # return a copy of the string with
# # upper case characters converted to lowercase and vice versa
# aa = "kAlLu"
# b = aa.swapcase()
# print(b)
# print(name.swapcase())


# title

# returns a titlecased version of the string
# where words start with an uppercase character and
# the remaining characters are lowercase


# name = "hello world"
#
# print(name.title())
#
# name1 = "datta"
# print(len(name))
# print(len(name1))

# #replace
#
# name11 = "hello world"
# result_rep = name11.replace("world","python")
# print(result_rep)


# name11 = "hello my name is khan, but i am not a terrorist"
# result_rep = name11.replace("khan","sangam")
# print(result_rep)
#
# # INDEX AND LEN
# name = "raj"
# # len - starts from 1
# print(len(name))
# index - 0 to len-1
# r - 0, a-1, j - 2

# find()

# returns the lowest index of a substring in the string
# return -1 if the substring is not found

# text = "hello world"
# index = text.find("world")
# print(index)

# # count() - count the char-
# count = text.count("l",2,14)
# print(count)
#
# val = None
# print(val)
# print(type(val))
# print(id(val))
# print(len(val)) # None has no length - type error
#
# string = "i like %s" % "python"
# print(string)
# name = input("enter your name\n")
# print("your name is %s" % name)
#
#
# a = [1,2,3,4,3]
#
#
