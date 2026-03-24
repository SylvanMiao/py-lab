#现在有一串字符需要输入，规定输入的字符里只能含有字母和“*“符号。请编写程序实现除了将字符整体签后的星号之外，将其他所有字符都删除的
#效果

def fun(s):
    a=[0]*len(s)
    for i in range(len(s)):
        a[i]=s[i]
    
    for item in a:
        if item =='*':
            item=""
        print(item,end='')


if __name__=="__main__":
    s=str(input("pkease enter one string:"))
    print(s)
    fun(s)