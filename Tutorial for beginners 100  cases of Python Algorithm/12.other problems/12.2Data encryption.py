#某个公司采用公用电话来传递数据，传递的数据是4位的整数，且要求在传递过程中数据是加密的。
#数据加密的规则是：将每位传递的数字都加上5，之后用和除以10的余数来代替该数字，最后将第一位和第四位数字交换，第二位和第三位
#交换，程序实现数据加密的过程

def encry(n):
    t=0
    s=[0]*4
    s[0]=n%10
    s[1]=n//10%10
    s[2]=n//100%10
    s[3]=n//1000

    for i in range(4):
        s[i]+=5
        s[i]%=10

    t=s[0]
    s[0]=s[3]
    s[3]=t

    t=s[2]
    s[2]=s[1]
    s[1]=t

    return s

if __name__=="__main__":
    n=int(input("please enter one number:"))
    print(n)
    print(encry(n)) 
