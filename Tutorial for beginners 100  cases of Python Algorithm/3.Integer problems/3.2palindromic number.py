# print所有的水仙花数，即一个三位数，将其三个位置上的数字自乘三次后相加刚好等于自身的数
if __name__ == "__main__":
    for i in range(100, 1000):
        sum = 0
        hundred = i // 100
        ide = i % 10
        ten = (i - ide) // 10 % 10
        if hundred * hundred * hundred + ten * ten * ten + ide * ide * ide == i:
            """if hundred**3+ten**3+ide**3==i"""
            print(i)
