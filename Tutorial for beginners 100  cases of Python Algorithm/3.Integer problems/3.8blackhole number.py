# 求三位数黑洞数，指将任何一个数字不全相同的数字三位重新排列之后，最大的结果减去最小的结果得到的一些数
if __name__ == "__main__":
    # 判断是否三位数不完全相同
    def judgesame(x):
        if x < 1000 and x >= 100:
            a = x // 100
            b = (x - 100 * a) // 10
            c = x % 10
            if a == b and b == c:
                return 0
            else:
                return 1

    # 重新排列函数并求差值
    def rearrange(x):
        a = x // 100
        b = (x - 100 * a) // 10
        c = x % 10
        m = [a, b, c]
        for j in range(0, 2):
            for i in range(1, 3):
                if m[i] > m[i - 1]:
                    t = m[i - 1]
                    m[i - 1] = m[i]
                    m[i] = t
        max = m[0] * 100 + m[1] * 10 + m[2]
        min = m[2] * 100 + m[1] * 10 + m[0]
        difference = max - min
        return difference

    save = []
    for i in range(1, 1000):
        if judgesame(i):
            while rearrange(i) != i:
                i = rearrange(i)
            t = rearrange(i)
            save.append(t)
            for i in save:
                if i == t:
                    break
                else:

                    print(t)
    print(save[0])
