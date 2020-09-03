import calculator
import math
import pytest

#The tolerance used by all tests for floating point numbers
tolerance = 10**-12

#Creates an error message for a typical assert statement
def message(expected, recieved):
    return f"Expected {expected}, got {recieved}"

#Tests add function for integers
@pytest.mark.parametrize("x, y, expected", \
    ((1, 2, 3), (-1, 1, 0), (-2, -4, -6), (-2, 3, 1)))
def test_add_excercise_1(x, y, expected):
    num = calculator.add(x, y) 
    assert num==expected, message(expected, num)

#Tests add function for floating point numbers
@pytest.mark.parametrize("x, y, expected", \
    ((0.1, 0.2, 0.3), (-1.1, 1.1, 0), (-2.0, -4.1, -6.1), (-2.1, 3.2, 1.1)))
def test_add_excercise_2(x, y, expected):
    num = calculator.add(x, y)
    assert abs(num - expected) < tolerance, message(expected, num)

#Tests add function for strings
@pytest.mark.parametrize("x, y, expected", \
    (("Hello ", "World", "Hello World"), ("Hello World", "", "Hello World"), \
        ("'@", "Hello World'", "'@Hello World'"), ("Hello ", "Wørld", "Hello Wørld")))
def test_add_excercise_3(x, y, expected):
    string = calculator.add(x, y)
    assert string == expected, message(expected, string)

#Tests the factorial function for 4 inputs against math.factorial
@pytest.mark.parametrize("n", (0, 1, 5, 10))
def test_factorial_excercise_4(n):
    num = calculator.factorial(n)
    expected = math.factorial(n)
    assert num==expected, message(expected, num)

#Tests the sin function for 4 inputs against math.sin
@pytest.mark.parametrize("x", (0, 0.1, 1, math.pi))
def test_sin_excercise_4(x):
    N = 50
    num = calculator.sin(x, N)
    expected = math.sin(x)
    assert abs(num - expected) < tolerance, message(expected, num)

#Tests the divide function for 4 sets of inputs
@pytest.mark.parametrize("x, y, expected", \
    ((0, 1, 0), (120.75, 10.5, 11.5), (7, 5, 1.4), (5, 7, 0.714285714285714)))
def test_divide_excercise_4(x, y, expected):
    num = calculator.divide(x, y)
    assert abs(num - expected) < tolerance, message(expected, num) 

#Tests the exp function for 4 inputs against math.exp
@pytest.mark.parametrize("x", (-2, 0, 0.5, 4))
def test_exp_excercise_4(x):
    N = 50
    num = calculator.exp(x, N)
    expected = math.exp(x)
    assert abs(num - expected) < tolerance, message(expected, num)

#Tests the combination function for 4 inputs against math.comb
@pytest.mark.parametrize("i", (0, 25, 50, 60))
def test_comb_excercise_4(i):
    n = 50
    num = calculator.comb(n, i)
    expected = math.comb(n, i)
    assert num == expected, message(expected, num)

#Checks that the add function raises a TypeError for str+int and str+float
@pytest.mark.parametrize("str, num", (("Hello", 2), ("Hello", 2.5), ("1", 1)))
def test_add_raises_TypeError_for_string_plus_number_excercise_5(str, num):
    with pytest.raises(TypeError):
        calculator.add(str, num)

#Checks that the divide function raises a ZeroDivisionError for x/0
@pytest.mark.parametrize("x", (5, 5.5, 0, 0.0))
def test_divide_raises_ZeroDivisionError_for_number_divided_by_0_excercise_5(x):
    with pytest.raises(ZeroDivisionError):
        calculator.divide(x, 0)