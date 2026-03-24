#将1,2,3,4,5,6填入2x3的表格中，要求左上方数字比右下方小，问一共有几组填法？

if __name__=="__main__":
    a=[0]*6
    a[0]=1
    a[5]=6
    times=0
    for t in range(2,6):
        a[1]=t
        for x in range(t,6):
            a[2]=x
            for m in range(2,6):
                a[3]=m
                for c in range(m,6):
                    if c>a[1]:
                        a[4]=c
                        if a[1]!=a[2] and a[2]!=a[3] and a[3]!=a[4] and a[1]!=a[3] and a[1]!=a[4] and a[2]!=a[4]:
                            times+=1
                            print("NO.%d arrangement"%times,end='\n')
                            print(' ')
                            for i in range(0,3):
                                print(a[i],end=' ')
                            print(" ")
                            for i in range(3,5):
                                print(a[i],end=' ')
                            print(a[5])
                            print(' ')