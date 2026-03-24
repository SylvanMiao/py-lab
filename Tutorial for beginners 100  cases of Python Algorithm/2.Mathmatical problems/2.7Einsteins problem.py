# 爱因斯坦出了一道这样的数学题：有一条长阶梯，若每步跨2阶，则最后剩一阶梯；每步跨3阶，则最后只剩2阶；若每步跨5阶，则最后剩4阶
# 若每步跨6阶，则最后剩5阶，只有每次跨7阶，最后才1阶不剩。请问在1到n内，有多少个数才能满足？
def judgeproblem(n):
    for i in range(7, n - 1):
        if i % 2 == 1 and i % 3 == 2 and i % 5 == 4 and i % 6 == 5 and i % 7 == 0:
            print(i)


if __name__ == "__main__":
    while 1:
        n = int(input("请输入目标值："))
        judgeproblem(n)
