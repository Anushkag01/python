import pickle
#to write
fobj=open("myfile.dat","wb")
record=[] #for nested list
while True:
    roll=int(input("Enter a roll number"))
    marks=int(input("enter marks of student"))
    name=input("Enter name ")
    list1=[roll,marks,name]
    record.append(list1)
    choice=input("Do you want to continue?(Y/N)")
    if choice=='N':
        break

pickle.dump(record,fobj)
fobj.close()
'''
#to read
f=open("myfile.dat","rb")
r=pickle.load(f)
for i in r:
    print(i)    
fobj.close()
'''
#the above throws EOF Error, to overcome that we use try and except
f=open("myfile.dat","rb")
try:
    r=pickle.load(f)
    for i in r:
        print(i)
except EOFError:
    fobj.close()
    
    



