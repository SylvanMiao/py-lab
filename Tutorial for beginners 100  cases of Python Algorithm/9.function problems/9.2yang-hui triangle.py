#在屏幕上打印杨辉三角形，又称帕斯卡三角形，是二项式系数在三角形中的一种几何排列
#递归思想
def c(x,y):
    if y==1 or y==x:
        return 1
    else:
        return c(x-1,y-1)+c(x-1,y)
if __name__=="__main__":
    n=int(input("enter one number:"))
    for i in range(1,n+1):
        for j in range(0,n-i+1):
            print("   ",end=' ')
        for j in range(1,i+1):
            print("%6d "%c(i,j),end=" ")
        print( )