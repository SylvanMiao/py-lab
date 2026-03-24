def drawdiamond(n):
    for i in range(1,n+1):
        for j in range(1,(n+i-1)+1):
            if j == n+1-i or j==n-1+i:
                print("*",end="")
            else:
                print(" ",end="")
        print()
    
    for i in range(1,n):
        for j in range(1,(2*n-1-i)+1):
            if j==1+i or j==2*n-i-1:
                print("*",end="")
            else:
                print(" ",end="")
        print()


if __name__=="__main__":
   

    n=int(input("输入行数:"))
    drawdiamond(n)