'''
list2=[30,67,56,[78],34,56,46,70]
print(list2[3])
list3=[30,67,56,[78,67],34,56,46,70]
print(list3[3])
list3.append([34])
print(list3)
----------------------------------------
str1=input("enter a string")
l1=list(str1)
countv=0
countc=0
for i in l1:
    if i in "AEIOUaeiou":
        countv+=1
    elif i==' ':
        pass
    else:
        countc+=1

print("vowel=",countv)
print("consonant=",countc)
----------------------------------------------

print("123"<"Hello")

------------------------------------------
s="hello"
s=s+"bye"
print(s)
--------------------------------------------

for i in range(1,1):
    
    print(i)
    for j in range(0,i):
        print("hello")
-----------------------------

l1=eval(input("enter"))
print(l1)#prints in tuple by default

------------------------------
for i in range(4,10):
    print(i,sep="#")
------------------------------
d1={1:23,2:34,24:67}
d2=d1.copy()
d1[2]=89
print(d1)
print(d2)
print(d1.keys())
print(d1.values())
print(d1.get(2))
---------------------------------
import random
print(random.randint(12,8))#value error
------------------------------
S="THANK YOU"
S=S+"YOU"
print(S)
---------------------

def fun():
    n=10

fun()
print(n)
----------------

s="ShakESpHerE"
m=""
for i in range(0,len(s)):
    if s[i].islower():
        m+=s[i-1]
    elif s[i].isupper():
        if s[i]=='S':
            m+='X'
    elif(s[i]=="E"):
            m+=s[i-1].upper()
    else:
            m+=chr(ord(s[i])-1)

print(m)            
-------------------

l=['CS','HINDI','PHYSICS','CHEMISTRY','MATHS']
n=5
for i in range (0,n):
    if len(l)>4:
        l[i]=l[i]+l[i]
    else:
        l[i]=l[i]

print(l)
---------------------------

a=30
def call(x):
    global a
    if a%2==0:
        x+=a

    else:
        x-+a

    return x

x=20
print(call(35),end='#')
print(call(40),end='@')
--------------------------

def makenew(mystr):
    newstr=""
    count=0
    for i in mystr:
        if count%2!=0:
            newstr+=str(count)
  
        else:
            if i.lower():
                newstr+=i.upper()
            else:
                newstr+=i

        count+=1
    print(newstr)
makenew("No@1")
-------------------------
#prints on the same line the two sentences
print("hey how you doing \
noice")
#again prints on same line and without any space heynice
print("hey" \
      "nice")
----------------------------
#prints2e+31--higher number scientific notation
a=20e30
print(a)
----------------------------

#sep
print("a",sep="$")
print("b")
#end
print("a",end="$")
print("b")
'''
#both sep and end
print("a","c",sep="$",end="")
print("b")

