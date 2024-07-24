class Class2:
    def m(self):
        print("In Class2")
class Class3:
    def m(self):
        print("In Class3")
class Class4(Class3, Class2):
    pass
obj = Class4()
obj.m()
