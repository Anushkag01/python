'''
QUESTION 1
Write a Python program that checks if a given non-negative
integer from the user, is a palindrome.
A palindrome is a number that remains the same when
its digits are reversed. For example, 121 is a palindrome
because it reads the same forward and backward, whereas 1231 is not a palindrome.

ANS:

n=int(input("Enter a non-negative number"))
n1=n
s=0
while n1>0:
    num=n1%10
    s=s*10+num
    n1=n1//10

if s==n:
    print("Number is a palindrome")

else:
    print("Number is not a palindrome")
    
-----------------------------------------------------
QUESTION 2
Write a program that takes number of rows ‘n’ as input
and prints the following pattern. For n=4, it is,
      1
      121
      12321
      1234321
ANS:

col=-1
n=int(input("Enter the number of rows"))
for i in range(n):
    count1=-1
    col+=2
    num=0
    for j in range(col):
        count1+=1
        if count1<=i:
           num+=1
        else:
            num=num-1
        print(num,end="")
            
    print()

------------------------------------------------
4
444
44444
4444444
444444444

ANS:easier way to solve than upper

n=4
for i in range(1,10,2):
    for j in range(i):
        print(n,end="")

    print()
-----------------------------------------------
QUESTION 3
Write a program that takes number of rows ‘n’ as
input and prints the following pattern, for
n=4, it is,
      ###1
      ##21
      #321
      4321

ANS:

n=int(input("enter the number of rows"))
num=0
col=0
for i in range(n,0,-1):
    count=0
    for k in range(1,i):
        count+=1
        print("#",end="")
    col=n-count
    num=col
    for j in range(col):
        print(num,end="")
        num-=1
    print()
    
---------------------------------------------------------
4)
Write a program that takes number of rows
‘n’ as input and prints the following pattern,
for n=4, it is,
1
10
101
1010


ANS:

n=int(input("enter the number of the rows"))
for i in range(1,n+1):
    for j in range(i):
        num=False
        if j%2==0:
            num=True  
        print(int(num),end="")

    print()

-------------------------------------------------
5)
Write a program that takes an integer 'n' as the number
of elements to be inserted inside a list.
Accept the integer elements for list from the user and
an integer 'k' as the desired occurrence frequency from the user.
The program should remove all elements that do not occur exactly 'k' times
within the list andprint the resulting modified list.
Eg: n=7, input_lst=[10,20,20,30,40,10,50], k=2 Output=[20,20,10,10]

ANS:

n=int(input("Enter the number elemenets to be inserted in the list"))
l1=[]
for i in range(n):
    n1=int(input("Enter element"))
    l1.append(n1)

k=int(input("Enter your desired frequency"))
l2=[]
while l1!=[]:
    count=0
    num=l1[0]
    for i in l1:
        if i==num:
            count+=1
    if count==k:
        for i in range(count):
            l2.append(num)
            
    for j in range(count):
        l1.remove(num)
          
print(sorted(l2,reverse=True))

---------------------------------
QUESTION 6: CHECK OUT AMAZING DO IT!!

Write a program that takes integer 'n' as the number of
elements to be inserted inside a list. Accept the integer elements for list,
and position 'k' from the user.
The program's objective is to find and display the kth smallest number from the list.
It is important to note that the numbers in the list may be repeated,
and a simple sorting approach may not yield the correct result. The program should
handle this case by considering the frequency of each number.
Eg1:-n=6, lst1=[20,7,15,16,7,8], k=3 output=15
Eg 2:- n=5,lst1=[5,4,19,9,18], k=8 output=None

ANS:
n=int(input("Enter the number of elements in the list"))
k=int(input("Enter the position value"))
num=0
l1=[]

for i in range(n):
    num=int(input("Enter the elements"))
    l1.append(num)

d={}
for i in l1:
    d[i]=l1.count(i)

l2=list(d.keys())
l2.sort()
if k>n:
    print("NONE")
else:
    print("OUTPUT:",l2[k-1])
---------------------------------------------------------------------------------------------------
QUESTION 7:
Write a program that takes integer 'n' as the number of elements to be inserted inside a list,
and the integer elements for list from the user.
Modify each element of a list by replacing it with the sum of the next two elements.
Assume the list is circular,
so the last element will be the sum of the elements at index[0] and index[1].
Eg1:-n=4,lst1=[1,2,3,4] output=[5,7,5,3]
Eg2: n=2, lst1=[100,200], output=[300,300]

ANS:
n=int(input("Enter the number of elements of the list"))
l1=[]
l2=[]
n1=0
for i in range (n):
    n1=int(input("Enter the element"))
    l1.append(n1)

for i in range(n):
    if i<n-2:
        n1=l1[i+1]+l1[i+2]
        l2.append(n1)
    
    elif i>=n-2 and i<n-1:
        n1=l1[n-1]+l1[0]
        l2.append(n1)

    elif i==n-1:
        n1=l1[0]+l1[1]
        l2.append(n1)
    

print("OUTPUT: ",l2)

---------------------------------------------------------
QUESTION 8:
Write a program that accepts a
square 2D list (nested list/like matrix) representing
a grid of integers from the user and prints
the average of the elements along the main diagonal of the 2D list(nested list).
Eg 1: row_ col= 3,
input_lst1=[[1,2,3],[4,5,6],[7,8,9]],
output= 5.0 (i.e. (1 + 5 + 9) / 3 =5.0)

ANS:
row_col=int(input("Enter the desired number of rows for 2-D list"))
l2=[]
n=0
for i in range(row_col):
    l1=[]
    for j in range(row_col):
        n=int(input("Enter the element"))
        l1.append(n)
    l2.append(l1)

num=0
s=0
for i in range(row_col):
    s+=l2[i][num]
    num+=1

print("OUTPUT:",(s/row_col))    

----------------------------------
QUESTION 9:CHECK OUT AMAZING DO IT!!

Write a program that accepts a square 2D list (nested list/like matrix)representing
a grid of integers from the user
and print the transpose of the 2D list(nested list/like matrix).
Eg 1:- row_col=2
input_lst1= [[1, 5],[2, 7]]
Output= [[1, 2],[5, 7]]

ANS:
l2=[]
l4=[]
n=int(input("Enter the number of rows"))
for i in range(n):
    l1=[]
    for j in range(n):
        num=int(input("Enter the element"))
        l1.append(num)
    l2.append(l1)

for i in range(n):
    l3=[]
    for j in range(n):
        l3.append(l2[j][i])
    l4.append(l3)
print("OUTPUT",l4)    
----------------------------------------
QUESTION 10:
Write a program that takes a sentence as input
and converts each alphabet in a given sentence to the next letter in the alphabet,
while preserving the case of the letters.
For example, a is converted to b, b to c, so on and z to a.
(ignore punctuations in the input sentence)
Eg: inp_str=”Welcome to python” output=”Xfmdpnf up qzuipm”

ANS:
s1=input("Enter a string")
s2=0
wrd=""
for i in s1:
    if i.isupper():
        if i!="Z":
            s2=ord(i)
            wrd+=chr(s2+1)
        elif i=="Z":
            wrd+="A"
    
    elif i.islower():
        if i!="z":
            s2=ord(i)
            wrd+=chr(s2+1)
        elif i=="z":
            wrd+="a"
    else:
        wrd+=i

print("OUTPUT",wrd)

-------------------------------------------------------------
QUESTION 11:
Write a program to take inputs of different data type as key input
and then the value as its data_types name (i.e,. “string”, “integer” or “float”).
Store the values in a dictionary with key as input and value as data type.
Make a sentence with all the inputs which are of string data type and display the same.
For example,
for the dictionary {"hello":"string", 5:"integer", “world”: “string”}
the sentence is "hello world".

ANS:
n=int(input("Enter the number of elements"))
d={}
wrd=""
for i in range(n):
    key=input("enter value of key")    
    if "." in key:
            d[float(key)]="Float"
    elif key.isdigit():         
            d[int(key)]="Integer"
    elif key.isalpha():
        d[key]="String"
    else:
        continue
print("dictionary:",d)
for i in d:
    if d[i]=="String":
        wrd+=i+" "
        
print(wrd)
--------------------------------------------------------------------------------------------
QUESTION 12:
Write a python program that accepts two inputs as word from the user
and checks if two words are anagrams of each other.
An anagram is a word or phrase formed by rearranging the letters of another.
Eg 1: inp_string 1: anagram inp_string 2: nagaram , Output: True
Eg 2: inp_string 1: baseball, inp_string 2: basketball , Output: False

ANS:
s1=input("Enter your first string")
s2=input("enter your second string")
l1=list(s1)
l2=list(s2)
l1.sort()
l2.sort()
if l1==l2:
    print("OUTPUT: True")

else:
    print("OUTPUT: False")
----------------------------------------------------------------------------------------
QUESTION 13
Write a program that accepts word as input from the user
and translates that word into Pig Latin.
In Pig Latin, words are transformed by moving the first letter to the end
and adding "ay."
For example, "hello" becomes "ellohay."

ANS:
s=input("Enter a word")
nword=s[1:]+s[0]+"ay"
print(nword)

--------------------------------------------------------------------------------------
QUESTION 14:
A cipher is a method of transforming a message to conceal its meaning.
The simplest technique involves shifting the letters in the message by a certain number of positions,
known as the “shift” or “key”.
Given a message and an integer shift value, print the encrypted message.
For instance, Encryption - If shift value is 2, A becomes C, B becomes D etc.
Z cycles back and becomes B.
Eg1: inp_str=”Hello world” , shift_value=3, Output= Khoor zruog
Eg2: inp_str=” Zero to hero!” , shift_value=1, Output= Afsp up ifsp!

ANS:
s=input("Enter a string")
key=int(input("Enter your shift value"))
wrd=""
s2=0
for i in s:
    if i.isupper():
        if i!="Z":
            s2=ord(i)
            wrd+=chr(s2+key)
        elif i=="Z":
            wrd+=chr(64+key)
    
    elif i.islower():
        if i!="z":
            s2=ord(i)
            wrd+=chr(s2+key)
        elif i=="z":
            wrd+=chr(96+key)
    else:
        wrd+=i

print("OUTPUT=",wrd)
-------------------------------------------------------------------------------------------
QUESTION 15:DO IT 
Write a Python program that takes a string as input,
finds and prints all the unique substrings of the given string in a list in lexicographical order.

ANS:
'''


def unique_substrings(input_str):
    substrings = set()

    # Generate all possible substrings
    for i in range(len(input_str)):
        for j in range(i + 1, len(input_str) + 1):
            substrings.add(input_str[i:j])

    # Convert the set of substrings to a list and sort it lexicographically
    sorted_substrings = sorted(list(substrings))

    return sorted_substrings

# Take input from the user
input_string = input("Enter a string: ")

# Call the function and print the result
result = unique_substrings(input_string)
print("Unique Substrings in Lexicographical Order:", result)
