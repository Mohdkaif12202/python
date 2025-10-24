# in string the indexing start from zero to (lenght -1)
# And reverse indexing start from -1 
a = "world" # in python a single charter like "d"  is also consider as the string which has lenght of 1 but in c or c++ a single is consider as the single charter 
print((a[2:4])) 
# This is the silcing of the string
# syntax == [staring_index(it's include the value) : ending_index(It's not include the value)]
print((a[:3])) # a[:3] staring value is consider is 0 by defalut
print(a[2:]) # a[2:] ending value is consider as last

#==================================================================

# slicing of string by skiping the value

# syntax == [staring_index(it's include the value) : ending_index(It's not include the value):skping value]
f ="thisistuhkhgy"
print(f[:10:2])