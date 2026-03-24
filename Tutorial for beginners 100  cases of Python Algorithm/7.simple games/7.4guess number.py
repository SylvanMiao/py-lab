import random

if __name__=="__main__":
    com_num=random.randint(1000, 10000)
    print("computer has come up with a number")
    print(" ")
    l=[0]*4
    times=1

    
    while True:
        a=com_num
        b=int(input("please enter one number:"))
        address_correct=0
        number_correct=0
        l[0]=l[1]=l[2]=l[3]=0
        for i in range(1,5):
            m=a%10
            t=b
            flag=1
            for j in range(1,5):
                n=t%10
                if flag and n==m and j!=l[0] and j!=l[1] and j!=l[2] and j!=l[3]:
                    number_correct+=1
                    flag=0
                    l[number_correct-1]=j
                    if i==j:
                        address_correct+=1
                t//=10
            a//=10
        times+=1
        print("address correct:%d  number correct:%d" %(address_correct,number_correct))
        if address_correct==4:
            print("you won")
            print(" ")
            break
    
    print("total trials: %d" %times)