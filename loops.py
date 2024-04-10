# value = 1
# while value <=10:
#     value+=1
#     if value == 5:
#         continue
#     print(value)


# value = 1
# while value <=10:
#     value+=1
#     if value == 5:
#         continue
#     print(value)
# else:
#     print('value is more than expected')

# for loop mainly uses for known number specific typw

classes = ['studednts','techers','staff','me']
for i in classes:
    print(type(i))
    print(i)

for i in "jfdnbvjihui efcjdio":
    print(i)
    if i == "o":
        break
for x in range(7):
    print(x+1)
for i in range(2,6):
    print(i)


for i in range(0,1000,100):
    print(i)

name = ['ram','sham','boos']
action = ['write','read','sleps']
for name in name:
    for act in action:
        print(name+" "+act+"!")