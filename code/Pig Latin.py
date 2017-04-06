'''
题目内容：
“Pig Latin”是一个英语儿童文字改写游戏，整个游戏遵从下述规则：

(1). 元音字母是‘a’、‘e’、‘i’、‘o’、‘u’。字母‘y’在不是第一个字母的情况下，也被视作元音字母。
    其他字母均为辅音字母。
    例如，单词“yearly”有三个元音字母（分别为‘e’、‘a’和最后一个‘y’）和三个辅音字母（第一个‘y’、‘r’和‘l’）。

(2). 如果英文单词以元音字母开始，则在单词末尾加入“hay”后得到“Pig Latin”对应单词。
    例如，“ask”变为“askhay”，“use”变为“usehay”。

(3). 如果英文单词以‘q’字母开始，并且后面有个字母‘u’，将“qu”移动到单词末尾加入“ay”后得到“Pig Latin”对应单词。
    例如，“quiet”变为“ietquay”，“quay”变为“ayquay”。

(4). 如果英文单词以辅音字母开始，所有连续的辅音字母一起移动到单词末尾加入“ay”后得到“Pig Latin”对应单词。
    例如，“tomato”变为“omatotay”， “school” 变为“oolschay”，“you” 变为“ouyay”，“my” 变为“ymay ”，“ssssh” 变为“sssshay”。

(5). 如果英文单词中有大写字母，必须所有字母均转换为小写。 

输入格式:
一系列单词，单词之间使用空格分隔。

输出格式：
按照以上规则转化每个单词，单词之间使用空格分隔。

输入样例：
Welcome to the Python world Are you ready

输出样例：
elcomeway otay ethay ythonpay orldway arehay ouyay eadyray
时间限制：500ms内存限制：32000kb
'''

s=input()
s=s.lower()
c=s.split(' ')
for i in range(len(c)):
    if c[i][0] in 'aeiou':
        c[i]=c[i]+'hay'
    elif c[i][0]=='q' and c[i][1]=='u':
        c[i]=c[i][2:]+'quay'
    elif c[i][0] not in 'aeiou':
        for j in range(1,len(c[i])):
            if c[i][j] in 'aeiouy':
                #k=j
                break
            elif j+1==len(c[i]):
                j=len(c[i])
        c[i]=c[i][j:]+c[i][:j]+'ay'
for i in range(len(c)):
    if i==0:
        s=c[i]
    else:
        s=s+' '+c[i]
print(s)

'''
def PigLatin():
    s=input();
    list=s.lower().split(" ")
    for i in range(len(list)):
        if ((list[i][:1] in "aeiou")): 
            list[i] = list[i]+"hay"
        elif(list[i][:2]=="qu"):
            list[i]=list[i][2:]+"quay"
        else:
            num =getIndex(list[i])
            list[i] = list[i][num:]+list[i][0:num]+"ay"
    return list
 
def getIndex(s):
    for i in range(len(s)):
        if((s[i] in "aeiou") or (i!=0 and s[i] =="y")):
            return i
    return len(s)
 
result = PigLatin()
for i in range(len(result)):
   print(result[i] ,)
'''
