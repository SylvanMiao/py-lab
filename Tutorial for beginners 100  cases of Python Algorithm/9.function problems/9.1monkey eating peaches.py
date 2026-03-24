#一个猴子摘了一些桃子，第一天吃了其中的一半然后多吃了一个，第二天吃了剩下的一半再多吃一个
#一直到第十天重复如此吃完后发现只剩一个桃子了，求一共有多少个桃子
def calculate_peach(x):
    t=(x+1)*2
    return t
if __name__=="__main__":
    sum_peach=1
    times=1
    while times<=10:
        sum_peach=calculate_peach(sum_peach)
        times+=1
    print("peaches numbers:%d"%sum_peach)