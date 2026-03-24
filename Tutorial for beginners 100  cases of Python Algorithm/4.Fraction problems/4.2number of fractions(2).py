#按递增顺序列出所有分母为40，分子小于40的最简分数
#利用最大公约数的方法定义辗转相除法函数
if __name__=="__main__":
    #辗转相除的具体原理在书上4.4
    def zhanzhuanxiangchu_answer(num1,num2):
        while num2!=0:
            temp=num1%num2
            num1=num2
            num2=temp
        return num1
for i in range(1,41):
    m=zhanzhuanxiangchu_answer(i, 40)
    if m==1 :
        print("%d/40" %i)