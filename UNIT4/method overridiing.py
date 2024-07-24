class A:
    def greeting(self):
        return "Hello from A"
class B(A):
    def greeting(self):
        return super().greeting() + " overridden by B"

class C(A):
    def greeting(self):
        return super().greeting() + " overridden by C"
class D(B, C):
    pass
obj = D()
print(obj.greeting())