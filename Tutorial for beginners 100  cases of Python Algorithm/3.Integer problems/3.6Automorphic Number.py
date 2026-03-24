# 自守数是指一个数的平方的尾数等于该数自身的自然数，例如76*76=5776
if __name__ == "__main__":
    # 求位数函数
    def calculatebyte(x):
        count = 0
        while x != 0:
            count += 1
            x //= 10
        return count

    n = int(input())
    for i in range(0, n + 1):
        square = i**2
        w = calculatebyte(i)
        if (square - i) % (10**w) == 0:
            print(i)
