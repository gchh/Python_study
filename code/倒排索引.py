'''
题目内容：

倒排索引（Inverted index），也常被称为反向索引，是一种索引方法，用来存储某个单词存在于哪些文档之中。
是信息检索系统中最常用的数据结构。通过倒排索引，可以根据单词快速获取包含这个单词的文档列表。

本作业主要完成以下四个功能：

(1). 建立索引：首先输入100行字符串，用于构建倒排索引，每行字符串由若干不含标点符号的、全部小写字母组成的单词构成，每个单词之间以空格分隔。
依次读入每个单词，并组成一个由<单词, 每个单词出现的行号集合>构成的字典，其中行号从1开始计数。

(2). 打印索引：按照字母表顺序依次输出每个单词及其出现的位置，每个单词出现的位置则按行号升序输出。
例如，如果“created”出现在第3, 20行，“dead”分别出现在14, 20, 22行。
则输出结果如下（冒号和逗号后面都有一个空格，行号不重复）：

…
created: 3, 20
dead: 14, 20, 22
…

(3). 检索：接下来输入查询(Query)字符串，每行包含一个查询，每个查询由若干关键字(Keywords)组成，每个关键字用空格分隔且全部为小写字母单词。
要求输出包含全部单词行的行号（升序排列），每个查询输出一行。
若某一关键字在全部行中从没出现过或没有一行字符串包含全部关键字，则输出“None”。
遇到空行表示查询输入结束。
如对于上面创建的索引，当查询为“created”时，输出为“3, 20”；当查询为“created dead”时，输出为“20”；当查询为“abcde dead”时，输出为“None”；

(4). 高级检索：当输入的Query以“AND: ”开始，则执行“与”检索，即要求输出包含全部关键字的行；
如果输入的Query以“OR:”开始，则执行“或”检索，即某行只要出现了一个关键字就满足条件。默认情况（不以“AND: ”或“OR: ”开始），执行“与”检索。

输入格式:
首先输入100行字符串，每行字符串由若干不含标点符号的、全部小写字母组成的单词构成，每个单词之间以空格分隔。
若干个查询，每个查询占一行，既可能是普通检索，也可能是高级检索。

输出格式：
首先打印索引，然后将每个查询的结果输出到一行。
时间限制：500ms内存限制：32000kb
'''
w_dic={}
for i in range(1,101):
    line=raw_input()
    for w in line.split():
        if w in w_dic:
            if not (i in w_dic[w]):
                w_dic[w].append(i)
            else:
                w_dic[w]=[i]
sr=[]
while True:
    qs=raw_input()
    if qs=='':
        break
    sr.append(qs)

jh=w_dic.keys()
jh.sort()

for w in jh:
    print w+': '+str(w_dic[w])[1:-1]

for qs in sr:
    os=[]
    if qs[0:3]=='OR:':
        ws=qs[3:].split()
        for w in ws:
            if w in w_dic:
                os=list(set(os)|set(w_dic[w]))
        if len(os)==0:
            print 'None'
        else:
            os.sort()
            print str(os)[1:-1]
    else:
        if qs[0:4]=='AND:':
            qs=qs[4:]
        ws=qs.split()
        if ws[0] in w_dic:
            os=w_dic[ws[0]]
        for w in ws:
            if w in w_dic:
                os=list(set(os)&set(w_dic[w]))
            else:
                os=[]
                break
        if len(os)==0:
            print 'None'
        else:
            os.sort()
            print str(os)[1:-1]
