d = {"name": "Alice", "age": 25, "city": "New York"}
print(list(d.values())) #print the all values in the form of dictnory
print(list(d.keys())) # print the all keys in the form of dictnory

# print the all value in the form of dictnory
for i in d.values():
    print(i)
# print the all keys in the form of dictnory
for i in d.keys():
    print(i)
# print the all keys-value pair in the form of dictnory
for i in d.items():
    print(i,"------------------")

# clear the dictionary
#     d.clear()

# it update the value of the any keys and add other key value pair in the dictnory
d1 = {"name": "k","gender":"m"} # change the name and add the gender key value pair
d.update(d1)
print(d)
print(d1)

#  it delete the any key and it's vlaue form diictnory
del d ["age"]
print(d.items())
d.popitem()

for i in range(7):
    print(i)