#数组元素的判断与交换

def swap(x,y):
    temp=color[x]
    color[x]=color[y]
    color[y]=temp

if __name__=="__main__":
    WHITE='W'
    RED='R'
    BLUE='B'
    color=['R','W','B','W','W','B','R','B','W','R']
    w,r,b=0,len(color)-1,0

    for i in range(len(color)):
        print(color[i],end=' ')
    print(' ')



    while w<=r:
        if color[w]==WHITE:
            w+=1
        elif color[w]==BLUE:
            swap(w, b)
            b+=1
            w+=1
        else:
            while w<r and color[r]==RED:
                r-=1
            swap(w, r)
            r-=1
        
    for i in range(len(color)):
            print(color[i],end=' ')
    print(' ')