import doctest

# Parašykite funkciją su dokumentaciniais testais
def factorial(n):
    """
    Return factorial of n

    >>> [factorial(n) for n in range(6)]
    [1, 1, 2, 6, 24, 120]
    """
    fact = 1
    for i in range(1, n + 1):
        fact = fact * i
    return fact

# Ištestuokite funkciją
if __name__ == '__main__':
    doctest.main()
