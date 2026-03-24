def bubblesort(a):
    n = len(a)
    i = 1
    while i <= n - 1:
        j = 0
        while j < n - i:
            if a[j] > a[j + 1]:
                t = a[j]
                a[j] = a[j + 1]
                a[j + 1] = t
            j += 1
        i += 1
    print(a)


if __name__ == "__main__":

    print("请输入需要排序的数组：")
    num = input()
    num_ = num.split(" ")
    for i in range(0, len(num_)):
        num_[i] = int(num_[i])
    bubblesort(num_)
