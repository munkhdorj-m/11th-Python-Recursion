import pytest
import inspect
from assignment import fibonacci, count_digits, sum_digits

def check_no_loop(func):
    """Return True if function does NOT contain 'for' or 'while'."""
    source = inspect.getsource(func)
    if "for " in source or "while " in source:
        return False
    return True

@pytest.mark.parametrize("n, expected", [
    (0, 0),
    (1, 1),
    (2, 1),
    (3, 2),
    (6, 8),
    (10, 55)
])
def test1(n, expected):
    # Fail test if student used a loop
    assert check_no_loop(fibonacci), "fibonacci() uses a loop! Use recursion instead."
    assert fibonacci(n) == expected

@pytest.mark.parametrize("n, expected", [
    (0, 1),
    (5, 1),
    (5029, 4),
    (1234567890, 10)
])
def test2(n, expected):
    assert check_no_loop(count_digits), "count_digits() uses a loop! Use recursion instead."
    assert count_digits(n) == expected

@pytest.mark.parametrize("n, expected", [
    (0, 0),
    (5, 5),
    (5029, 16),
    (123, 6),
    (9999, 36)
])
def test3(n, expected):
    assert check_no_loop(sum_digits), "sum_digits() uses a loop! Use recursion instead."
    assert sum_digits(n) == expected
