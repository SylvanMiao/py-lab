# 求某一范围内的完数，指一个数等于它的因子之和
if __name__ == "__main__":
    n = int(input("enter the range"))
    for i in range(1, n):
        sum = 0
        # 对整数n来说，其因子最大为n//2
        for j in range(1, i // 2 + 1):
            if i % j == 0:
                sum += j
        if sum == i:
            print(i)
