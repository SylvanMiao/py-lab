if __name__ == "__main__":
    # 个税起征点
    taxbase = 2000
    taxtable = [
        (0, 500, 0.05),
        (500, 2000, 0.10),
        (2000, 5000, 0.15),
        (5000, 20000, 0.20),
        (20000, 40000, 0.25),
        (40000, 60000, 0.30),
    ]

    def calculatetax(profit):
        tax = 0.0
        profit -= 2000
        i = 0
        for i in range(len(taxtable)):
            if profit > taxtable[i][0]:
                if profit > taxtable[i][1]:
                    tax += (taxtable[i][1] - taxtable[i][0]) * taxtable[i][2]
                else:
                    tax += (profit - taxtable[i][0]) * taxtable[i][2]
            profit -= taxtable[i][1]
            if profit < 0:

                break
            print(
                "征税范围：%6d~%6d 累计缴纳金额：%6.2f 超出该范围的金额：%6d"
                % (taxtable[i][0], taxtable[i][1], tax, profit)
            )

        return tax

    profit = int(input("enter revenue:"))
    tax = calculatetax(profit)
    print(tax)
