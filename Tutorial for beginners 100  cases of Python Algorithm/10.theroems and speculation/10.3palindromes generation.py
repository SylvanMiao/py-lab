#任意1个十进制整数，将其倒过来之后与原来的正整数相加，重复以上步骤后最终可以得到一个回文数
#请验证

def reverse(x):
    t=10
    sum=0
    while x>0:
        m=x%10
        sum=sum*t+m    
        x//=10
    return sum


if __name__=="__main__":
    while 1:
        n=int(input("enter one number:"))
        times=0
        while reverse(n)!=n:
            n+=reverse(n)
            times+=1
        print(n,times)