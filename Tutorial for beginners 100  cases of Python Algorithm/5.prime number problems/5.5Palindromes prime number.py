#是回文数且是素数
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
    #输出逆序数函数
    def reversenum(x):
        sum=0
        while x!=0:
            m=x%10
            sum=(sum+m)*10
            x//=10
        sum//=10
        return sum

    for i in range(1,1001):
        t=reversenum(i)
        if t==i and prime_judge(t)==1:
            print(t,end=",")