# tests/test_parametrize.py
import pytest

# Example 1: Simple math test with multiple inputs
@pytest.mark.parametrize("a, b, expected", [
    (2, 3, 5),
    (5, 5, 10),
    (10, -2, 8),
])
def test_addition(a, b, expected):
    assert a + b == expected


# Example 2: String length check
@pytest.mark.parametrize("word, length", [
    ("Python", 6),
    ("pytest", 6),
    ("QA", 2),
])
def test_string_length(word, length):
    assert len(word) == length


# Example 3: Check if a number is even
@pytest.mark.parametrize("num", [2, 4, 6, 8, 10])
def test_is_even(num):
    assert num % 2 == 0
