'''def fib(n):    #Recursive Function
  	if n <= 1: #terminating condition
    	     return n
  	else:
    	     return(fib(n-1) + fib(n-2))
 
n_terms=int(input("Enter the number of terms for Fibonacci Series\n"))

for i in range(n_terms):
           print(fib(i))
 '''
def sum1(n):
    if (n == 1):
        return 1
    else:
        return n + sum1(n - 1)
number = 10
print("The sum of first", number,"number is", sum1(number))