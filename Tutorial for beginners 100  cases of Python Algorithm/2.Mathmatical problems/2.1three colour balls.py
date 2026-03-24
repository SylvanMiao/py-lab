# 一个口袋中放有12个球，已知其中3个是红的，3个是白的，6个是黑的，现从中任取8个，问一共有多少种可能的颜色搭配
# 不定方程求整数解问题
# 设红球m个，白球n个，则黑球一共8-m-n个

if __name__ == "__main__":
    types = 0
    for m in range(0, 4):
        for n in range(0, 4):
            t = 8 - m - n
            if t <= 6:
                print("红球%d个,白球%d个,黑球%d个" % (m, n, t))
                types += 1
                t += 1
    print("%d种" % types)
