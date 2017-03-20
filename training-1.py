#10以内的素数2,3,5,7的和为17。要求计算得出任意正整数n以内的所有素数的和。
import math
n=int(input())
sum=0
for x in range(2,n):
    a=0
    for i in range(2,int(math.sqrt(x))+1):
        if x%i==0:
            a=1
            break
    if a==0:
        sum+=x
print(sum)

'''
根据下列信息计算在1901年1月1日至2000年12月31日间共有多少个星期天落在每月的第一天上？

a)  1900.1.1是星期一
b)  1月，3月，5月，7月，8月，10月和12月是31天
c)  4月，6月，9月和11月是30天
d)  2月是28天，在闰年是29天
e)  公元年数能被4整除且又不能被100整除是闰年
f)  能直接被400整除也是闰年
'''
import calendar
a=0
for year in range(1901,2001):
    for month in range(1,13):
        if calendar.monthcalendar(year,month)[0].index(1)==6:
        #calendar.monthcalendar(year,month)[0]这个月的第一周，
        #.index()这个月的第几天
        #==0~6（星期一到星期日）
            a=a+1
            print('%s-%s-%s is sunday'%(year,month,1))
print(a)

#求任意正整数n以内一共有多少个这样的循环素数
import math
n=int(input())
num=0
def sushu(x):
    a=0
    for i in range(2,int(math.sqrt(x))+1):
        if x%i==0:
            a=1
            break
    return a
for x in range(2,n):
    b=x
    l=len(str(x))
    for y in range(l):
        a=sushu(b)
        if a==0:
            c=b%10
            c=c*math.pow(10,l-1)
            b=c+int(b/10)#必须把b/10的结果转换成整数，不然b/10得到的是浮点数
        else:
            break
    if a==0:
        print(x)
        num=num+1
print(num)
