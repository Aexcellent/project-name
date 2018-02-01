

import itertools

#自然数序列
naturals = itertools.count(1)
for n in natuals:
	print(n)
	

cs=itertools.cycle('ABC')	
for c in cs:
	print(c)
	
	
ns=itertools.repeat('A',3)	
for n in ns:
	print(n)

	
nn=itertools.takewhile(lambda x: x<=10,natuals)	
list(nn)






	