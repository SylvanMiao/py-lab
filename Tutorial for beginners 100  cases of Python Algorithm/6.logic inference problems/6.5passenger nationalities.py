#利用条件矩阵消去法得到结果
if __name__=="__main__":
    def nationality():
        #initialize matrix
        a=[]
        for i in range(7):
            b=[]
            for j in range(7):
                b.append(j)
            a.append(b)
        for i in range(1,7):
            a[0][i]=1

        #enter significance
        a[1][1]=a[2][1]=a[3][1]=a[5][1]=0
        a[1][3]=a[2][3]=a[3][3]=0
        a[1][4]=a[2][4]=a[3][4]=a[5][4]=a[6][4]=0
        a[3][5]=0
        a[1][6]=a[3][6]=a[5][6]=0

        x=0
        y=0
        while a[0][1]+a[0][2]+a[0][3]+a[0][4]+a[0][5]+a[0][4]>0:
            for i in range(1,7):
                if a[0][i]!=0:
                    e=0
                    for j in range(1,7):
                        if a[j][i]!=0:
                            x=j
                            y=i
                            e+=1
                    if e==1:
                        for t in range(1,7):
                            if t!=i:
                                a[x][t]=0
                        a[0][y]=0
        #final result
        for i in range(7):
            print(a[i])
        
        
    nationality()


 