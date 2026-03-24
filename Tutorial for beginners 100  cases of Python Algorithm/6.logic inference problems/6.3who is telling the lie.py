#三人A,B,C,A说B在说谎,B说C在说谎,C说AB都在说谎
#求出谁在说谎

if __name__=="__main__":
    #x,y,z分别代表三人说话的真假情况，1为真0为假
    for x in range(2):
        for y in range(2):
            for z in range(2):
                if (x and (not y) or (not x) and y) and (y and (not z) or (not y) and z)\
                    and (z and x==0 and y==0 or(not z) and x+y!=0):

                    a='真' if x==1 else '假'
                    b='真' if y==1 else '假'
                    c='真' if z==1 else '假'
                    
                    print(" A说的是"+ a +"话")
                    print(" B说的是"+ b +"话")
                    print(" C说的是"+ c +"话")
