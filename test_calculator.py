import calculator
import math

#Creates an error message for a typical assert statement
def message(expected, recieved):
    return f"Expected {expected}, got {num}"

#Tests add function for integers
def test_add_excercise_1():
    num = calculator.add(1, 2)
    expected = 3 
    assert num==expected, message(expected, num)

#Tests add function for floating point numbers
def test_add_excercise_2():
    num = calculator.add(0.1, 0.2)
    expected = 0.3
    tolerance = 10**-12
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

