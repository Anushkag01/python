'''
v=25
def Fun(Ch):
    v=50
    print(v,end=Ch)
    v*=2
    print(v,end=Ch)
    print(v,end="*")

Fun("!")
print(v)
---------------------------------
d1={"A":23,'a':34,"b":56}
print(d1.values())
print(d1)
-------------------------
str1="Immediately"
print(str1[8:12]) #here no out of bounds error will be printed
-----------------------------------
'''
#tocheck whether prime or composite

num=int(input("Enter a number"))
count=0
for i in range(num+1):
    for j in range(i):
        if((i*j)==num):
            count+=1

if (count==1):
    print(num,"is the prime Number")
elif(count>1):
    print(num,"is the composite Number")
else:
    print(num,"neither prime nor composite")
'''
--------------------------------------------------

t1=(1,2,3,4,5)
t2=(34,56,7,78)
print(t1+t2)
-----------------------


for i in range(1,10):
    print()
    for j in range (1,10):
        print(i*j,end='\t')
        

---------------------
print((0.1+0.2)== 0.3) #output False
---------------------
#list half value swapped
l1=[]
l=[23,45,67,865,754,3544,22,3,5]
n=len(l)
num=int(n/2)
l1=l[num:]
l2=l[ :num]
l3=l1+l2
print(l3)
-------------------------


l=[23,45,67,865,754,3544,22,3,5]
for i in range(len(l)-1,-1,-1):
    print(l[i])

-------------------------------
#term2 question8 of cbse 2021

Novowel=[]
def PushNV(N):
    
    for i in N:
        word=""
        for j in i:
            if j not in "AEIOUaeiou":
                word=word+j
            else:
                word=""
            if word==i:
                Novowel.append(word)
    flag=True        
    while flag==True:
        if Novowel==[]:
            print("Empty Stack")
            flag=False
            
        else:
            print(Novowel.pop(),end=" ")
                

All=[]
e1=input("enter a string")
e2=input("enter a string")
e3=input("enter a string")
e4=input("enter a string")
e5=input("enter a string")
All.extend([e1,e2,e3,e4,e5])
PushNV(All)    
----------------------------------------

#term2 question8 of cbse 2021

only3_5=[]
def Push3_5(N):
    for i in N:
        if i%3==0 or i%5==0:
            only3_5.append(i)
            
    flag=True        
    while flag==True:
        if only3_5==[]:
            print("Empty Stack")
            flag=False
            
        else:
            print(only3_5.pop(),end=" ")


Num=[]
e1=int(input("enter a Integer"))
e2=int(input("enter a Integer"))
e3=int(input("enter a Integer"))
e4=int(input("enter a Integer"))
e5=int(input("enter a Integer"))
Num.extend([e1,e2,e3,e4,e5])
Push3_5(Num)
-------------------------------------------------------
import math
print(math.pow(2,3))
---------------------------
#to check for palindrome word in sentence
string="Hello madam do you speak malayalam"
list1=list(string.split())
count=0
word=''
for i in list1:
    word=''
    if i.isalpha():
        for j in range(len(i)-1,-1,-1):
            word+=i[j]

        if word==i:
            count+=1
            print(i)

print(count)            
            
-------------------------------------

#stack
print("..................MENU..............")
print("................1.PUSH..............")
print("................2.POP...............")
print("................3.DISPLAY...........")
print("................4.EXIT..............")
 
def push(stck):
    roll=int(input("Enter your roll number"))
    name=input("Enter your name")
    marks=int(input("Enter your marks"))
    stck.append([roll,name,marks])
    print(stck)

def pops(stck):
    if stck==[]:
        print("The stack is empty ..Underflow condition")
    else:
        print("The Deleted item is: ",stck.pop())
    
def display(stck):
    if stck==[]:
        print("the stack is empty")
    else:
        print("The elements of stack are:")
        for i in range(len(stck)-1,-1,-1):
            print(stck[i])

stack=[]
while True:
    choice=int(input("Enter your choice"))
    if choice==1:
        print("Please enter the following details")
        push(stack)

    elif choice==2:
        pops(stack)

    elif choice==3:
        display(stack)

    else:
        break

-----------------------------------------------------------------
'''


    
    
            
    







 





















        
    
































