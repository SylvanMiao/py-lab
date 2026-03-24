#2000以内的不小于4的正偶数都能够分解为两个素数之和(proof)
if __name__=="__main__":
    import math
    count=0
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
    for i in range(4,2002,2):
        for j in range(2,i//2+1):
            if prime_judge(j)==1 and prime_judge(i-j)==1:
                print("%d = %d + %d " %(i,j,i-j))
                count+=1
                break
    if count==(2000-4)//2+1:
        print("Q.E.D")         
    