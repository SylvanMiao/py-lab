#编写脚本在字符串中的数字前面添加一个美元符号
def fun(s):
    a=[0]*len(s)
    for i in range(len(s)):
        a[i]=s[i]
    
    for item in a:
        if item.isdigit() ==True:
            item='$'+item
        print(item,end='')


if __name__=="__main__":
    s=str(input("pkease enter one string:"))
    print(s)
    fun(s)