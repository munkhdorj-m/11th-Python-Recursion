# assignment.py

# ------------------- Exercise 1: Fibonacci -------------------
def fibonacci(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)

 
# ------------------- Exercise 2: Count Digits -------------------
def count_digits(n):
    n = abs(n)  # handle negative numbers
    if n < 10:
        return 1
    else:
        return 1 + count_digits(n // 10)


# ------------------- Exercise 3: Sum Digits -------------------
def sum_digits(n):
    n = abs(n)  # handle negative numbers
    if n == 0:
        return 0
    else:
        return n % 10 + sum_digits(n // 10)
