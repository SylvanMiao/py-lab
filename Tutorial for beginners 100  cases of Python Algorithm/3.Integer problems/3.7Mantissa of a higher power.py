# 求一个数的高次方的后三位尾数，例如13的13次方的后三位
if __name__ == "__main__":
    print("请输入乘数以及乘方数")
    n, times = map(int, input().split())
    count = 1
    x = 1
    total = n
    while count <= times:
        count += 1
        total = total * x
        total = total % 1000
        x = 13
    print(total)
    """
    last赋初值1
     last=last%1000*n """
