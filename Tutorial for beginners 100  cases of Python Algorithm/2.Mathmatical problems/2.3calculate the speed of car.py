# 司机看见仪表盘上的里程数为95859，两小时后一表盘上出现了新的五位数对称数
if __name__ == "__main__":
    flag = 1
    i = 95860

"""  while i >= 95860 and i <= 100000:
        a = int(i // 10000)
        b = int((i % 10000) // 1000)
        c = int((i % 1000) // 100)
        d = int((i % 100) // 10)
        e = int(i % 10)
        if a == e and b == d:
            print(i)
            break
        i += 1
    print("车速为：%d" % ((i - 95859) / 2.0))
 """

x = [0, 0, 0, 0, 0]
while 1:
    t = 0
    K = 100000
    while K >= 10:
        x[t] = (i % K) // (K // 10)
        K /= 10
        t += 1
    if x[0] == x[4] and x[1] == x[3]:
        print("%.2f" % ((i - 95859) / 2.0))
        break
    i += 1
