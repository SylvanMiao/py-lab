def sortscore(psn,n):
    for i in range(n-1):
        for j in range(n-1-i):
            if psn[j][1]>psn[j][1]:
                tmp=psn[j]
                psn[j]=psn[j+1]
                psn[j+1]=tmp

def sortrand(psn,n):
    j=1
    min_=10
    psn[0][2]=1
    for i in range(n):
        if psn[i][1]!=psn[i-1][1]:
            psn[i][2]=j
            j+=1
        else:
            psn[i][2]=psn[i-1][2]


def sortnum(psn,n):
    for i in range(n-1):
        for j in range(n-1-i):
            if psn[j][0]>psn[j+1][0]:
                tmp=psn[j]
                psn[j]=psn[j+1]
                psn[j+1]=tmp

if __name__=="__main__":
    print("num  score  rank")
    psn=[[1,5,0],[2,3,0],[3,4,0],[4,7,0],[5,3,0],[6,5,0],[7,6,0]]
    n=7
    sortrand(psn, n)
    sortscore(psn, n)
    sortnum(psn, n)
    for item in psn:
        print(item,end=' \n')