def factorial(n: int) -> int:
    # n! factorial can also be defined as n * (n - 1)!
    """calculate n! recursively"""
    if n <= 1:
        return 1
    else:
        return n * factorial(n - 1)


try:
    print(factorial(1000))
except (RecursionError, OverflowError):
    print('This program cannot calculate factorials that large')

print('Program terminating...')
