# s=1+ 1/1*2+ 1/1*2*3 +...+1/1*2*3*4*...*50

if __name__=="__main__":
    
    denominator=1
    andthem=0
    for i in range(1,51):
        denominator*=i
        andthem+=1/denominator
        
    print(andthem)