#有5个人坐在一起，问第五个人多少岁，他说比第四个人大两岁，问第四个人说比第三个人大两岁，直到问第一个人说自己10岁
#求出当输入某个人时其对应的年龄

def calculateage(n):
    if n==1:
        age=10
    elif n>5:
        print("error enter again")
        age=1000000
    else:
        age=calculateage(n-1)+2
    
    return age


if __name__=="__main__":
    while True:
            
        n=int(input("enter the person:"))
        m=calculateage(n)
        print("the age is ",m)