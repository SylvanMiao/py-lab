#邮局有四种不同面值的邮票，在每个信封上可以贴5张邮票，面值可以相同也可以不相同
#但至少要贴3种不同面值的邮票，问这四种邮资能做到的最大的价钱是多少

if __name__=="__main__":
    a,b,c,d=map(int, input("enter value:").split(' '))
    stamp=[]
    max_=0
    j=0
    for i in (a,b,c,d):
        stamp.append(i)
    stamp.sort(reverse=True)
    print(stamp)
    print("max value:%d" %(stamp[0]*3+stamp[1]*2))