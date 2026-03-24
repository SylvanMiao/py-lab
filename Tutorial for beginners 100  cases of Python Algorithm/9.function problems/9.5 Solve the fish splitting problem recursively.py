#A,B,C,D,E五个人合伙夜间钓鱼，捕到鱼之后都去休息了，早上A第一个醒来，他将鱼平均分为5份，将多余的一条扔回河里，然后拿着自己的一份回家
#B第二个醒过来，又将剩下的平均分成5份并拿自己的一份回家了，C,D,E依次如此，问这五个人至少捕获多少条鱼，每人醒来后看到的鱼是多少

def getfish(n,x):
    if (x-1)%5==0:
        if n==1:
            return 1
        else:
            return getfish(n-1, (x-1)//5*4)
    return 0
    

if __name__=="__main__":
    n=5
    i=0
    flag=0
    while True:
        if flag!=1:
            i+=1
            x=i*5+1
            if getfish(n, x):
                flag=1
                print("total number:",x)
                exit()
    