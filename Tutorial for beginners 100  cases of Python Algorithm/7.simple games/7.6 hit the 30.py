import random


def input_funtion(m):
    t=int(input("please enter one number:"))
    while t>2 or t<1 or 30-t<0:
        print("error enter again")
        t=int(input("please enter one number:"))
    print("you count to %2d" %(m+t))
    x=m+t
    return x

def com_function(x):
    if (30-x)%3==0:
        n=random.randint(1, 2)
    else:
        n=(30-x)%3
    print("computer count to:%2d" %(x+n))
    w=x+n
    return w




if __name__=="__main__":
    first_=random.randint(1, 2)
    sum_=0
    while sum_<30:
        if first_==1:
            sum_=input_funtion(sum_)
            sum_=com_function(sum_)
        if first_==2:
            sum_=com_function(sum_)
            sum_=input_funtion(sum_)
            
    