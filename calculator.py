
#Implements addition
def add(x, y):
    return x + y

#Implements the factorial function n! for integers n
def factorial(n):
    fact = 1
    for i in range(1, n+1):
        fact *= i
    return fact