#角谷猜想：任给一个自然数，若为偶数则除以2，若为奇数则乘以三再加一，如此循环下去最终可以得出1
if __name__=="__main__":
    n=int(input("enter one number:"))
    print(n,end='')
    
    while n!=1:
        if n%2==0:
            n//=2
            print("-->%d"%n,end='')
        elif n%2==1:
            n=n*3+1
            print("-->%d"%n,end='')