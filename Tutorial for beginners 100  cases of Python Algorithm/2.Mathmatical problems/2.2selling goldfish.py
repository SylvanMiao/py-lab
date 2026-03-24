# 一桶金鱼分5次出售，第一次卖出全部的二分之一加二分之一条，第二次卖出剩下的三分之一加三分之一条。。。第四次买完后，第五次卖出11条，求原来一共有多少条金鱼
if __name__ == "__main__":
    original = 23
    flag = 1

    while flag == 1:
        sell_time = 0
        total = original
        for i in range(1, 5):
            if (total + 1) % (i + 1) == 0:
                total -= (total + 1) // (i + 1)
                sell_time += 1
        if total == 11 and sell_time == 4:
            flag = 0
            print(original)
        """ else:
            sell_time = 0 """
        original += 2
