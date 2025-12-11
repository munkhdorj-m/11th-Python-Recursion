def fibonacci(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)

def count_digits(n):
    if n < 10:
        return 1
    else:
        return 1 + count_digits(n // 10)

def sum_digits(n):
    if n == 0:
        return 0
    else:
        return n % 10 + sum_digits(n // 10)
