'''
题目内容：
若已知1800年1月1日为星期3，则对于一个给定的年份和月份，
输出这个月的最后一天是星期几。

输入格式:
两行整数，分别代表年份和月份

输出格式：
星期数，0代表星期日

输入样例：
2033
12

输出样例：
6
时间限制：500ms内存限制：32000kb
'''
def is_leap_year(Year):
    if Year%4==0 and Year%100!=0 or Year%400==0:
        return True
    else:
        return False

def year_month_days(Year,Month):
    if Month in (1,3,5,7,8,10,12):
        return 31
    elif Month in (4,6,9,11):
        return 30
    elif is_leap_year(Year):
        return 29
    else:
        return 28

def year_days(Year):
    if is_leap_year(Year):
        return 366
    else:
        return 365

def weekday_year_month(Year,Month):
    Weekday=2
    for year in range(1800,Year):
        Weekday=(Weekday+year_days(year))%7
    for month in range(1,Month+1):
        Weekday=(Weekday+year_month_days(Year,month))%7
    print(Weekday)

year=int(input())
month=int(input())

weekday_year_month(year,month)
