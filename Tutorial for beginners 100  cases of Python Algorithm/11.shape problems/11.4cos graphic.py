#0~360 cos 曲线

if __name__=="__main__":
    import turtle
    import numpy as np
    import matplotlib.pyplot as plt
    X=np.linspace(0,2*np.pi,100)
    Y=np.cos(X)

    #正常显示中文
    plt.rcParams['font.sans-serif']=['SimHei']
    #正常显示负号
    plt.rcParams['axes.unicode_minus']=False
    plt.plot(X,Y,linewidth=4)
    plt.plot(X,Y,'g')
    plt.title("余弦曲线")
    


    plt.show()