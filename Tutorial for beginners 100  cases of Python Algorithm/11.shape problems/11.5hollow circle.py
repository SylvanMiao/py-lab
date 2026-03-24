if __name__=="__main__":
    import numpy 
    import matplotlib.pyplot as plt
    #正常显示中文
    plt.rcParams['font.sans-serif']=['SimHei']
    #正常显示负号
    plt.rcParams['axes.unicode_minus']=False

    r=2.0
    a,b=(0.,0.)
    circle=numpy.arange(0,2*numpy.pi,0.01)
    x=a+r*numpy.cos(circle)
    y=b+r*numpy.sin(circle)
    fig=plt.figure()
    axes=fig.add_subplot(111)
    axes.axis('equal')
    axes.plot(x,y)
    plt.title("circle")
    plt.show()
