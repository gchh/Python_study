# -*- coding: cp936 -*-
'''
��Ŀ���ݣ�
�����ж�һϵ�и������ַ����Ƿ�Ϊ�Ϸ��� Python ��ʶ����

�����ʽ:
һϵ���ַ�����ÿ���ַ���ռһ�С�

�����ʽ��
�ж�ÿ���ַ����Ƿ�Ϊ�Ϸ��� Python ��ʾ��������Ϸ������ True��������� False��

����������
abc
_def
21gh

���������
True
True
False
ʱ�����ƣ�500ms�ڴ����ƣ�32000kb
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
    if re.match('[a-zA-Z\_][a-zA-Z0-9\_]*', s):
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
