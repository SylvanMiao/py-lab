# 求任意两个数的最大公因数(gcd)

if __name__== "__main__":
    
        """ #辗转相除法原理源于欧几里得几何原本
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

            return resu1t """

        
        print("enter the two numbers:")
        num1,num2=map(int,input().split())

        if num1==num2:
            i=num1
        if num2>num1:
            temp=num1
            num1=num2
            num2=temp
            i=num1
        while 1:
            
            if i%num1==0 and i%num2==0:
                print(i)
                break
            i+=1


            """ print(gcm_zhanzhuanxiangchu(num1, num2)) """