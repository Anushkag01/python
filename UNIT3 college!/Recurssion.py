'''
#For finding the factorial
def fact(n):
    if n==0:
        res=1

    else:
        res=n*fact(n-1)

    return res

print(fact(5))
print(fact(0))

#for finding the length of the string
def length(s):
    if s=="":
        return 0
    else:
        len=1+length(s[1:])

    return len     

print(length("Python"))        
'''
#for fibonacci series
#0 1 1 2 3 5
count=0
def fib(n):
    if count==n:
        return 0
    else:
        
        s=1+fib(count)
    return s
count=0
print(fib(5))
