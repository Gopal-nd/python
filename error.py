x=2
try:
    print(x/1)
    if not type(x) is str:
        raise TypeError("only Strings are allowed")
except NameError:
    print("There is an Error in Naming")
except ZeroDivisionError:
    print("cannot divide by zero")
except Exception as error:
    print(error)
else:
    print('no error')
finally:
    print("i an going to print without an error")

    

