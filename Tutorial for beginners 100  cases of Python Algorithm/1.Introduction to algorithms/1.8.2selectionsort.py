def selectionsort(a):
    n = len(a)
    for i in range(0, n - 1):
        for j in range(i + 1, n):
            if a[i] < a[j]:
                t = a[i]
                a[i] = a[j]
                a[j] = t
    print(a)


if __name__ == "__main__":

    print("请输入需要排序的数组：")
    num = input()
    num_ = num.split(" ")
    for i in range(0, len(num_)):
        num_[i] = int(num_[i])
    selectionsort(num_)
