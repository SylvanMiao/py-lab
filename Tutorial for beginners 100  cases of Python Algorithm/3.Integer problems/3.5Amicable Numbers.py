# 求给定范围内的所有亲密数，亲密数定义为：整数a的所有因子之和等于b，反之亦然(包括1，不包括本身)
if __name__ == "__main__":
    # 因数求和函数
    def sumit(x):
        sum = 0
        for j in range(1, x // 2 + 1):
            if x % j == 0:
                sum += j
        return sum

    n = int(input())
    for i in range(1, n):
        k = sumit(i)
        if k <= 3000:
            w = sumit(k)
        if w == i and i < k:
            print("%d--- %d" % (i, k))
