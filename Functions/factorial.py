# n! = n*n-1*n-2*n-3
def factorial(n):
    prod = 1
    while n>=1:
        prod*=n
        n=n-1
    return prod
    
for i in range(1 ,100):
    print('Factorial is {} is {}'.format(i, factorial(i)))