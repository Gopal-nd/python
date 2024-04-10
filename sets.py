#Sets

num1 = {1,2,3,4,5,6,7}
num2 = set((1,2,3,4,5,6,67))

print(num1)
print(num2)
print(type(num1))
print(len(num2))

# no duplictes in set

num1 = {1,3,22,22,3,5,4,4,334,4,3,43,3}
print(num1)
num2 = {True,False,1,2,3,3,2,1,0}
print(num2)

# find for  keyword

print(3 in num2)
 # no indexing or no key for elemnets
 # adding a number 
num1.add(2222)
lists = [1,4,4,55,655,7646554,6565]
num1.update(lists)  # using update keyword we can add or update any data type example list ,tuple, dictionaries too
print(num1)

# use union to add sets

set1 = {1,2,3}
set2 = {4,5,6,7}
new =  set1.union(set2)
print(new)

# for duplecates
set1 = {1,2,3}
set2 = {1,3,7}
set1.intersection_update(set2)
print(set1)

# for non duplicates

set1 = {1,6,3}
set2 = {4,4,6,7}
set1.symmetric_difference_update(set2)
print(set1)