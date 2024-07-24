fobj=open("a.txt",'w')
n=int(input("How many lines do we want to enter"))
for i in range(n):
    name=input("Enter name")
    fobj.write(name+'\n')

fobj.close()
