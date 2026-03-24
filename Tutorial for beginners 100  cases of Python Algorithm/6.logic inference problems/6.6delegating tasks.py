#基本同6.2;某项任务需要在ABCDEF这六个人中挑选人来完成、
#AB两人至少去一个人
#AD不同时去
#AEF三个人要挑选两个人去
#BC同时去或者都不去
#如果D不去，那么E也不去
#CD两人中只能去一个
if __name__=="__main__":
    
    for A in range(2):
        for B in range(2):
            for C in range(2):
                for D in range(2):
                    for E in range(2):
                        for F in range(2):
                            if A+B>=1 and A+D<=1 and A+E+F==2\
                                and B+C!=1 and ((D==0 and E==0) or(D==1)) and C+D==1:
                                print(A,B,C,D,E,F)
