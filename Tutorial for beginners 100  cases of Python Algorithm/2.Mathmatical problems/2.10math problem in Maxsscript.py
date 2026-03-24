# 共30个人，其中有女人，男人和小孩，男人吃饭需要3元，女人需要2元，小孩需要1元，一共花费50元，求男人女人小孩各多少人

if __name__ == "__main__":
    for men in range(0, 11):
        for women in range(0, 30 - men):
            kids = 30 - women - men
            if men * 3 + women * 2 + kids * 1 == 50:
                print("%d %d %d" % (men, women, kids))
