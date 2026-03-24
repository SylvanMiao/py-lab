# 将5元的人民币兑换成1元、5角和1角的硬币，共有多少种不同的兑换方法

if __name__ == "__main__":
    count = 0
    for x in range(0, 11):
        for y in range(0, (50 - 10 * x) // 5 + 1):
            for z in range(0, (50 - 10 * x - 5 * y) + 1):
                if 10 * x + 5 * y + z == 50:
                    print("%d %d %d" % (x, y, z))
                    count += 1
                    if count % 3 == 0:
                        print(" ")
    print("共有%d种" % count)
