	height=int(input('你的身高(cm)：'))
	weight=int(input('你的体重(0.1kg)：'))
	height/=100
	weight/=10
	print(height)
	print(weight)
	bmi = weight/(height*height)
	print('BMI=',bmi)
	print('BMI= %.2f'%bmi)
	if bmi<18.5:
	    print('过轻')
	elif bmi<25:
	    print('正常')
	elif bmi<28:
	    print('过重')
	elif bmi<32:
	    print('肥胖')  
使用python2.7运行，结果如下：  

	Python 2.7.13 (v2.7.13:a06454b1afa1, Dec 17 2016, 20:42:59) [MSC v.1500 32 bit (Intel)] on win32
	Type "copyright", "credits" or "license()" for more information.
	>>> 
	==================== RESTART: D:\Users\atdo\Desktop\1.py ====================
	你的身高(cm)：176
	你的体重(0.1kg)：620
	1
	62
	('BMI=', 62)
	BMI= 62.00
	严重肥胖  
使用python3.6运行，结果如下：

	Python 3.6.0 (v3.6.0:41df79263a11, Dec 23 2016, 08:06:12) [MSC v.1900 64 bit (AMD64)] on win32
	Type "copyright", "credits" or "license()" for more information.
	>>> 
	==================== RESTART: D:\Users\atdo\Desktop\1.py ====================
	你的身高(cm)：176
	你的体重(0.1kg)：620
	1.76
	62.0
	BMI= 20.015495867768596
	BMI= 20.02
	正常  
即，在python2中整数(int)/整数，还是一个整数；而在python3中整数/整数，结果自动转换成了浮点数。  
另外，在python2中`print`是语句，所以`print('BMI=',bmi)`，会把`('BMI=',bmi)`作为一个元组(tuple)输出；而在python3中`print`是函数，`print('BMI=',bmi)`，`'BMI'`和`bmi`作为`print`的两个参数输出。  
python2要想和python3输出相同的效果，需要把`print('BMI=',bmi)`改成`print 'BMI=',bmi`。  

