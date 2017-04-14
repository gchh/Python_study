'''
题目内容：
定义一个 prime() 函数求整数 n 以内（不包括n）的所有素数（1不是素数），并返回一个按照升序排列的素数列表。
使用递归来实现一个二分查找算法函数bi_search()，
该函数实现检索任意一个整数在 prime() 函数生成的素数列表中位置（索引）的功能，
并返回该位置的索引值，若该数不存在则返回 -1。

输入格式:
第一行为正整数 n
接下来若干行为待查找的数字，每行输入一个数字

输出格式：
每行输出相应的待查找数字的索引值

输入样例：
10
2
4
6
7

输出样例：
0
-1
-1
3
时间限制：500ms内存限制：32000kb
'''
import math

def isPrime(n):#判断一个数是否是素数
    is_prime=1
    for i in range(2,int(math.sqrt(n))+1):
        if n%i==0:
            is_prime=0
            break
    return is_prime

def prime(n):#生成n以内的素数列表
    primes_list=[]
    for i in range(2,n):
        if isPrime(i):
            primes_list.append(i)
    return primes_list
'''
def bi_search(n,primesList):#用二分查找一个整数在prime()生成的素数列表的位置
    result=-1
    high=len(primesList)
    low=0
    guess=low+int((high-low)/2)
    count=0
    while count<len(primesList):
        if primesList[guess]==n:
            result=guess
            break
        elif primesList[guess]<n:
            low=guess
        else:
            high=guess
        guess=low+int((high-low)/2)
        count+=1
    return result
'''
def bi_search(n,primesList):#用二分查找一个整数在prime()生成的素数列表的位置
    result=-1
    high=len(primesList)-1
    low=0
    guess=low+int((high-low)/2)
    while low<=high:
        if primesList[guess]==n:
            result=guess
            break
        elif primesList[guess]<n:
            low=guess+1
        else:
            high=guess-1
        guess=low+int((high-low)/2)
    return result
#用递归实现二分查找一个整数在prime()生成的素数列表的位置
def bi_search_recursion(low,high,n,primesList):
    while low<=high:
        guess=low+int((high-low)/2)
        if primesList[guess]==n:
            return guess
        elif primesList[guess]<n:
            return bi_search_recursion(guess+1,high,n,primesList)
        else:
            return bi_search_recursion(low,guess-1,n,primesList)
    return -1

if __name__ == '__main__':
    n=int(input())
    ListPrimes=prime(n)
    #print(ListPrimes)
    searchList=[]
    while True:
        #x=int(input())
        #print(bi_search(x,ListPrimes))
        x=input()
        if x=='':
            break
        else:
            searchList.append(int(x))
    #for i in searchList:
        #print(bi_search(i,ListPrimes))
    high=len(ListPrimes)-1
    low=0    
    for i in searchList:
        print(bi_search_recursion(low,high,i,ListPrimes))
