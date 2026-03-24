#按递增顺序列出所有分母为40，分子小于40的最简分数
if __name__=="__main__":
    for i in range(1,41):
        if i==1:
            print("%d/40" %i)
        if i >1:
            t=0
            for j in range(2,i+1):
                if 40%j==0 and i%j==0:
                    t=1
            if t==0:
                print("%d/40" %i)