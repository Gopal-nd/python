
import os 
f= open("test.txt")
print(f.read())
print(f.readline())

for i in f:
    print(i)

f.close()

try:
    r=open("tes.txt")   
    print(r.read())
except:
    print('file donot exist')

a =  open("test.txt","a")
a.write("awesome!")
a.close()

a = open("test.txt")
print(a.read())
a.close()


# w ==> wil over write all th econtent w as super power  to ceate if th efile do not exist

w= open("new_file.txt","w")
w.write("This is the new file created by write")








# creaty a new file
# if not os.path.exists():
#     t = open("new.txt","x")
#     t.close()


# delete a file
if os.path.exists("new.txt"):
    os.remove("new.txt")
else:
    print("file do not exist to delete")


  # small Experiment
def create(num):
    for i in range(num):
        name = f"news{i}.txt"
        if not os.path.exists(name):
            t = open(name,"x")
            t.close()

def delete(num):
     for i in range(num):
        name = f"news{i}.txt"
        if  os.path.exists(name):
            os.remove(name)
        
            
# create(4)
delete(4)


# use files with keyword

