if __name__=="__main__":
    import matplotlib.pyplot as plt
    #正常显示中文
    plt.rcParams['font.sans-serif']=['SimHei']
    labels='香蕉','苹果','雪梨','西瓜','葡萄'
    size=[10,15,8,62,5]
    explodes=(0,0,0,0.1,0)
    fig1,axl=plt.subplots()
    axl.pie(size,explode=explodes,labels=labels,autopct='%1.1f%%',shadow=True,startangle=90)
    axl.axis('equal')
    plt.title("水果销量表")
    plt.show()