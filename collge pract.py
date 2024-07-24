'''
a=1234

s=0
while a>0:
    n=a%10
    s=s*10+n
    a=a//10

print(s)    
-------------
print("hi how u doing\
nicr to meet you da")
print(1,3)
-----------------------------
rows = int(input())
num = 1
for i in range(1, rows + 1):
    for j in range(i):
        print(num, end=" ")
        num += 1
    print()
----------------

7
   *
  ***
 *****
*******
 *****
  ***
   *


rows = int(input())
half_rows = (rows + 1) // 2
for i in range(1, half_rows + 1):
    print(" " * (half_rows - i) + "*" * (2 * i - 1))
for i in range(half_rows - 1, 0, -1):
    print(" " * (half_rows - i) + "*" * (2 * i - 1))

--------------------------------------------------
#ARMSTRONG NUMBER OR NOT 
n=153
num=n
sums=0
while num>0:
    n2=num%10
    sums+=(n2*n2*n2)
    num//=10

if sums==n:
    print("yes")
else:
    print("no")
--------------------------
lcm
n = int(input())
for i in range(1, int(n ** 0.5) + 1):
    if n % i == 0:
        # Floor division (//) to get integer values
        print(i, n // i)
=============================
def out_fn():
    v = 10
    def in_fn():
        # indicates that it has to access v of out_fn()
        # using the keyword nonlocal
        nonlocal v
        v = v * 5
        print(v) #50
    in_fn()
    print(v) #50

out_fn()
--------------------------------------
import random
l=[2,345,6743,567]
print(random.shuffle(l))
print(l)

-------------------------------

values = [[3, 4, 5, 1], [33, 6, 1, 2]]
v = values[0][0]
for row in range(0, len(values)):
    for column in range(0, len(values[row])):
        if v < values[row][column]:
            v = values[row][column]

print(v)
----------------
d={2:3,3:4,4:5}
print(d.get(2))
--------------------

n=4
s=0
for i in range(1,n+1):
    s+=(i*(i+1))
    if i<(n):
        print(i,"*",i+1,"+",end="")
    else:
        print(i,"*",i+1,end="")
print("=",s)
------------------

from tkinter import *
master = Tk()
master.geometry("500x500")
label = Label(master, text ='Languages you know:', font = "50")
label.pack()
CButton1 = Checkbutton(master, text = "C", height = 2,variable = 1, width = 10)
CButton2 = Checkbutton(master, text = "C++", height = 2, width = 10, variable = 1)
CButton3 = Checkbutton(master, text = "JAVA", height = 2, variable = 1,width = 10)
CButton4 = Checkbutton(master, text = "Python", height = 2, width = 10)
CButton1.pack()
CButton2.pack()
CButton3.pack()
CButton4.pack()
mainloop()
---------------------

from tkinter import *
from tkinter import messagebox
root = Tk()
root.geometry("300x200")
w = Label(root, text ='Keep clicking on any one option', font = "50")
w.pack()
messagebox.showinfo("showinfo", "Information")
messagebox.showwarning("showwarning", "Warning")
messagebox.showerror("showerror", "Error")
messagebox.askquestion("askquestion", "Are you sure?")
messagebox.askokcancel("askokcancel", "Want to continue?")
root.mainloop()
------------------

import tkinter
win = tkinter.Tk()
label = tkinter.Label(text = "Which is your favourite subject?")
label.grid(row = 0, column = 0)
sub1 = "mathematics"
sub2 = "pcps_theory"
sub3 = "chem theory"
button1 = tkinter.Checkbutton(win, text = "Maths", bg = "red",variable = sub1)
button1.grid(row = 1,column = 1)
button2 = tkinter.Checkbutton(win, text = "PCPS", bg = "yellow",variable = sub2)
button2.grid(row = 2,column = 1)
button3 = tkinter.Checkbutton(win, text = "CHEM", bg = "yellow",variable = sub3)
button3.grid(row = 3, column = 1)
tkinter.Button(win, text="Use it").grid(row=5,columnspan=2)
tkinter.Button(win, text="Use it").grid(row=6,columnspan=2)
win.mainloop()
-----------------
from tkinter import *
win = Tk()
canvas1 = Canvas(win, bg = "light blue", height = 400)
#coord = 10,10,200,200
myrect = canvas1.create_rectangle((10,10,100,200), fill = "red", width = 5)
canvas1.pack()
mainloop()
----------------
from tkinter import *
win=Tk()
win.geometry("400x400")
frame1=Frame(win,bg="brown",width=500,height=300)
frame1.pack()
frame2=Frame(frame1,bg="pink",width=100,height=100)
frame2.pack(pady=20,padx=20) #remove padx and pady. Check the output.
win.mainloop()
---------------------

import tkinter
win = tkinter.Tk()
for i in ["yellow", "blue", "red", "orange","brown", "violet", "indigo", "green"]:
    tkinter.Frame(win,height = 10, width = 200, bg = i).pack()
win.mainloop()
----------------------
'''
import tkinter as tk

root = tk.Tk()
button = tk.Button(root, text="Click Me!")
button.pack()
root.mainloop()
