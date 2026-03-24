# 魔术师将一副牌中的13张黑桃按一定顺序放置，从最上面的一张开始数，第一张翻过来为A，将A放桌上(最下面)，按从上到下的顺序数2张牌
# 第二张翻过来正好是2，将这两张放在A上面，之后再进行同样操作，依次将13张牌全部翻出来
# 问原始排序

# 将牌堆看做首尾相连的圆圈，翻过来的牌不重新计数
if __name__ == "__main__":
    # 定义初始空数组
    card = [0] * 14
    j = 1
    # i:牌的序号  j:位置的序号
    for i in range(1, 14):
        invalidtimes = 0
        while invalidtimes < i:
            if j > 13:
                j = 1
            if card[j]:
                j += 1
            else:
                if invalidtimes == i - 1:
                    card[j] = i
                j += 1
                invalidtimes += 1
    print(card[1:])
