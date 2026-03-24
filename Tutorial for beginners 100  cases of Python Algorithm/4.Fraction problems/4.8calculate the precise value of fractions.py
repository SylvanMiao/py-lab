#分数皆为有理数，即有限小数或者无限循环小数；我们可以利用数组来求出第一循环节
if __name__=="__main__":
    n=int(input("请输入分子:"))
    m=int(input("请输入分母:"))
    print("输入的分数为:%d/ %d" %(n,m))
    a=[]
    b=[]
    x=n//m
    y=n%m
    t=0
    while t<=1:
        a.append(x)
        b.append(y)
        y*=10
        x=y//m
        y=y%m
        if y==0:
            a.append(x)
            break
        if y!=0:
            for item in b:
                if y==item:
                    t+=1
    print("该分数的理想值为:")
    print(int(a[0]),end="") 
    print(".",end="")
    for item in a[1:]:
            print(item,end="")
    