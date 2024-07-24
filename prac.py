'''
s="Hi i am done with do in a do will and done deal"
print(len(s))
list1=list(s)
print(len(list1))
count=0
for i in range(len(s)):
    list1.append(" ")
    if list1[i]+list1[i+1]=="do":
        count+=1


print(count)        
     
--------------------------------------------
d={"ala":23,"bb":90,"hi":"nope"}
for i in d:
    
    if type(d[i])!=int:
        print(i)
'''
l=[1.2,3,5,67]
print(l)
print(l[1::-1])
