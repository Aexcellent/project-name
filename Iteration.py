
#字典的迭代
d = {'a':1,'b':2,'c':3}
for key in d:
	print(key)
for values in d.values():
	print(values)
for k,v in d.items():
	print(k,v)

	
#是否可迭代判断
from collections import Iterable
isinstance('abc',Iterable)
isinstance([1,2,3],Iterable)
isinstance(123,Iterable) #不可迭代

#Python内置的enumerate函数可以把一个list变成索引-元素对，这样就可以在for循环中同时迭代索引和元素本身
for i,values in enumerate(['A';'B';'C']):
	print(i,values)

	
for x,y in [(1,1),(2,4),(3,9)]


	