'''
Problem Statement: Write a program that takes a positive number as input and
pairwise prints all the factors of the number.
------------------------------------------------
n = int(input())
for i in range(1, int(n ** 0.5) + 1):
 if n % i == 0:
 # Floor division (//) to get integer values
  print(i, n // i)

***************************************
'''
'''
40)(Competitive) Problem Statement: Write a program that takes number of rows as
input and prints the following pattern -
###1
##21
#321
4321
------

rows = int(input())
for i in range(1, rows + 1):
    print("#" * (rows - i), end="")
    for j in range(i, 0, -1):
        print(j, end="")
    print()

**************
'''
'''
38)Problem Statement: Write a program that prints all the perfect squares between 1
and N (inclusive).

Solution:

n = int(input())
for i in range(1, n+1):
# Taking integer values closest or equal to square root, truncates decimal
sqt = int(i ** 0.5)
if sqt ** 2 == i:
print(i)

**********************************
'''
'''
36)(Competitive) Problem Statement: Write a program that takes number of rows as
input and prints the following pattern -
1
121
12321
1234321

n=int(input())
for i in range(1,n+1):
    for k in range(1,i+1):
        print(k,end="")
    for j in range(i-1,0,-1):
        print(j,end="")
    print()
'''
'''
(Competitive) Problem Statement: Write a program that calculates and prints the
Least Common Multiple (LCM) of two positive integers entered by the user.
Solution:
----------
num1 = int(input())
num2 = int(input())
if num1 == num2:
 print(num1)
else:
    max_num = max(num1, num2)
    lcm = max_num
    while True:
        if lcm % num1 == 0 and lcm % num2 == 0:
            break
        lcm += 1
    print(lcm)
    -------

def length(string):
    if string=="":
        return string
    else:
        return string
    
string1=input()
print("length=",length(string1))
'''
from tkinter import *
win = Tk()
win.geometry("300x300")
username=Label(win, text = "Username")
password=Label(win, text = "Password")
e1=Entry(win,width = 20)
e2=Entry(win, width = 20, show = "-")
username.pack()
e1.pack()
password.pack()
e2.pack()
win.mainloop()