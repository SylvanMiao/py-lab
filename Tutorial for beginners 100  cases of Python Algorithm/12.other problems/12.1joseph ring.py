#十七世纪的法国数学家加斯帕在《数目的游戏》中讲到一个故事：十五个教徒和十五个教徒在海上遇险，必须将一半的人
#投入海中，其余的人才能幸免于难。于是想了一个办法：将三十个人围成一个圆圈，从第一个人依次开始报数，每数到第九个人就把
#他投入大海，如此循环直到仅剩15个人为止。问怎样的排法才能使每次被投入大海的都是异教徒

if __name__=="__main__":
    array=[[0]*2 for i in range(31)]
    print("最终结果为:")
    for i in range(1,31):
        array[i][0]=1
        array[i][1]=i+1
    array[30][1]=1

    j=30

    for i in range(15):
        k=0
        while True:
            if k<9:
                j=array[j][1]
                k+=array[j][0]
            else:
                break
        array[j][0]=0

    for i in range(1,31):
        if array[i][0]==0:
            print("0",end=" ")
        if array[i][0]==1:
            print("amen",end=" ")
    print()
        