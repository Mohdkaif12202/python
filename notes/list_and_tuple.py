# list are container to store a set of values of different data type
friends =  ["apple","akash",5,5.453, False] 
print(friends)
print(type(friends))

# list are mutable matlb jo change hoga wo original list me bhi change ho jayega 
friends[0] = "mango" 
print(friends)

print(friends[1:4])

#==================================================
# FUNCTION OF THE LIST

# 1 = l1.sort(): update the list to assending order (l1 means name of the list)
# defalut in ascending order
# for descending order : l1.sort(reverse=true)
# Sorting with a key function : 
words = ["apple", "banana", "cherry"]
words.sort(key=len)  # Sort by string length
print(words) # Output: ['apple', 'cherry', 'banana']

# 2 = l1.reverse() : updates the list to reverse form
# 3 = l1.append(value) : this function add the element in end of list
# 4 = l1.insert(index,value) : this will add the element in the any index of list
# 5 = l1.pop(index): this function delete the element by using the index in the list
# and usig : print(l1.pop(index)) it give the deleted item 
# 6 = l1.remove(element/value) : This function delete the element from list by using the element

lst = [10, 20, 30, 40, 20] # return the index of value 
print(lst.index(20))  # Output: 1

lst = [1, 2, 3, 2, 2, 4] # cout the element of list
print(lst.count(2))  # Output: 3

'''the short() meathod is use to sort the element in the list 
it sort by defaul in ascending order 
the data should have similar type data  in list'''
#syntax :>  list_name.sort(reverse="False") assending order
#syntax :>  list_name.sort(reverse="true") descending order


#================================================================================================================

# Tuple is an immutable data type in python it also hold the mix charcter value in tuple("hi", 4,4.5)
a=() #empty tuple
print(type(a))
b = (1,) # tuple with only one element needs a comma
c = (1,5,3,7,) # tuple with more than one element

# FUNCTION OF TUPLES

t = (10, 20, 30 ,20,) # unpacking = assigns tuple values to varibles 
a, b, c , _= t
print(a, b, c)  # Output: 10 20 30
print(t.index(30)) # return the index value
print(t.count(20)) # it count the value in tuple

t2 = (1, 2, 3, 4)# return the number of elements in a tuple
print(len(t2))  # Output: 4
print(t2*4) # repeats a tuple multiple time

t3 = (4, 7, 1, 9) # return the max and min number 
print(max(t3))  # Output: 9
print(min(t3))  # Output: 1


t = (0, 1, 2, 3, 4, 5) # slicing
print(t[1:4])  # Output: (1, 2, 3)
print(t[::-1]) # Output: (5, 4, 3, 2, 1, 0)  # Reversing the tuple

c=(lambda x: x % 2 and 'odd' or 'even')
print(c(4))