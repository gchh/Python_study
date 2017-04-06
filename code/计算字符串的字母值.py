'''
题目内容：
依次计算一系列给定字符串的字母值，字母值为字符串中每个字母对应的编号值（A对应1，B对应2，以此类推，不区分大小写字母，非字母字符对应的值为0）的总和。例如，Colin 的字母值为 3 + 15 + 12 + 9 + 14 = 53

输入格式:
一系列字符串，每个字符串占一行。

输出格式：
计算并输出每行字符串的字母值。

输入样例：
Colin
ABC

输出样例：
53
6
时间限制：500ms内存限制：32000kb
'''
s=[]
while True:
    a=input()
    a=a.lower()
    if a=='':
        break
    else:
        s.append(a)
alph='abcdefghijklmnopqrstuvwxyz'
for a in s:
    sum=0
    for b in a:
        sum=sum+alph.find(b)+1
    print(sum)
'''
def getStrValue (letter):
    alph = "abcdefghijklmnopqrstuvwxyz"
    letter = letter.lower()
    return alph.find(letter) + 1
 
params = []
while True:
    s = input()
    if s == '':
        break
    else:
        params.append(s)
 
for word in params:
    sum = 0
    for letter in word:
        sum += getStrValue(letter)
    print(sum)
'''
