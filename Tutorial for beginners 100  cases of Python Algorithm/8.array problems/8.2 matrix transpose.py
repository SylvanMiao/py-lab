#3x3二维矩阵转置
if __name__=="__main__":
    n=[[1,2,3],[4,5,6],[7,8,9]]
    print("原始矩阵")
    for i in range(3):
        for j in range(3):
            print("%d "%(n[i][j]),end=' ')
        print()
   
    print("转置后的矩阵")
    for i in range(3):
        for j in range(3):
            if i>j:
                temp=n[i][j]
                n[i][j]=n[j][i]
                n[j][i]=temp
    for i in range(3):
        for j in range(3):
            print("%d "%(n[i][j]),end=' ')
        print()