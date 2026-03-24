#假设有张、李、王三家，每家有三个孩子。某一天，这三家的9个孩子一起举行跑步比赛，第一名得9分，第二名得8分，第三名得7分，以此类推
##比赛结束后发现三家孩子的总分是相同的，已知名次不并列，同一家不会出现相连的名次。
#且第一名为李家的孩子，第二名为王家的孩子，求出最后一名是谁家的孩子，

if __name__=="__main__":
    #(1+9)*4.5/3=15,由此可知第三名为张家的孩子，否则总分超过15分
    score=[([0]*4)for i in range(4)]
    #zhang
    score[1][1]=7
    #wang
    score[2][1]=8
    #li
    score[3][1]=9
    for zhang in range(4,6):
        for wang in range(4,7):
            for li in range(4,7):
                if zhang!=wang and li!=zhang and li!=wang\
                    and 15-zhang-score[1][1]!=15-wang-score[2][1]\
                        and 15-zhang-score[1][1]!=15-li-score[3][1]\
                            and 15-wang-score[2][1]!=15-li-score[3][1]:
                            score[1][2]=zhang
                            score[1][3]=15-zhang-7
                            score[2][2]=wang
                            score[2][3]=15-wang-8
                            score[3][2]=li
                            score[3][3]=15-li-8
    for i in range(1,4):
        for j in range(1,4):
            print(score[i][j],end=" ")
        print( )
    #结果可见1分的在第二行，即王家