#验证任意奇数平方与1的差是8的倍数
if __name__=="__main__":
    for i in range(1001,2001,2):
        m=i**2-1
        n=m//8
        k=m%8
        print("%d:(%d*%d-1)/8=%d.......%d" %(i,i,i,n,k))