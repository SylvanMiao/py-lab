#一次只能移动一个棋子，棋子可以向空格中移动，也可以跳过一个对方的棋子进入空格，白棋子只能向右移动，黑棋子只能向左移动
#不能跳过两个棋子
def printline(a):
    global number
    print("NO.%2d:" %number)
    number+=1
    print(" ",end=' ')
    for i in range(7):
        if a[i]==1:
            print("♠",end=' ')
        else:
            if a[i]==2:
                print("♥",end=' ')
            else:
                print("__",end=' ')
    print("\n..................\n")          


def change(t,i,j):
    term=t[i]
    t[i]=t[j]
    t[j]=term
    return t
if __name__=="__main__":
    t=[1,1,1,0,2,2,2]
    number=0
    printline(t)
while t[0]+t[1]+t[2]!=6 or t[4]+t[6]+t[5]!=3:
    flag=True

    i=0
    while flag and i<5:
        if t[i]==1 and t[i+1]==2 and t[i+2]==0:
            t=change(t, i, i+2)
            printline(t)
            flag=False
        i+=1
    
    i=0
    while flag==True and i<5:
        if t[i]==0 and t[i+1]==1 and t[i+2]==2:
            t=change(t, i, i+2)
            printline(t)
            flag=False
        i+=1
    
    i=0
    while flag==True and i<6:
        f=True
        if i<5:
            f=t[i-1]!=t[i+2]
        if t[i]==1 and t[i+1]==0 and (i==0 or f):
            t=change(t, i, i+1)
            printline(t)
            flag=False
        i+=1

    i=0
    while flag==True and i<6:
        f=True
        if i<5:
            f=t[i-1]!=t[i+2]
        if t[i]==0 and t[i+1]==2 and (i==5 or f):
            t=change(t, i, i+1)
            printline(t)
            flag=False
        i+=1