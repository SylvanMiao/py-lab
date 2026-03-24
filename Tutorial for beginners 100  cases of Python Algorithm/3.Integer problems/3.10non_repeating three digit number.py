# 用1,2,3,4四个数字能够组成多少个互不相同且无重复数字的三位数？
if __name__ == "__main__":
    count = 0
    for a in range(1, 5):
        for b in range(1, 5):
            for c in range(1, 5):
                if a != b and b != c and a != c:
                    count += 1
                    print("%d %d %d" % (a, b, c))
    print("共有%d种" % count)
