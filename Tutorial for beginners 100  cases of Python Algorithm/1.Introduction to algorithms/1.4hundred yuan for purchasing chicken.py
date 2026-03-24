if __name__ == "__main__":
    for cock in range(0, 21):
        for hen in range(0, 33):
            for chicken in range(0, 100):
                if (
                    cock + hen + chicken == 100
                    and 5 * cock + 3 * hen + chicken / 3 == 100
                ):
                    print("cock=%d hen=%d chicken=%d" % (cock, hen, chicken))
                else:
                    continue
