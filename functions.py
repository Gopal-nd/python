def hello():
    print("Hello World!")

hello()

def sum(a=0,b=0):
   return(a+b)

res = sum(1,2)
print(res)

def add(a=0,b=0):
    print(a+b)


add()

# multipltr  arguments

def multiple(*args):
    print(args)
    print(type(args))

    # type rettun will be tuople

    # **args for type dictyinory and you need to put argfuments in th e form of dict construction