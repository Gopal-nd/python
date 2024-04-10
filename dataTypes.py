import math 
# string data type
 # lityreal assignment

first = 'dev'
print(type(first))

#const6ructgpt functions

pizza = str('PER')
print(type(pizza))

mutliline = '''
hello this is an example of multiline 
    see how it works 
            i think it is good
            '''
print(mutliline)

#escasping special charecters

sentendce = 'I \' m back to work! \t Hey \n\n where \'s this at \\ located'
print(sentendce)

# string methods
print(sentendce.title())    
print(sentendce.replace('i','f'))
print(len(mutliline))
mutliline+= "";
mutliline= "                             "+mutliline
print(len(mutliline))

#build aa menu 
title = "menu".upper()
print(title.center(25,"="))
print("Coffee".ljust(16,'.')+"$1".rjust(4))
print("Tea".ljust(16,'.')+"$1".rjust(4))
print("ColdCoffee".ljust(16,'.')+"$1".rjust(4))
print("ChessCake".ljust(16,'.')+"$1".rjust(4))

# string index values
print(sentendce[0:13])
print(sentendce[-1])

# SOME METHODS remove boolean values
print(sentendce.startswith('I'))
print(sentendce.endswith('I'))

# Boolea values
myvalue = True;
x= bool(False)
print(type(x))
print(isinstance(myvalue,bool))

# with numbers 
price = 1000
best_price = int(90)

gpa = float(3.32)
print(abs(gpa))
print(round(gpa))
print(round(gpa,1))


print(math.pi)


# casting a string to a numbre 
zipcode = "562106"
zip=int(zipcode)
print(type(zip))
print(zip)