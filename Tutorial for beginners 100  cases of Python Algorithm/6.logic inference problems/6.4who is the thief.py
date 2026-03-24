#4人中有一个人是窃贼
#4人的陈述分别如下：
# 甲：乙没有偷，是丁偷的
# 乙：我没有偷，是丙偷的
# 丙：甲没有偷，是乙偷的
# 丁：我没有偷
# 每人说的话要么都真，要么都假，求出谁是小偷

if __name__=="__main__":
   A,B,C,D=1,0,0,0
   for i in range(1,5):
    if B+D==1 and B+C==1 and A+B==1 and A+B+C+D==1:
        break
    if i==1:
        A=0
        B=1
        print("乙为窃贼")
    if i==2:
        C=1
        B=0
        print("丙为窃贼")
    if i==3:
        C=0
        D=1
        print("丁为窃贼")    
    if i==4:
        print("甲为窃贼")
    print(A,B,C,D)