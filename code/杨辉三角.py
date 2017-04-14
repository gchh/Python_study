'''
题目内容：
帕斯卡三角形，又称杨辉三角形是二项式系数在三角形中的一种几何排列。
帕斯卡三角形通常从第0行开始枚举，并且每一行的数字是上一行相邻两个数字的和。
在第0行只写一个数字1，然后构造下一行的元素。
将上一行中数字左侧上方和右侧上方的数值相加。
如果左侧上方或者右侧上方的数字不存在，用0替代。下面给出6行的帕斯卡三角形：
     1
    1 1
   1 2 1
  1 3 3 1
 1 4 6 4 1
1 5 10 10 5 1
编写程序，输入帕斯卡三角形的高度 n，然后生成和上面例子一样风格的三角形。

输入格式:
一个正整数 n

输出格式：
相应高度的帕斯卡三角形，两个数字之间有一个空格

输入样例：
6

输出样例：
     1
    1 1
   1 2 1
  1 3 3 1
 1 4 6 4 1
1 5 10 10 5 1

时间限制：500ms内存限制：32000kb
'''
'''
def pascalLine(num):
    l = [1]
    if num == 0:
        return l
    else:
        for i in range(num):
            l = [0] + l[:] + [0]
            l = [l[i] + l[i + 1] for i in range(len(l) - 1)]
        return l
   
if __name__ == '__main__':
    n = int(input())
    for i in range(0, n):
        l = pascalLine(i)
        s = ''
        for j in l:
            s = s + str(j) + ' '
        print(' ' * (n - i - 1) + s[:-1])
'''
def pascalLine(num):
    l=[]
    if num==0:
        l=[1]
    elif num==1:
        l+=[1,1]
    else:
        for i in range(len(l[num-1])-1):
            l1+=[l[i]+l[i+1]]
        l=[1]+l1+[1]
    l2=l
    return l
if __name__ == '__main__':
    n = int(input())
    for i in range(0, n):
        l = pascalLine(i)
        s = ''
        for j in l:
            s = s + str(j) + ' '
        print(' ' * (n - i - 1) + s[:-1])
