#编写程序实现将大于某个整数n且紧靠n的k个素数存入某个数组中，同时实现从INFILE.txt中读取10对
#n 与 k 的值，并将符合要求的素数存入output.txt文件中
import math

def judge_prime(x):
    t=int(math.sqrt(x))+1
    for i in range(2,t):
        if x%i!=0:
            flag=1
        else:
            flag=0
            break
    return flag


#求出紧靠n的k个素数，并存放到数组中
def num(n,k,array):
    i,n=0,n+1
    while k>0:
        if judge_prime(n):
            array[i]=n
            i+=1
            k-=1
        n+=1

# file operation
def filedata():
    array=[0]*1000
    rf=open('infile.txt','r')
    wf=open('outfile.txt','w')
    
    #read 10 (n,k)
    for i in range(10):
            (n,k)=rf.readline().split()
            n=int(n)
            k=int(k)
            num(n, k, array)
            for i in range(k):
                print('%d' %array[i],file=wf,end=' ')
            print(file=wf)
  #关闭文件时code在循环外
    rf.close()
    wf.close()

if __name__=="__main__":
    array=[0]*100
    print("enter n and k :")
    n,k=map(int,input().split())
    num(n, k, array)
    for i in range(k):
        print(array[i],end=' ')
        print('\n')
    filedata()
