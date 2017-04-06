'''
题目内容：
如在汉诺塔游戏中，我们希望将塔A上的n个盘子，通过塔B移动到塔C，则对于任意输入的n，给出移动的步骤。

输入格式:
一个正整数n

输出格式：
移动的步骤

输入样例：
2

输出样例：
Move 1 from A to B
Move 2 from A to C
Move 1 from B to C

时间限制：500ms内存限制：32000kb
'''
def move(n,a,b,c):
    if n == 1:      # 只有一个盘子时，直接从a移动到c
        print('move',n,'from',a,'to',c)
        return
    move(n-1,a,c,b)     # 大于一个盘子时，开始递归，首先将n-1个盘子从a移到辅助区b
    print('move',n,'from',a,'to',c)# 然后将最后一个大盘子从a移动到c
    move(n-1,b,a,c)     # 最后将原来移动到b的盘子移动到c

if __name__=='__main__':
    n = int(input())
    move(n,'A','B','C')
'''
#Python2.7 print和3.x不同
def hanoi(n, A, B, C):
    if n == 1:
        print 'Move', n, 'from', A, 'to', C
    else:
        hanoi(n - 1, A, C, B)
        print 'Move', n, 'from', A, 'to', C
        hanoi(n - 1, B, A, C)
 
num = int(raw_input())
hanoi(num, 'A', 'B', 'C')
'''
