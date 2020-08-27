import calculator

def test_add_excercise_1():
    num = calculator.add(1, 2)
    expected = 3
    msg = f"Expected {expected}, got {num}"
    assert num==expected, msg
