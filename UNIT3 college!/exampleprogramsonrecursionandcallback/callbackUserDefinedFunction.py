#Example 1
'''
def multiply(x):
    return x[0]*x[1]
 
def compute(func,x):
    return func(x)
 
num_list=[2,3] 
product=compute(multiply,num_list) 
print("Multiplication=",product)
'''
#Example 2 - Multiple Callback functions
'''
def function(func_list, x, y):
    print("Inside function")
    for func in func_list:
        func(x,y)
    
def add(x,y):
    z = x+y
    print('Sum =',z)
 
def divide(x,y):
    z = x/y
    print('Quotient =',z)
    
cb_list=[add, divide]
function(cb_list, 10, 5)
'''
#Example 3 - Multiple Callback functions (Different Approach)
'''
def function(func, x, y):
    print("Inside function")
    func(x,y)
    
def add(x,y):
    z = x+y
    print('Sum =',z)
 
def divide(x,y):
    z = x/y
    print('Quotient =',z)
    
function(add, 10, 5)
function(divide, 10, 5)
'''
#Example 4 - Read a number. If it's even, calculate it's double; if it's odd, calculate it's triple
'''
def double(x):
    print("Even number =",x,", Its double =",x**2)
def triple(x):
    print("Odd number =",x,", Its triple =",x**3)

def compute(func, n):
    func(n)

n=int(input("Enter a number\n"))
if n%2==0:
    compute(double,n)
else:
    compute(triple,n)
'''

