def fibonacci(n):
    """Return the first n Fibonacci numbers."""
    numbers = []
    a, b = 0, 1
    for _ in range(n):
        numbers.append(a)
        a, b = b, a + b
    return numbers


if __name__ == "__main__":
    for num in fibonacci(5):
        print(num)
