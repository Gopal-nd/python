# sum = lambda a,d:a+d

from functools import reduce

# squre = lambda a:a*a

sums = lambda a,d:a+d
sqr = lambda a:a*a

# print(sqr(2))
# print(sum(1,2))

###############################

# used for quick functrions

def funcBuilder(x):
    return lambda a:a+x
add = funcBuilder(1)

add1 = funcBuilder(2)

print(add(1))
print(add1(3))

################################

# map function in pythons

numbers = [1,3,4,45,4,2,5,3,3,2,345,3434,23443]
squre= map(lambda num: num*num,numbers)
print(list(squre))

##############################

# filters in list 

odd = filter(lambda num : num%2!=0,numbers)
print(list(odd))

############################

num = [1,2,3,4,45,6,21]

total = reduce(lambda acc,curr:acc+curr,num)
total_v = reduce(lambda acc,curr:acc+curr,num,1000)

print(total)
print(total_v)

########## sum ############

print(sum(num))
print(sum(num,10))
