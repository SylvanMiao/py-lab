#编写脚本模拟福利彩票双色球开奖过程，有程序生成6个红色球和1个蓝色球。
#程序要求开出的红色球号码不能重复，但蓝色球可以是红色球中的一个
# 红色球的范围是1~33，蓝色球的范围是1~16


import random

if __name__=="__main__":
    
    red=[1]*6
    i=0
    j=0
    while i<6:
        tmp=random.randint(1, 33)
        while j<i:
            if tmp==red[j]:
                break
            j+=1
        if j==i:
            red[i]=tmp
        i+=1
    print("red: ")
    print(red)

    f=random.randint(1, 6)
    print("blue: \n[%d]" %f)