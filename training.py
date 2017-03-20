import math
#对于三角形三边长a, b, c，有c^2=a^2+b^2-2*a*b*cos(C)，编写程序，求得a和b的夹角C(角度值)。
a=float(input())
b=float(input())
c=float(input())
#x=math.degrees(math.acos((math.pow(a,2)+math.pow(b,2)-math.pow(c,2))/(2*a*b)))
#x=math.degrees(math.acos((a**2+b**2-c**2)/(2*a*b)))
x=math.acos((math.pow(a,2)+math.pow(b,2)-math.pow(c,2))/(2*a*b))
x=x*180/math.pi
print('%.1f'%x)
#print('{0:.{1}f}'.format(degree,1))

#假设你每年初往银行账户中1000元钱，银行的年利率为4.7%。求几年后的账户余额
def v(x):
    if x==0:
        return 0
    elif x==1:
        return 1000*(1+0.047)
    else:
        return (1000+v(x-1))*(1+0.047)

#一元二次方程求解a*x**2+b*x+c=0
def fun(a,b,c):
    if(b**2-4*a*c):
        print('%.2f'%((math.sqrt(b**2-4*a*c)-b)/(2*a)))
        print('%.2f'%(-((math.sqrt(b**2-4*a*c)+b)/(2*a))))
        
def fun2(a,b,c):
    delta=b**2-4*a*c
    if delta<0:
        print('无解')
    else:
        x1=(-b+math.sqrt(delta))/(2*a)
        x2=(-b-math.sqrt(delta))/(2*a)
        print('x1=%.2f,x2=%.2f'%(x1,x2))
