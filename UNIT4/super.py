class Person:
    def __init__(self,name,idnumber):
        self.name=name
        self.idnumber=idnumber
        
    def display(self):
        print(self.salary)
        print(self.idnumber)
        
        
class Employee(Person):
    def __init__(self,name,idnumber,salary,desg):
        self.salary=salary
        self.desg=desg
        super().__init__(name,idnumber)
        
emp = Employee('Riya', 802, 50000, "Admin")
emp.display()        
        