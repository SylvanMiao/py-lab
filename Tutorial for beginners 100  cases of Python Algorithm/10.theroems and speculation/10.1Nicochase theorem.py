#任何一个整数的立方都可以表示成一连串连续奇数的和(以正数为例)
if __name__=="__main__":
    n=int(input("enter one number:"))
    cube=n**3
    i=1
    while i<cube:
        sum=0
        j=i
        while j<cube:
            
            sum +=j
            if sum==cube:
                print("%d=%d+%d+......%d"%(cube,i,i+2,j))
            if sum>cube:
                
                break
            j+=2
        i+=2