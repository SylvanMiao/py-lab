#四方定理是数论中的重要定理，它可以叙述为“所有的自然数至多用4个数的平方和就可以表示出来”
if __name__=="__main__":
    n=int(input("enter one number:"))
    for i in range(0,n//2+1):
        for j in range(0,i+1):
            for k in range(0,j+1):
                for m in range(0,k+1):
                    if i**2+j**2+k**2+m**2==n:
                        print("%d=%d+%d+%d+%d" %(n,i**2,j**2,k**2,m**2))