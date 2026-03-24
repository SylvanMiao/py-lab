#将不超过1993的所有素数从小到大排成第一行,第二行上的每一个数都等于它上面两个相邻素数之差.
# 求出第二行是否存在若干个连续的整数,它们的和正好是1898
if __name__=="__main__":
    import math
    sum=0
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
    m=[]
    n=[]
    for i in range(2,1994):
        if prime_judge(i)==1:
            m.append(i)
    print(m)
    for j in range(0,len(m)-1):
        t=m[j+1]-m[j]
        n.append(t)
    print(n)
    for item in m:
        while item>1898:
            for thing in m:
                if item-thing==1898:
                    print("%d,%d" %(thing, item))
                    break
            break

