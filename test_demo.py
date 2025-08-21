# tests/test_basics.py

def test_hello_world():
    print("Hello, PyTest!")
    assert "Hello" in "Hello, PyTest!"


def add(a, b):
    return a + b


def test_addition():
    assert add(2, 3) == 5
    assert add(-1, 1) == 0
