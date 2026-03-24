#真分数是指分子比分母小的分数，埃及分数是指分子是1的分数
if __name__=="__main__":
    print("输入一个分数：" ,end=" ")
    a,b=map(int, input().split())
    print("分解后的埃及分数为:", end=" ")
    while 1:
        if b%a==0:
            c=b//a
            a=1
        else:
            c=b//a+1
        if a==1:
            print("1/%ld\n" %c,end="")
            break
        else:
            print("1/%ld + " %c,end="")
        a=a*c-b
        b=b*c
        if a==3 and b%2==0:
            print("1/%ld +1/%ld\n" %(b//2,b))
            break
        