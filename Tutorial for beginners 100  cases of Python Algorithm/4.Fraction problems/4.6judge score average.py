#去掉一个最高分和一个最低分之后求平均值

if __name__=="__main__": 
    import random 
    print("评委打分为:")
    #生成随机数组
    a=[]
    for i in range(10):
        a.append(random.randint(80,100))
    print(a)
    #找出最大值和最小值
    max_=0
    for item in a:
        if item>max_:
            max_=item
    min_=10
    for item in a:
        if item<min_:
            min_=item
    #数组求和并减去最大最小值
    sum_=0
    for i in a:
        sum_+=i
    print("去掉一个最高分:%d" %max_)
    print("去掉一个最高分:%d" %min_)
    print("最后得分为：")
    print((sum_-max_-min_)/len(a))