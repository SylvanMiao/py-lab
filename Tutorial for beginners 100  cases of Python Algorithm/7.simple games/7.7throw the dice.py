import random
import time

if __name__=="__main__":
    times=0
    sum1=sum2=0
    while times<=99:
        m=random.randint(1, 6)
        n=random.randint(1, 6)
        sum1+=m
        sum2+=n
        times+=1
    if m>n:
        print("you win")
    else:
        print("you lose")