#一个四位数经过取四位运算之后，再经过某种运算后总是得到6174这个数，编程进行验证

def split(x):
    l=[]
    a=x%10
    b=x//10%10
    c=x//100%10
    d=x//1000
    l.append(a)
    l.append(b)
    l.append(c)
    l.append(d)
    return l

def calculatemax(s):
    s.sort(reverse=True)
    max_num=s[0]*1000+s[1]*100+s[2]*10+s[3]
    return max_num


def calculatemin(s):
    s.sort(reverse=False)
    min_num=s[0]*1000+s[1]*100+s[2]*10+s[3]
    return min_num

if __name__=="__main__":
    x=int(input("enter one 4-num number:"))
    m=split(x)
    print(m)
    c=x
    while c!=6174:
        a=calculatemax(m)
        b=calculatemin(m)
        c=a-b
        print(a,b,c)
        m=split(c)