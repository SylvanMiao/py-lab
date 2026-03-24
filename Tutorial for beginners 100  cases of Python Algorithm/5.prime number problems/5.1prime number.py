#求给定范围内的所有素数
if __name__=="__main__":
    import math
    n=int(input())
    count=0
    for j in range(1,n+1):      
        flag=1
        m=math.sqrt(j)
        i=2
        while i<=m:
            if j%i==0:
                flag=0
                break
            i+=1
        if flag!=0:
            count+=1
            print(j,end=",")
    print("共有%d个素数" %count)
