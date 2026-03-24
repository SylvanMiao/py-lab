def Newtons_method(a, b, c, d):
    x = 1.5
    x0 = x
    f = a * x0 * x0 * x0 + b * x0 * x0 + c * x0 + d
    fd = 3 * a * x0 * x0 + 2 * b * x0 + c
    x = x0 - f / fd
    while abs(x - x0) >= 1e-5:
        x0 = x
        f = a * x0 * x0 * x0 + b * x0 * x0 + c * x0 + d
        fd = 3 * a * x0 * x0 + 2 * b * x0 + c
        x = x0 - f / fd

    return x


print("请输入方程系数：")
a, b, c, d = map(float, input().split())
x = Newtons_method(a, b, c, d)
print(x)
