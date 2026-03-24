#分数比较简单地通分就行
if __name__=="__main__":
    print("请输入第一个分数:")
    a,b=map(int,input().split())
    print("请输入第二个分数:")
    c,d=map(int,input().split())
    print("输入的两个分数分别为: %d/%d %d/%d" %(a,b,c,d))
    m=a*d
    n=c*b
    if m>n:
        print("%d/%d > %d/%d" %(a,b,c,d))
    if m<n:
        print("%d/%d < %d/%d" %(a,b,c,d))
    if m==n:
        print("%d/%d = %d/%d" %(a,b,c,d))