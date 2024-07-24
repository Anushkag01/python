class MyDate:
    def __init__(self, d,m,y):
        self.dd = d
        self.mm = m
        self.yy = y
   def __str__(self):
        return str(self.dd)+" "+str(self.mm)+" "+str(self.yy)

class Person:
    def __init__(self, n,a,d,m,y):
        self.name = n
        self.age = a
        self.dob = MyDate(d,m,y) #Person has date of birth
    def __str__(self):
        return self.name+" "+str(self.age)+" "+str(self.dob)
    
p1 = Person("sindhu", 56, 2,4,1999)
p2 = Person("indhu", 53, 2,8,1919)
p3 = Person("bindhu", 51, 2,1,2000)
print(p1)
print(p2)
print(p3)    