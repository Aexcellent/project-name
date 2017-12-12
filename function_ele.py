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














	
	
	
	
	
	
	
	
