abs(-100)
max(1, 2)
int('123')
int(12.34)
float('12.34')
str(1.23)
str(100)
bool(1)
bool('')



def my_abs(x):
	if not isinstance(x,(int,float)):
		raise TypeError('bad operand type')
	if x >= 0:
		return x
	else:
		return -x

def nop()
	pass

if age >= 18:
	pass
#pass可以用来作为占位符，比如现在还没想好怎么写函数的代码，
#就可以先放一个pass，让代码能运行起来。


import math

def move(x,y,step,angle=0):
	nx = x + step*math.cos(angle)
	ny = y + step*math.sin(angle)

x , y = move(100,100,60,math.pi / 6)
print(x,y)

r = move(100,100,60,math.pi / 6)
print(r)
#原来返回值是一个tuple！
#但是，在语法上，返回一个tuple可以省略括号，
#而多个变量可以同时接收一个tuple，按位置赋给对应的值，
#所以，Python的函数返回多值其实就是返回一个tuple，但写起来更方便


def power(x,n=2)   #必选参数和默认参数
	s=1
	while n>0:
		n=n-1
		s=s*x
	return s
#定义默认参数要牢记一点：默认参数必须指向不变对象！

def add_end(L=None):
	if L is None:
		L  = []
	L.append('End')
	return L



#可变参数就是传入的参数个数是可变的	
def cale(numbers):
	sum=0
	for n in numbers:
		sum= sum+n*n
	return sum

#但是调用的时候，需要先组装出一个list或tuple	
cale([1,2,3])
cale((1,2,3))
#如果利用可变参数，调用函数的方式可以简化成这样
cale(1,2,3)


def cale2(*numbers):
	sum=0
	for n in numbers:
		sum = sum+n*n
	return sum
#定义可变参数和定义一个list或tuple参数相比，仅仅在参数前面加了一个*号。
#在函数内部，参数numbers接收到的是一个tuple，因此，函数代码完全不变。但是，调用该函数时，可以传入任意个参数，包括0个参数
cale2(1,2)
cale2()	
	
nums = [1,2,3]
cale2(*nums)
#*nums表示把nums这个list的所有元素作为可变参数传进去



#关键字参数允许你传入0个或任意个含参数名的参数，这些关键字参数在函数内部自动组装为一个dict
def person(name, age, **kw):
	print('name:', name'age:' age,'other:' kw)

person('Michael',30)
person('Bob', 35, city='Beijing')
person('Adam', 45, gender='M', job='Engineer')

extra = {'city':'Beijing','job':'Engineer'}
person('Jack', 24,**extra)

#**extra表示把extra这个dict的所有key-value用关键字参数传入到函数的**kw参数，kw将获得一个dict.
#注意kw获得的dict是extra的一份拷贝，对kw的改动不会影响到函数外的extra



def person(name, age, **kw):
	if 'city' in kw:
		pass
	if 'job' in kw:
		pass
	print('name:',name,'age:'age,'other:',kw)

#如果要限制关键字参数的名字，就可以用命名关键字参数，例如，只接收city和job作为关键字参数。
def person(name,age,*,city,job):
	print(name,age,city,job)

	
#如果函数定义中已经有了一个可变参数，后面跟着的命名关键字参数就不再需要一个特殊分隔符*了
def person(name,age,*args,city,job):
	print(name,age,args,city,job)
#命名关键字参数必须传入参数名，这和位置参数不同。如果没有传入参数名，调用将报错


#参数定义的顺序必须是：必选参数、默认参数、可变参数、命名关键字参数和关键字参数。



#对于任意函数，都可以通过类似func(*args, **kw)的形式调用它，无论它的参数是如何定义的

///
要注意定义可变参数和关键字参数的语法:
*args是可变参数，args接收的是一个tuple；
**kw是关键字参数，kw接收的是一个dict。
以及调用函数时如何传入可变参数和关键字参数的语法：
可变参数既可以直接传入：func(1, 2, 3)，又可以先组装list或tuple，再通过*args传入：func(*(1, 2, 3))；
关键字参数既可以直接传入：func(a=1, b=2)，又可以先组装dict，再通过**kw传入：func(**{'a': 1, 'b': 2})。
///











	
	
	
	
	
	
	
	
