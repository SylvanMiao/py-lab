if __name__ == "__main__":
    i = 0
    for a in range(1, 6):
        for b in range(1, 6):
            if a != b:
                for c in range(1, 6):
                    if a != c and b != c:
                        print(a, b, c)
                        i += 1
                        if i % 4 == 0:
                            print()
