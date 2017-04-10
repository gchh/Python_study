##第一周：程序设计的基础知识
###第一周测验
1单选(1分)计算机为什么采用二进制，而非十进制作为数制的基础？  

	A.因为二进制比十进制表示能力更强  
	B.因为二进制比十进制计算速度快  
	C.因为二进制数更容易被硬件存储和计算  
	D.因为二进制数精度更高  
2单选(1分)Python语言为什么被称为高级程序设计语言？  

	A.因为它比低级语言功能强大
	B.因为它比低级语言更贴近人类的思维
	C.因为它是编译型语言
	D.因为它是解释型语言
3单选(1分)下列Python程序，没有错误的是？  

	A.Print 'Hello, World!'
	B.print 'Hello, this's Tom.'
	C.print 'Hello, ' print 'World!'
	D.print 'Hello, I\'m Tom.'
4单选(1分)关于Python语言的执行过程，描述正确的是？  

	A.可以同时执行多条语句
	B.执行过的语句将不会再被执行
	C.由编译器将源程序转化为机器语言，然后执行
	D.由解释器一条语句一条语句地执行
5单选(1分)在Spyder IDE中编写Python程序，输出“Hello World”，要求将这两个单词分两行输出，以下哪个程序不正确？

	A.print 'Hello\nWorld'
	B.print 'Hello
	  World'
	C.print 'Hello' 
	  print 'World'
	D.print "Hello\nWorld"

##第二周：数据类型、运算符与表达式、变量赋值与简单I/O操作
###第二周测验
1.单选(1分)执行下列语句，输出的结果是？  

	x = 7.0
	y = 5
	print x % y

	A.1 
	B.2.0 
	C.1.0 
	D.2 
正确答案：C  
2.单选(1分)能实现下面功能的程序是？  
接收用户输入的一个整数。如果输入的是偶数，则输出“True”，否则输出“False”。  

	A.print int(raw_input()) % 2 != 0 
	B.print not bool(int(raw_input()) % 2) 
	C.print not bool(raw_input() % 2) 
	D.print int(raw_input()) % 2 == 1
正确答案：B  
3.填空(1分)假设你每年初往银行账户中1000元钱，银行的年利率为4.7%。   
一年后，你的账户余额为：   
1000 * ( 1 + 0.047) = 1047 元   
第二年初你又存入1000元，则两年后账户余额为： 
(1047 + 1000) * ( 1 + 0.047) = 2143.209 元  
以此类推，第10年年末，你的账户上有多少余额？   
注：结果保留2位小数（四舍五入）。   
结果为 ：12986.11 ,实现代码：  

	total = 0
	for x in xrange(0,10):
	    total = (total+1000)*(1+0.047)
	print total
4.填空(1分)Python提供了众多的模块。你能找到一个合适的模块，输出今天的日期吗？格式为“yyyy-mm-dd”。可以查找任何搜索引擎和参考资料，并在下面的空白处写出相应的模块名。   
参考答案： datetime  
5.填空(1分)对于一元二次方程ax<sup>2</sup>+bx+c=0，若有a=10,b=40,c=15，则其解是什么？若有多个解，则按照从小到大的顺序在一行中输出，中间使用空格分隔。解保留2位小数（四舍五入）。   
答案: -3.58 -0.42  

###第二周 OnlineJudge
1.编写程序，完成下列题目（1分）  
题目内容：   
身体质量指数（Body Mass Index，BMI）是根据人的体重和身高计算得出的一个数字，BMI对大多数人来说，是相当可靠的身体肥胖指标，其计算公式为：，其中体重单位为公斤，身高单位为米。编写程序，提示用户输入体重和身高的数字，输出BMI。   
输入格式:   
输入两行数字，第一行为体重（公斤），第二行为身高（米）   
输出格式：   
相应的BMI值，保留两位小数。注：可以使用 format 函数设置保留的小数位数，使用 help(format) 查看 format 函数的使用方法。   
输入样例：   
80   
1.75   
输出样例：   
26.12   
时间限制：500ms内存限制：32000kb   
代码：  

	#!/usr/bin/env python
	#coding: utf-8
	#身体质量指数计算
	weight = float(raw_input())
	high = float(raw_input())
	result = weight/(high ** 2)
	print '{:.2f}'.format(result)
2.编写程序，完成下列题目（2分）  
题目内容：   
接收用户输入的一个秒数（非负整数），折合成小时、分钟和秒输出。   
输入格式:   
一个非负整数   
输出格式：   
将小时、分钟、秒输出到一行，中间使用空格分隔。   
输入样例：   
70000   
输出样例：   
19 26 40   
时间限制：500ms内存限制：32000kb   
代码：  

	#!/usr/bin/env python
	#coding: utf-8
	
	sec = int(raw_input())
	print str(sec/3600)+' '+str(sec%3600/60)+' '+str(sec%60)
3.编写程序，完成下列题目（2分）  
题目内容：   
对于三角形，三边长分别为a, b, c，给定a和b之间的夹角C，则有：。编写程序，使得输入三角形的边a, b, c，可求得夹角C(角度值)。   
输入格式:   
三条边a、b、c的长度值，每个值占一行。   
输出格式：   
夹角C的值，保留1位小数。   
输入样例：   
3   
4   
5   
输出样例：   
90.0   
时间限制：500ms内存限制：32000kb   
代码：  

	#!/usr/bin/env python
	#coding:utf-8
	
	import math
	
	a = float(raw_input())
	b = float(raw_input())
	c = float(raw_input())
	degree = math.degrees(math.acos((a**2 + b**2 - c**2) / (2 * a * b)))
	print '{0:.{1}f}'.format(degree, 1)
##第三周 程序控制结构  
###第三周：测验与作业
1.以下程序的输出结果是？  

	number = 30
	if number % 2 == 0:
	    print number, 'is even'
	elif number % 3 == 0:
	    print number, 'is multiple of 3'

	A.程序出错 
	B.30 is even 
	30 is multiple of 3 
	C.30 is multiple of 3 
	D.30 is even
答案(D)  
2.以下程序的输出结果是？  

	x = 1
	y = -1
	z = 1
	if x > 0: 
	    if y > 0: print 'AAA' 
	elif z > 0: print 'BBB'

	A.无输出 
	B.BBB 
	C.语法错误 
	D.AAA
答案(A)  
3.以下程序的输出结果是？  

	y = 0 
	for i in range(0, 10, 2): 
	    y += i 
	print y

	A.20 
	B.30 
	C.10 
	D.9
答案(A)  
4.如果输入4, -1, 6, 9, 8, 3, 0，请问以下程序的输出结果是？  

	number = int(raw_input('Enter an integer: '))
	max = number
	while number != 0:
	    number = int(raw_input('Enter an integer: '))
	    if number > max:
	        max = number
	print max
答案（9）  
5.Python语言中，  

	if x > 0:
	    y = 1
	else:
	    y = -1
等价于：

	y = 1 if x > 0 else -1
阅读下面代码，给出x结果：

	a = 3
	b = 2
	x = a if a > b else b
答案（3）  
###第三周：Online Judge
1.编写程序，完成下列题目  
题目内容：   
如果列出10以内自然数中3或5的倍数，则包括3,5,6,9。那么这些数字的和为23。要求计算得出任意正整数n以内中3或5的倍数的自然数之和。   
输入格式:   
一个正整数n。   
输出格式：   
n以内中3或5的倍数的自然数之和。   
输入样例：   
10   
输出样例：   
23   
代码：  

	sum = 0
	n = int(raw_input())
	for i in range(n):
	    if i % 3 == 0:
	        sum += i
	    elif i % 5 == 0:
	        sum += i
	print sum
2.编写程序，完成下列题目  
题目内容：   
10以内的素数2,3,5,7的和为17。要求计算得出任意正整数n以内的所有素数的和。   
输入格式:   
一个正整数n。   
输出格式：   
n以内的所有素数的和。   
输入样例：   
10   
输出样例：   
17   
时间限制：500ms内存限制：32000kb   
代码：  


3.编写程序，完成下列题目  
题目内容：   
根据下列信息计算在1901年1月1日至2000年12月31日间共有多少个星期天落在每月的第一天上？   
a) 1900.1.1是星期一   
b) 1月，3月，5月，7月，8月，10月和12月是31天   
c) 4月，6月，9月和11月是30天   
d) 2月是28天，在闰年是29天   
e) 公元年数能被4整除且又不能被100整除是闰年   
f) 能直接被400整除也是闰年   
输出格式：   
一个正整数   
时间限制：500ms内存限制：32000kb   
代码：  


4.编写程序，完成下列题目  
题目内容：   
数字197可以被称为循环素数，因为197的三个数位循环移位后的数字：197,971,719均为素数。100以内这样的数字包括13个，2,3,5,7,11,13,17,31,37,71,73,79,97。要求任意正整数n以内一共有多少个这样的循环素数。   
输入格式:   
一个正整数n。   
输出格式：   
n以内循环素数的数目。   
输入样例：   
100   
输出样例：   
13   
时间限制：2000ms内存限制：32000kb   
代码：  


##第四周: 函数与递归函数
###第四周测验
1.下列程序的输出结果是：  

	def foo():
	    m = 1
	    def bar():
	         n = 2
	         return m + n
	    m = bar()
	    print m
	foo()
正确答案：3  
2.针对以下的函数，正确的函数调用有哪些？  

	def foo(arg1, arg2='test', arg3=100):
	    print arg1, arg2, arg3

	A.foo(arg1 = 'where', arg2 = 'what')
	B.foo(arg2 = 'what', 10)
	C.foo('where')
	D.foo('where','what')  
正确答案：A,C,D  
3.下列说法是否正确：“函数中仅允许使用一条return语句”  
答案： 错  
4.下列程序的输出结果是？

	def gcd(m, n):
	    r = m % n
	    if r == 0:
	        return n
	    else:
	        r = m % n
	    return gcd(n, r)
	print gcd(15, 36)  
正确答案：3  
5.下面程序的输出结果是：

	def fib(n):
	    f1, f2 = 0, 1
	    while f2 < n:
	        print f2,
	        f1, f2 = f2, f1 + f2
	fib(10)  
正确答案：1 1 2 3 5 8  
###第4周 Online judge
1.一个斐波那契数列的前10项为：1, 2, 3, 5, 8, 13, 21, 34, 55, 89，对于一个最大项的值不超过n的斐波那契数列，求值为偶数的项的和。  
输入格式:   
一个正整数n，如100。   
输出格式：   
值为偶数的项的和，如 2 + 8 + 34 = 44。   
输入样例：   
100   
输出样例：   
44  
迭代法：  

	#!/usr/bin/env python
	#coding: utf-8
	
	def fib(n):
	    if n == 0 or n == 1:
	        return 1
	    else:
	        return fib(n - 1) + fib(n - 2)
	
	sum = 0
	i = 0
	num = int(raw_input())
	while fib(i) < num:
	    if fib(i) % 2 == 0:
	        sum += fib(i)
	    i += 1
	print sum  
循环法：

	#!/usr/bin/env python
	#coding: utf-8
	
	
	def fib_qiujie(n):
	    result = 0
	    sum = 0
	    i = 0
	    tmp1 = 0
	    tmp2 = 0
	    while result < n:
	        if i ==0 or i == 1:
	            tmp1 = 1
	            tmp2 = 1
	            result = 1
	        elif i > 1:
	            if result % 2 == 0:
	                sum += result
	            result = tmp2 +tmp1
	            tmp1 = tmp2
	            tmp2 = result
	        i += 1
	
	    print sum
	
	num = int(raw_input())
	fib_qiujie(num)  
2.若已知1800年1月1日为星期3，则对于一个给定的年份和月份，输出这个月的最后一天是星期几。  
输入格式:   
两行整数，分别代表年份和月份   
输出格式：   
星期数，0代表星期日   
输入样例：   
2033   
12   
输出样例：   
6  

	#!/usr/bin/env python
	#coding: utf-8
	
	def is_leap_year(Year):
	     if Year % 4 == 0 and Year % 100 != 0 or Year % 400 == 0:
	         return True
	     else:
	         return False
	
	def  year_month_days(Year, Month):
	    if Month in (1, 3, 5, 7,  8, 10, 12):
	        return 31
	    elif Month in (4, 6, 9, 11):
	        return 30
	    elif is_leap_year(Year):
	        return 29
	    else:
	        return 28
	
	def  year_days(Year):
	    if is_leap_year(Year):
	        return 366
	    else:
	        return 365
	
	def  weekday_year_month(Year, Month):
	    Weekday = 2              
	    for year in range(1800, Year):
	        Weekday = (Weekday + year_days(year) ) % 7
	
	    for month in range(1, Month + 1):
	        Weekday = (Weekday + year_month_days(Year, month)) % 7
	
	    print Weekday
	
	Y = int(raw_input())
	M = int(raw_input())   
	
	weekday_year_month(Y, M)  
3.如在汉诺塔游戏中，我们希望将塔A上的n个盘子，通过塔B移动到塔C，则对于任意输入的n，给出移动的步骤。  
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

	#!/usr/bin/env python
	#coding: utf-8
	
	def hanoi(n, A, B, C):
	    if n == 1:
	        print 'Move', n, 'from', A, 'to', C
	    else:
	        hanoi(n - 1, A, C, B)
	        print 'Move', n, 'from', A, 'to', C
	        hanoi(n - 1, B, A, C)
	
	num = int(raw_input())
	hanoi(num, 'A', 'B', 'C')  
##第五周：字符串
###第五周测验
1.字符串s长度为奇数，则显示中间字符的表达式为？  

	A.s[(len(s) - 1)/2]
	B.s[len(s)/2 - 1]
	C.s[(len(s) + 1)/2]
	D.s[len(s)/2 + 1]
答案 A    
2.下载并遍历 names.txt 文件，输出长度最长的回文人名。  
相关代码：

	def is_pamax(name):
	    low = 0
	    up = len(name)-1
	    while low < up:
	        if name[low] != name[up]:
	            return  False
	        low += 1
	        up -= 1
	    return True
	
	
	f = open("D:/names.txt")
	
	max_length = 0
	for line in f:
	    name = line.strip()
	    if is_pamax(name):
	        temp_length = len(name)
	        if temp_length > max_length:
	            max_length=temp_length
	
	print max_length
	
	f.close()
	
	# maxlength=8
	f = open("D:/names.txt")
	for line in f:
	    name = line.strip()
	    if is_pamax(name):
	        if 8 == len(name):
	            print name
	f.close()  
正确答案：TREFFERT  
3当输入为 'hello'时，写出下列程序的输出结果：

	s = raw_input()
	y = 0
	  
	for i in s:
	    y += 1
	    print y, i,
正确答案：1 h 2 e 3 l 4 l 5 o  
4.当输入为 ‘cbabc’ 时，下列程序的输出结果为？  

	s1 = raw_input()
	index = 0
	s2 = ''
	
	while index < len(s1) - 1:
	    if s1[index] > s1[index + 1]:
	        s2 += s1[index]
	    else:
	        s2 = s2 * 2
	
	    index += 1
	
	print s2  
正确答案：cbcbcbcb  
5.若 s = ‘What is your name’， 则 s[11:2:-2] 的结果为？  
答案： ro it  
###第五周作业 Online Judge
1、编写程序，完成下列题目：  
题目内容：   
“Pig Latin”是一个英语儿童文字改写游戏，整个游戏遵从下述规则：   
(1). 元音字母是‘a’、‘e’、‘i’、‘o’、‘u’。字母‘y’在不是第一个字母的情况下，也被视作元音字母。其他字母均为辅音字母。例如，单词“yearly”有三个元音字母（分别为‘e’、‘a’和最后一个‘y’）和三个辅音字母（第一个‘y’、‘r’和‘l’）。  
(2). 如果英文单词以元音字母开始，则在单词末尾加入“hay”后得到“Pig Latin”对应单词。例如，“ask”变为“askhay”，“use”变为“usehay”。  
(3). 如果英文单词以‘q’字母开始，并且后面有个字母‘u’，将“qu”移动到单词末尾加入“ay”后得到“Pig Latin”对应单词。例如，“quiet”变为“ietquay”，“quay”变为“ayquay”。  
(4). 如果英文单词以辅音字母开始，所有连续的辅音字母一起移动到单词末尾加入“ay”后得到“Pig Latin”对应单词。例如，“tomato”变为“omatotay”， “school” 变为“oolschay”，“you” 变为“ouyay”，“my” 变为“ymay ”，“ssssh” 变为“sssshay”。  
(5). 如果英文单词中有大写字母，必须所有字母均转换为小写。   
输入格式:   
一系列单词，单词之间使用空格分隔。  
输出格式：    
按照以上规则转化每个单词，单词之间使用空格分隔。  
输入样例：   
Welcome to the Python world Are you ready  
输出样例：   
elcomeway otay ethay ythonpay orldway arehay ouyay eadyray  
代码：  

	#!/usr/bin/env python  
	# coding: utf-8

	import string  
	s = raw_input()  
	words = s.split()  
	newWords = ''  
	for word in words:  
	    tmp = word.lower()  
	    if tmp[0] in 'aeiou':  
	        tmp += 'hay'  
	    elif tmp[0] == 'q' and tmp[1] == 'u':  
	        tmp = tmp[2:] + 'quay'  
	    else:  
	        tmp = tmp[1:] + tmp[0]  
	        for i in range(0, len(tmp)):  
	            if tmp[i] in 'aeiouy':  
	                break;  
	        tmp = tmp[i:] + tmp[:i] + 'ay'  
	    newWords += tmp + ' '  
	print newWords.strip()  
2、编写程序，完成下列题目：  
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
代码：  

	#!/usr/bin/env python  
	# coding: utf-8
	
	import re  
	tmp = raw_input()  
	while (tmp != ''):  
	    if not re.search(u'^[_a-zA-Z0-9]+$',tmp):  
	        print False  
	    elif not re.search(u'^[_a-zA-Z]+$',tmp[0]):  
	        print False  
	    else:  
	        print True  
	    tmp = raw_input()  
3、编写程序，完成下列题目：  
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
代码：  

	#!/usr/bin/env python  
	# coding: utf-8
	
	tmp = raw_input()  
	while(tmp != ''):  
	    num = 0  
	    tmp = tmp.lower()  
	    for c in tmp:  
	        i = ord(c) - 96  
	        if i < 1 or i > 26:  
	            i = 0  
	        num += i  
	    print num  
	    tmp = raw_input()  
##第六周：列表与元组
###第六周测验
1、关于元组数据结构，下面描述正确的是

	A.所有元素数据类型必须相同 
	B.插入的新元素放在最后 
	C.元组不支持切片操作 
	D.支持 in 运算符 
正确答案：D  
2、下列代码的输出结果是？  

	list1 = [1, 2, 3]
	list2 = list1
	list3 = list2
	list1.remove(1)
	print list3[1]  
正确答案：3  
3、写出下面程序的输出结果：([9, 6, 5, 2, 1])

	def func(lst):
	    for i in range(len(lst) - 1):
	        for j in range(i + 1, len(lst)):
	            if lst[i] < lst[j] :
	                lst.insert(i, lst.pop(j))
	            else:
	                pass
	    else:
	        return lst
	    return -1
	
	lst1 = [6, 2, 4, 1, 5, 9]
	lst2 = func(lst1)
	lst2[3:-2] = []
	print lst1  
4、使用 Python 的算术运算符`+`、`-`、`*`、`/`、`**`（没有%），和数字 2、3、4、5，构造一个表达式，使用所有的4个数字和3个运算符各一次，计算得到 28，在下面的空格中填入不含空格的表达式。提示：构建字符串，然后使用 Python 的 eval() 函数，它的参数为字符串，计算该字符串，并返回计算结果，例如： `eval(‘2*3+4’)` 返回整数 10。  
正确答案：`2**3+4*5` 或 `2**3+5*4` 或 `4*5+2**3` 或 `5*4+2**3`  
5、有 3 个回文数字，第一个是两位数，第二个是三位数。将这两个数字相加得到第三个数字，这是个四位数。请问第三个数字是多少？  
正确答案： 1001  
###第六周作业(Online Judge)
1、编写程序，完成下列题目：  
题目内容：   
定义一个 prime() 函数求整数 n 以内（不包括n）的所有素数（1不是素数），并返回一个按照升序排列的素数列表。使用递归来实现一个二分查找算法函数bi_search()，该函数实现检索任意一个整数在 prime() 函数生成的素数列表中位置（索引）的功能，并返回该位置的索引值，若该数不存在则返回 -1。  
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
代码：  

	#!/usr/bin/env python
	# -*- coding: utf-8 -*-
	
	# import re
	# import itertools
	import math
	# import datetime
	# import sys
	
	# from PyQt4.QtCore import *
	# from PyQt4.QtGui import *
	
	# import numpy as np
	# import matplotlib.pyplot as plt
	# import copy
	
	def primeindex(n):
	    l = []
	
	    def is_prime(n):
	        for i in xrange(2, int(math.sqrt(n)) + 1):
	            if n % i == 0:
	                return False
	        return True
	    for i in xrange(2, n):
	        if is_prime(i):
	            l.append(i)
	    return l
	
	
	def bi_search(lst, low, high, x):
	    while low <= high:
	        mid = (low + high) / 2
	        if lst[mid] == x:
	            return mid
	        elif lst[mid] > x:
	            return bi_search(lst, low, mid - 1, x)
	        else:
	            return bi_search(lst, low + 1, high, x)
	    return -1
	if __name__ == '__main__':
	    n = int(raw_input())
	    lp = primeindex(n)
	    high = len(lp) - 1
	    l = []
	    while True:
	        num = raw_input()
	        if num == '':
	            break
	        else:
	            l.append(int(num))
	    for i in l:
	        print bi_search(lp, 0, high, i)  
2、编写程序，完成下列题目：  
题目内容：   
帕斯卡三角形，又称杨辉三角形是二项式系数在三角形中的一种几何排列。帕斯卡三角形通常从第0行开始枚举，并且每一行的数字是上一行相邻两个数字的和。在第0行只写一个数字1，然后构造下一行的元素。将上一行中数字左侧上方和右侧上方的数值相加。如果左侧上方或者右侧上方的数字不存在，用0替代。下面给出6行的帕斯卡三角形：  

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
代码：

	#!/usr/bin/env python  
	# coding: utf-8
	
	import datetime as dt
	
	def pascalLine(num):
	    l = [1]
	    if num == 0:
	        return l
	    else:
	        for i in xrange(num):
	            l = [0] + l[:] + [0]
	            l = [l[i] + l[i + 1] for i in range(len(l) - 1)]
	        return l
	if __name__ == '__main__':
	    n = int(raw_input())
	    for i in xrange(0, n):
	        l = pascalLine(i)
	        s = ''
	        for j in l:
	            s = s + str(j) + ' '
	        print ' ' * (n - i - 1) + s[:-1]　　
##第七周：字典与集合
###第七周测验
1(1分) 一个学生的信息包括：学号、姓名、年龄、性别、电话。如果想保存一系列学生，并且希望能够快速的查找某一姓名的学生，则下列数据结构哪个更合适？  

	A.集合 
	B.元组 
	C.列表 
	D.字典
答案：D  
2(1分) 一个学生的信息包括：学号、姓名、年龄、性别、电话。如果想保存一系列学生，并且希望能够根据姓名对他们进行排序，则下列数据结构哪个更合适？  

	A.集合 
	B.字典 
	C.列表 
	D.元组  
答案：C   
3(1分) 写出下面程序的输出结果：

	d1 = {}
	d1[2] = 10
	d1['2'] = 20
	
	d2 = {}
	d2[2] = d1
	d2['2'] = d2
	
	print d2['2']['2']['2']['2'][2][2]  
答案： 10  
4(1分) 下列程序的执行结果是：

	def f2 (my_dict): 
	    temp = ''
	    for key in my_dict:
	        if temp < key:
	            temp = key
	    return temp
	
	a_dict = {'bill':1,'rich':2,'fred':10,'walter':20}
	print f2(a_dict)  
答案： walter  
5(1分) 下列程序的输出结果是：

	def f1 (my_dict):
	    temp = 0
	    for value in my_dict.values():
	        temp = temp + value
	    return temp
	
	a_dict={'bill':1,'rich':2,'fred':10,'walter':20}
	print f1(a_dict)  
答案： 33  
