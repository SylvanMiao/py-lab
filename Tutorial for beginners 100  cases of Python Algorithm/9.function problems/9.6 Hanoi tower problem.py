#汉诺塔是一个古典的数学问题，只能用递归方式来解决，在古代有一个梵塔，塔内有A,B,C三个座。开始时A座上有64
#个盘子，大的在下，小的在上，大小各不相同，不改变这个规则将A座上的盘子按同样顺序移动到C座上，打印出步骤。

def hanoi(N,A,B,C):
    if N==1:
        print("move dish %d from %c to %c" %(N,A,C))
    else:
        hanoi(N-1,A,C,B)
        print("move dish %d from %c to %c" %(N,A,C))
        hanoi(N-1, B, A, C)

if __name__== "__main__":
    n=int(input("please enter the number of dishes:"))
    print("the steps to move %2d dishes are:")
    hanoi(n, 'A', 'B', 'C')