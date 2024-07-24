
#Example 1 - Compute factorial of a number
'''
def fact(n): #Recursive Function
	if n == 0 : #terminating condition
		res = 1 
	else:
		res = n * fact(n - 1) 
	return res	
print(fact(5)) 
print(fact(0))
'''
#Example 2 – Compute GCD of two numbers
'''
def gcd(m, n): #Recursive Function
	if m == n : #terminating condition
		res = m
	elif m > n :
		res = gcd(m -n, n)
	else:
		res = gcd(m, n - m)
	return res
print("GCD : ", gcd(16, 32))
'''
#Example 3 – Generate Fibonacci Series upto n_terms
'''
def fib(n):
  if n <= 1:
      return n
  else:
      return(fib(n-1) + fib(n-2))
 
n_terms=int(input("Enter the number of terms for Fibonacci Series\n"))
for i in range(n_terms):
    print(fib(i))
'''
#Example 4 - Tower of Hanoi
'''
def TowerOfHanoi(n , src, aux, dest):
    if n==1:
        print ("Move disk 1 from ",src,"to ",dest)
    else:    
        TowerOfHanoi(n-1, src, dest, aux)
        print ("Move disk",n,"from ",src,"to ",dest)
        TowerOfHanoi(n-1, aux, src, dest)
      
n=int(input("Enter number of disks\n"))
print("A-Source  B-Auxiliary  C-Destination\n")
TowerOfHanoi(n,'A','B','C')
'''
#Example 5 - To add two numbers using recursion
'''
def add(x, y):
    if(y == 0):
        return x
    return add(x, y - 1) + 1
 
print("Sum =", add(10, 20))
'''
#Example 6 - To subtract two numbers using recursion
'''
def subtract(x, y):
    if(y == 0):
        return x
    return subtract(x-1, y-1)
 
print("Result =", subtract(10, 20))
'''
#Example 7 - To multiply two numbers using recursion
'''
def product(a,b):
    if(a<b):
        return product(b,a)
    elif(b!=0):
        return(a+product(a,b-1))
    else:
        return 0

print("Product =",product(10,20))
'''
#Example 8 - To divide two numbers using recursion
'''
def divide(x, y):
    if(x < y):
        return 0
    else:
        return 1 + divide(x - y, y)

print("Result:", divide(20, 5))
'''
#Example 9 - To compute the sum of 1st n natural numbers using recursion
'''
def sum_nums(n):
    if n==1:
        return 1
    else:
        return n+sum_nums(n-1)

n=int(input("Enter the value of n\n"))
print(sum_nums(n))
'''

