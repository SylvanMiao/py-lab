#A,B,C三人打鱼，共21个箩筐，7个装满鱼，7个半满，7个空的，如何平分
if __name__=="__main__":
    print("分鱼的方案如下:")
    count=0
    a=[[0]*3 for i in range(3)]

    for i in range(4):
        a[0][0]=i
        j=i
        while j<=7-i and j<=3:
            a[1][0]=j
            a[2][0]=7-j-a[0][0]
            j+=1
            if a[2][0]>3:
                continue
            if a[2][0]<a[1][0]:
                break
            for k in range(1,6,2):
                a[0][1]=k
            for m in range(1,7-k,2):
                a[1][1]=m
                a[2][1]=7-k-m           
                flag,n=True, 0
                while flag and n<3:
                    if a[n][0]+a[n][1]<7 and a[n][0]*2+a[n][1]==7:
                        a[n][2]=7-a[n][0]-a[n][1]
                    else:
                        flag=False
                    n+=1               
                if flag:
                    count+=1
                    print('No.',count,"    full  half empty")
                    for n in range(3):
                        print('fisher',chr(65+n),':',a[n][0],'   ',a[n][1], '   ',a[n][2])