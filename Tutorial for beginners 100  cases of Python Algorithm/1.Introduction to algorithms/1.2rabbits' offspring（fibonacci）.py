fib1 = 1
fib2 = 1
for n in range(1, 31):

    if n < 3:
        fib = 1
        print(fib)
    else:
        fib = fib1 + fib2
        print(fib)
        fib1 = fib2
        fib2 = fib
    if n % 4 == 0:
        print()
