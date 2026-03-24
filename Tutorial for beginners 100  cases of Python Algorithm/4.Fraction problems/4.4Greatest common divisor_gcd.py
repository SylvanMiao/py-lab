# 求任意两个数的最大公因数(gcd)

if __name__== "__main__":

    def printgcd(num1,num2):
        temp=0
        if num1==num2:
            result=num1
        if num1>num2:
            tempp=num2
            while num2>=1:
                t=num1%tempp
                m=num2%tempp
                if t==0 and m==0:
                    result=tempp
                    break
                tempp-=1
        if num2>num1:
            temp=num1
            num1=num2
            num2=temp
            tempp=num2
            while num2>=1:
                t=num1%tempp
                m=num2%tempp
                if t==0 and m==0:
                    result=tempp
                    break
                tempp-=1
        return result
    #辗转相除法原理源于欧几里得几何原本
    def gcm_zhanzhuanxiangchu(num1,num2):
        if num1==num2:
            result=num1
        if num2>num1:
            temp=num1
            num1=num2
            num2=temp
        while num2!=0:
            t=num2
            num2=num1%num2
            num1=t
        resu1t=num1

        return resu1t
    print("enter the two numbers:")
    num1,num2=map(int,input().split())
    print(printgcd(num1, num2))
    print(gcm_zhanzhuanxiangchu(num1, num2))