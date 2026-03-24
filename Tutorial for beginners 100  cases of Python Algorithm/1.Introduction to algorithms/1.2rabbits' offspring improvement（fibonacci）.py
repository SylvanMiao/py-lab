if __name__ == "__main__":
    fib1 = 1
    fib2 = 1
    i = 1
    while i <= 15:
        print("%d %d" % (fib1, fib2))
        if i % 2 == 0:
            print()
        fib1 = fib1 + fib2
        fib2 = fib1 + fib2
        i += 1
