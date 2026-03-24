#孪生素数是指相邻的两个均为奇数的素数
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
    count=0
    for i in range(1,998):
        if prime_judge(i)==1 and prime_judge(i+2)==1:
            print("(%d,%d)" %(i,i+2),end="")
            count+=1
            if count%5==0:
                print()