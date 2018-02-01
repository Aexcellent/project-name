
def log(func):
	def wrapper(*args, **kw):
		print('call %s():' % func.__name__)
		return func(*args, **kw)
	return wrapper

@log
def now():
	print('2015-3-25')
#调用now()函数，不仅会运行now()函数本身，还会在运行now()函数前打印一行日志:
# >>>now()
#call now():
#2015-3-25
#把@log放到now()函数的定义处，相当于执行了语句
#now = log(now)



