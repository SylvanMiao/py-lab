#梅森素数是指满足形式为2**n-1的素数(指数也为素数)
#求出指数<20的所有梅森素数
if __name__=="__main__":
    import math
    #判断是否为素数的函数
    def prime_judge(x):
        flag=0
        m=math.sqrt(x)
        i=2
        while i<=m:
            if x%i==0:
                flag=1
                break
            i+=1
        if flag==0:
            return 1
        else:
            return 0

    for i in range(2,50):
        if prime_judge(i)==1:
            mp=2**i-1
            if prime_judge(mp)==1:
                print(mp)