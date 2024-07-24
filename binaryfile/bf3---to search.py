import pickle
#to write
fobj=open("myfile1.dat","wb")
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

#to search
f=open("myfile1.dat","rb")
rolln=int(input("Enter the roll no.to be searched"))
flag=0
r=pickle.load(f)
for i in r:
    if i[0]==rolln:
        print(r.index(i))
        flag=1
        break

if flag==0:
    print("element not found")
    
f.close()    
