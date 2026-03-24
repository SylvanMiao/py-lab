#三对情侣结婚，给出三条错误消息：
#新郎A说要和新娘X结婚；新娘X说和新郎C结婚；新郎C说和新娘Z结婚
#求出正确的配对

if __name__=="__main__":
    groom=['A','B','C']
    for x in groom:
        for y in groom:
            for z in groom:
                if x!=groom[0] and x!=groom[2] and z!=groom[2] and\
                    x!=y and x!=z and y!=z:
                    print("结果为:")
                    print("新娘X与新郎"+x+"结婚")
                    print("新娘Y与新郎"+y+"结婚")
                    print("新娘Z与新郎"+z+"结婚")
                    
