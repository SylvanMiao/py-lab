import random
def p(b,n):
    print("\n♠",end=' ')
    for i in range(13):
        if b[i]//13==0:
            print(n[b[i]%13],end=' ')

    print("\n♥",end=' ')
    for i in range(13):
        if b[i]//13==1:
            print(n[b[i]%13],end=' ')


    print("\n♦",end=' ')
    for i in range(13):
        if b[i]//13==2:
            print(n[b[i]%13],end=' ')
            

    print("\n♣",end=' ')
    for i in range(13):
        if b[i]//13==3 or b[i]//13==4:
            print(n[b[i]%13],end=' ')
            
    print()

if __name__=="__main__":
    n=['2','3','4','5','6','7','8','9','T','J','Q','K','A']
    a=[0]*53
    b1=[0]*13
    b2=[0]*13
    b3=[0]*13
    b4=[0]*13

    b11,b22,b33,b44,t=0,0,0,0,1        
    while t<=52:
        m=random.randint(0, 52)
        flag,i=True,1
        while i<=t and flag:
            if m==a[i]:
                flag=0   
            i+=1

        if flag:
            a[t]=m
            t+=1

            if t%4==0:
                b1[b11]=a[t-1]
                b11+=1
            
            if t%4==1:
                b2[b22]=a[t-1]
                b22+=1
            
            if t%4==2:
                b3[b33]=a[t-1]
                b33+=1

            if t%4==3:
                b4[b44]=a[t-1]
                b44+=1

    b1=sorted(b1,reverse=True)
    b2=sorted(b2,reverse=True)
    b3=sorted(b3,reverse=True)
    b4=sorted(b4,reverse=True)

    p(b1,n)
    p(b2,n)
    p(b3,n)
    p(b4,n)