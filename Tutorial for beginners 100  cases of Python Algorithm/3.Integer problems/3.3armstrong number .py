# 阿姆斯特朗数：不限定位数的水仙花数
if __name__ == "__main__":
    n = int(input())
    for i in range(0, n):
        sum = 0
        number = i
        a = []
        while number != 0:
            a.append(number % 10)
            number //= 10
        for j in range(0, len(a)):
            sum += a[j] ** 3
        if sum == i:
            print(i)
