# 10个小孩围成一圈分糖果 分别分得10 2 8 22 16 4 10 6 14 20块糖果。然后所有小孩同时将自己糖果的一半分给右边的小孩
# 糖果数量为奇数的小孩额外获得一个糖果
# 问经过几次之后大家手中的糖果一样多 是多少

if __name__ == "__main__":
    candies = [10, 2, 8, 22, 16, 4, 10, 6, 14, 20]

    def switchcandy(candy):
        half = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
        for i in range(0, len(candy)):
            half[i] = candy[i] // 2
        for i in range(0, len(candy) - 1):
            candy[i] -= half[i]
            candy[i + 1] += half[i]
        candy[9] -= half[9]
        candy[0] += half[9]

    def addcandies(candy):
        for i in range(0, len(candy)):
            if candy[i] % 2 != 0:
                candy[i] += 1

    def judgecandies(candy):
        judge = 0
        for i in range(0, len(candy) - 1):
            if candy[i] == candy[i + 1]:
                judge += 1
            else:
                judge = 0
        return judge

    times = 0
    while 1:
        times += 1
        t = judgecandies(candies)
        if t <= 8:
            switchcandy(candies)
            addcandies(candies)
        else:
            print(times)
            break
    print(candies)
