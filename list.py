users =['Dave','john','sara']
data = ['Dave',42,True]
print('Dave' in data)
emptyList = []

print(users[0])
print(users[0:])
print(users[-1])
print(users.index('sara'))
print(len(data))

users.append('Elesa')
users.insert(0,'Elesa')
users.extend(['jimmy','Robert'])

print(users)

users.remove("sara")
print(users)
users[1:2] =['save']
users.sort()
print(users)
users.sort(key=str.lower)
print(users)

users.reverse()
print(users)

nums = [12,432,34,45434,434,4]
nums.reverse()

print(nums)
nums.sort(reverse=True)
print(nums)

# methods to make a copy
numscopy = nums.copy()
mynum = list(nums)
mycopy = nums[:]

# tuples 
Mytuples = tuple(('dev',22,True))