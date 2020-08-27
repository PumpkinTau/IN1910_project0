
#Implements addition of both numbers and strings
def add(x, y):
    return x + y

#Implements the factorial function n! for integers n
def factorial(n):
    if not isinstance(n, int):
        raise TypeError("calculator.factorial does not support non-integer arguments.")
    fact = 1
    for i in range(1, n+1):
        fact *= i
    return fact

#Implements the taylor series for sin(x) for N+1 terms
def sin(x, N):
    if not isinstance(N, int):
        raise TypeError("Please enter an integer value for N")
    if N < 0:
        raise ValueError("Please enter a non-negative value for N")
    num = 0
    for n in range(N+1):
        num += ((-1)**n * x**(2*n + 1)) / factorial(2*n + 1)
    return num

#Implements division of numbers
#Returns x/y
def divide(x, y):
    return x/y

#Implements the taylor series for e^x for N+1 terms
def exp(x, N):
    if not isinstance(N, int):
        raise TypeError("Please enter an integer value for N")
    if N < 0:
        raise ValueError("Please enter a non-negative value for N")
    num = 0
    for n in range(N+1):
        num += x**n / factorial(n)
    return num

#Implements a combination
#Given integers n and i, returns the number of ways to choose i elements of a set of n
def comb(n, i):
    if not (isinstance(n, int) and isinstance(i, int)):
        raise TypeError("calculator.comb does not support non-integer arguments.")
    if n < 0 or i < 0:
        raise ValueError("calculator.comb does not support negative arguments.")
    if i > n:
        return 0
    else:
        num = 1
        for j in range(n-i+1, n+1):
            num *= j
        num /= factorial(i)
        return num