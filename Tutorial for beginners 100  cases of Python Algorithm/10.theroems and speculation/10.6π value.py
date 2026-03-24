#蒙特卡洛法 求π的近似值
if __name__=="__main__":
    from random import random
    import math
    dots=3000000
    hits=0.0
    for i in range(0,dots):
        #此处默认生成0,1之间的坐标
        x,y=random(),random()
        dist=math.sqrt(x**2+y**2)
        if dist<1.0:
            hits+=1
    pi=4*(hits/dots)
    print(pi)