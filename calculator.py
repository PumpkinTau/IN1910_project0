
#Implements addition
def add(x, y):
    return x + y

#Implements the factorial function n! for integers n
def factorial(n):
    fact = 1
    for i in range(1, n+1):
        fact *= i
    return fact

#Implements the taylor series for sin(x) for N+1 terms
def sin(x, N):
    num = 0
    for n in range(N+1):
        num += ((-1)**n * x**(2*n + 1)) / factorial(2*n + 1)
    return num