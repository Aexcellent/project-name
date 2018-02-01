
class Student(object):
	__slot__=('name','age') #用tuple定义允许绑定的属性名称
	def __init__(self,name):
		self.name=name
		
	def __str__(self):
		return 'Student object (name: %s)' %self.name
	__repr__=__str__
	

class Fib(object):
	def __init__(self):
		self.a,self.b=0,1
	
	def __getattr__(self,attr):
		if attr=='score':
			return 99
		raise AttributeError('\'Student\' object has no attribute \'%s\'' %attr)
	
	def __iter__(self):
		return self #实例本身就是迭代对象，故返回自己
		
		
	def __next__(self):
		self.a,self.b=self.b,self.a+self.b
		if self.a>100000
			raise StopIteration
		return self.a
		
	def __getitem__(self,n):
		if isinstance(n,int):
		a,b=1,1
		for x in range(n):
			a,b=b,a+b
		return a;
		if isinstance(n,slice):
			start = n.start
			stop = n.stop
			if start is None:
				start = 0
			a,b=1,1
			L=[]
			for x in range(stop):
				L.append(a)
			a,b=b,a+b
			return L

			
class Chain(object):
	
	def __init__(self, path=''):
		self._path = path
		
	def __getattr__(self,path):
		return Chain('%s/%s' %(self.path,path))
	
	def __str__(self):
		return self._path
	
	__repr__ = __str__
	

class Student(object):
	def __init__(self,name):
		self.name = name
		
	def __call__(self):
		print('My name is %s.' % self.name)
	
	
		
		
		
		