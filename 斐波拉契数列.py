'''
题目内容：
一个斐波那契数列的前10项为：1, 2, 3, 5, 8, 13, 21, 34, 55, 89，
对于一个最大项的值不超过n的斐波那契数列，求值为偶数的项的和。

输入格式:
一个正整数n，如100。

输出格式：
值为偶数的项的和，如 2 + 8 + 34 = 44。

输入样例：
100

输出样例：
44
时间限制：500ms内存限制：32000kb
'''
def fib(max):
    a, b = 0, 1
    while b < max:
        yield b
        a, b = b, a + b
    return

n=int(input())
sum=0
for x in fib(n):
    #print(x)
    if x%2==0:
        sum=sum+x
print(sum)
