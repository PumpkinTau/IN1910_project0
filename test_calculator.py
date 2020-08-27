import calculator

#Creates an error message for a typical assert statement
def message(expected, recieved):
    return f"Expected {expected}, got {num}"

def test_add_excercise_1():
    num = calculator.add(1, 2)
    expected = 3 
    assert num==expected, message(expected, num)

def test_add_excercise_2():
    num = calculator.add(0.1, 0.2)
    expected = 0.3
    tolerance = 10**-12
    assert abs(num - expected) < tolerance, message(expected, num)

    