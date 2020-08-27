import calculator
import math

#The tolerance used by all tests for floating point numbers
tolerance = 10**-12

#Creates an error message for a typical assert statement
def message(expected, recieved):
    return f"Expected {expected}, got {recieved}"

#Tests add function for integers
def test_add_excercise_1():
    num = calculator.add(1, 2)
    expected = 3 
    assert num==expected, message(expected, num)

#Tests add function for floating point numbers
def test_add_excercise_2():
    num = calculator.add(0.1, 0.2)
    expected = 0.3
    assert abs(num - expected) < tolerance, message(expected, num)

#Tests add function for strings
def test_add_excercise_3():
    string = calculator.add("Hello ", "World")
    expected = "Hello World"
    assert string == expected, message(expected, string)

#Tests the factorial function for 4 inputs against math.factorial
def test_factorial_excercise_4():
    for n in (0, 1, 5, 10):
        num = calculator.factorial(n)
        expected = math.factorial(n)
        assert num==expected, message(expected, num)

#Tests the sin function for 4 inpusts against math.sin
def test_sin_excercise_4():
    N = 50
    for x in (0, 0.1, 1, math.pi):
        num = calculator.sin(x, N)
        expected = math.sin(x)
        assert abs(num - expected) < tolerance, message(expected, num)

#Tests the divide function for 4 sets of inputs
def test_divide_excercise_4():
    args = ((0, 1), (100, 10), (7, 5), (5, 7))
    expected = (0, 10, 1.4, 0.714285714285714)
    for i in range(4):
        num = calculator.divide(args[i][0], args[i][1])
        assert abs(num - expected[i] < tolerance), message(expected[i], num) 

#Tests the exp function for 4 inputs against math.exp
def test_exp_excercise_4():
    N = 50
    for x in (-2, 0, 0.5, 4):
        num = calculator.exp(x, N)
        expected = math.exp(x)
        assert abs(num - expected) < tolerance, message(expected, num)

#Tests the combination function for 4 inputs against math.comb
def test_comb_excercise_4():
    n = 50
    for i in (0, 25, 50, 60):
        num = calculator.comb(n, i)
        expected = math.comb(n, i)
        assert num == expected, message(expected, num)

#Tests the comb function for numbers too large to be stored as ints
def test_comb_large_args_excercise_4():
    n = 500
    for i in (0, 50, 250, 500):
        num = calculator.comb(n, i)
        expected = math.comb(n, i)
        #Since the numbers are quite large, the relative error is more interesting than the absolute error
        assert abs(num/expected - 1) < tolerance, message(expected, num)

