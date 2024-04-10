# Ditionaries
band = {"vocal": "palnts", "geture": 12}
band2 = dict(planr="the", most=33)

print(band)
print(band2)

# accessing the value using key
print(band["geture"])
print(band.get("vocal", "geture"))

  #list all values
print(band.keys())

#list all the valurs
print(band.values())

#list in the form of key / value paresd
print(band.items())

print("me"in band)
band['geture'] = 34
band.update({'boss':'shiva'})

#remove iotems
print(band.pop('boss'))
print(band)

band.popitem() # cleare the ladt added item

#delete and cleare 
band["mass"]='garvity'
del band["mass"]
print(band)

band.clear()
print(band)

# copying the dictinory

band2 = band.copy()
band2['mee']='to do'
print(band)
print(band2)

 #nessted dictinory

print('List of students made recore in class test')

student1 = dict(name='student1',age=19)
student2 = dict(name="student2",age=20)

classTopers = {
    "first":student1,
    "second":student2
}

print(classTopers["first"]['name'])