'''
fobj=open("a1.txt",'w')
l1=[]
for i in range(3):
    names=input("enter a name")
    l1.append(names+'\n')
    
fobj.writelines(l1)
fobj.close()
    
-------------------------

fobj=open("a.txt","r")
d=fobj.readlines()
d.reverse()
fobj.close()

f=open("a.txt",'w')
f.writelines(d)
f.close()

---------------------------

fobj=open("a1.txt",'r')
print(fobj.read(23))
print(fobj.readlines())
print(fobj.read(4))
-----------------------------

fobj=open("a1.txt",'r+')
print(fobj.read(5))
fobj.write("Sunday")
fobj.close()
------------------------------
#to count the occurance of E and e in text file
countE=0
counte=0
f=open("a1.txt",'r')
data=f.read()
print(data)
for i in data:
    if i=="E":
        countE+=1
    elif i=="e":
        counte+=1

print(countE)
print(counte)
f.close()    
--------------------------------------
fobj=open("a.txt","r")
d=fobj.read().split()
for i in d:
    word=""
    for j in range(len(i)-1,-1,-1):
        word+=i[j]
    print(word,end=" ")    
fobj.close()
-----------------------------

fobj=open("a.txt","r")
data=fobj.readlines()
d=[]
for i in data:
    d=i.split()
    if(len(d)>6):
        print(i)
    d=[]

-------------------------
'''
fobj=open("a.txt","r")
data=fobj.readlines()
print("no. of lines",len(data))
c=0
for i in data:
    if i[0]=='p':
        c+=1
print(c)    
