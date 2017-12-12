age = 20
if age >=18:
	print ('your age is',age)
	print ('adult')
elif: age >=6:
	print ('teenager')
else:
	print ('your age is',age)
	print ('kid')
	
	
if x:
	print(x)
#只要x是非零数值、非空字符串、非空list等，就判断为True，否则为False。


s = input('birth:')
birth = int(s)      #这是因为input()返回的数据类型是str，str不能直接和整数比较，必须先把str转换成整数。Python提供了int()函数来完成这件事情
if birth < 2000:
	print('00前')
else:
	print('00后')
