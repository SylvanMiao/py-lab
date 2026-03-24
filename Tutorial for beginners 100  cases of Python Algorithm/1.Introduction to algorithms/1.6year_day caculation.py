# -*- coding:utf-8 -*-
# 判断闰年与否的函数
def judgeyear(year):
    if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
        return 1
    else:
        return 0


# 计算总天数的函数
def countdays(currentday):
    # 这里当前月份不计入总天数，因此数组第一个为0，最后一个为31
    permonth = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30]
    totalday = 0
    original_year = 2002
    while original_year < currentday["year"]:
        if judgeyear(original_year) == 1:
            totalday += 366
        else:
            totalday += 365
        original_year += 1
    if judgeyear(currentday["year"]) == 1:
        permonth[2] += 1
    original_month = 0
    while original_month < currentday["month"]:
        totalday += permonth[original_month]
        original_month += 1

    totalday += currentday["day"]
    totalday -= 124

    return totalday


if __name__ == "__main__":
    # 使得脚本重复运行
    while True:
        print("请输入指定日期：包括年，月，日")
        year, month, day = map(float, input().split())
        today = {"year": year, "month": month, "day": day}
        result = countdays(today)
        print("%d年%d月%d日距离2002年5月4日有%d天" % (year, month, day, result))
