# 求100以内的所有勾股数
if __name__ == "__main__":
    for a in range(1, 100):
        for b in range(a + 1, 100):
            for c in range(b + 1, 100):
                if a**2 + b**2 == c**2 and a + b > c:
                    print("%d %d %d" % (a, b, c))
