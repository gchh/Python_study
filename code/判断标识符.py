'''
题目内容：
依次判断一系列给定的字符串是否为合法的 Python 标识符。

输入格式:
一系列字符串，每个字符串占一行。

输出格式：
判断每行字符串是否为合法的 Python 标示符，如果合法则输出 True，否则输出 False。

输入样例：
abc
_def
21gh

输出样例：
True
True
False
时间限制：500ms内存限制：32000kb
'''
params=[]
while True:
    s=input()
    if s=='':
        break
    else:
        params.append(s)
for s in params:
    print(s.isidentifier())
'''
import re
 
def isIentifier (s):
    if re.match('[a-zA-Z_][a-zA-Z0-9_]*', s):
        return True
    else:
        return False

params = []
while True:
    s = input()
    if s == '':
        break
    else:
        params.append(s)
for s in params:
    if isIentifier (s):
        print('True')
    else:
        print('False')
'''
