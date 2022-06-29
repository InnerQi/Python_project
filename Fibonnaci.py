def fib(n):    # new function
    a, b = 0, 1    # assign initial values
    while a < n:
        print(a, end=' ')  # adds space between numbers on the same line
        a, b = b, a + b
    # print()
fib(1000)

