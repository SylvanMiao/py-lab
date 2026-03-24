#按照一定规律排放的一些数
def array(n):
    if n%2==0:
        n=n+1
    max_=n*n
    mtrx=[1]*max_
    mtrx[n//2]=1
    i=0
    j=n//2

    for num in range(2,max_+1):
        i=i-1
        j=j+1
        if (num-1)%n==0:
            i=i+2
            j=j-1
        if i<0:
            i=n-1
        if j>n-1:
            j=0
        no=i*n+j
        mtrx[no]=num

    print("%d-class:" %n,end=' ')
    no=0
    for i  in range(0,n):
        print()
        for j in range(0,n):
            print("%3d" %mtrx[no],end=' ')
            no+=1
    print()

if __name__=="__main__":
        n=int(input("enter one number:"))
        array(n)