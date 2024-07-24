#ESA PRACTICE
'''
print(eval("2+4-1"))
n=0
if n==0:
 print("hi")
'''
'''while n==0:
    print("bye")
    
list1=[2,34,5,667,87]
list2=[34,56,75]

list3=list1.copy()
list1.pop()
list4=list2[::]
list2.pop()
print(list4)
print(list1)

'''
'''
#print(list1[5:2:1])
rows = int(input())
num = 1
for i in range(1, rows + 1):
 for j in range(1, i + 1):
  print(num, end=" ")
  num += 1
 print()
 '''
'''
str1="Hello ppl amazing world"
print(str1.startswith("ppl",6,9))
print(str1.find("ppl"))
print(str1.rstrip("orld"))
print(str1)
'''
'''
def f1():
 print("in f1")
 return f2()
def f2():
 print("in f2")
print(f1())
'''
#print(chr(97))
'''
s=input()
s=s.replace(" ","").lower()
s1=s[::-1]
if s==s1:
    print("yes")
    
else:
    print("no")
    
 '''   
'''
string1 = input()
string2 = input()
# Check if the lengths of both strings are the same
if len(string1) != len(string2):
 print("N")
else:
 combined_string = string1 + string1 # Concatenate the first string with itself
 if string2 in combined_string:
  print("Y")
 else:
  print("N")
  '''
'''
count=0
d={}
string="how much would a wood chuck chuck if a wood chuck could chuck wood"
for i in string.split():
    count=string.count(i)
    d[i]=count
    count=0
print(sorted(d.items()))
---------


class Phone:
    def __init__(self,n):
        self.num = n
        self.service = 'Airtel'
class Person:
    def __init__(self,name):
       self.name = name
       self.ph = Phone(9855886601)
person = Person('John')
print(len(person.__dict__))

---------
print( 4 / 2 ** 3 )
a = 7; b = 2; print(a >> b << b)
print( ~~~3 ** 2)
print( 1,2 in [1,2,3,4,5])
a = 3; b = 4; print( a or b )
'''
'''
a=[0,1,2,3]
for a[-1] in a :
    print(a[-1],end=",")
    '''
class myRange:
 def __init__(self,n):
  self.limit = n
 def __iter__(self):
  self.i = 0
  return self
 def __next__(self):
  self.i += 1
  return self.i-1

r = myRange(5)
t = iter(r)
print(next(t))
print(next(t))
u = iter(r)
print(next(u))
print(next(t))