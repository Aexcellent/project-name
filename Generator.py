#要创建一个generator，有很多种方法。第一种方法很简单，只要把一个列表生成式的[]改成()，就创建了一个generator
L = [x*x for x in range(10)]
print(L)
g = (x*x for x in range(10))
#创建L和g的区别仅在于最外层的[]和()，L是一个list，而g是一个generator。

#我们可以直接打印出list的每一个元素，但我们怎么打印出generator的每一个元素呢？

#如果要一个一个打印出来，可以通过next()函数获得generator的下一个返回值
next(g)
next(g)
#generator保存的是算法，每次调用next(g)，就计算出g的下一个元素的值，直到计算到最后一个元素，没有更多的元素时，抛出StopIteration的错误

#上面这种不断调用next(g)实在是太变态了，正确的方法是使用for循环
for n in g:
 print(n)
 
#斐波那契数列
def fib(max):
	n,a,b=0,0,1
	while n < max:
		print(b)
	a, b = b , a + b
	n = n + 1
	return 'done'
#其中a, b = b, a + b相当于
#t = (b, a + b) # t是一个tuple
#a = t[0]
#b = t[1]


#要把fib函数变成generator，只需要把print(b)改为yield b就可以了
#如果一个函数定义中包含yield关键字，那么这个函数就不再是一个普通函数，而是一个generator
#最难理解的就是generator和函数的执行流程不一样。函数是顺序执行，遇到return语句或者最后一行函数语句就返回。而变成generator的函数，在每次调用next()的时候执行，遇到yield语句返回，再次执行时从上次返回的yield语句处继续执行。

#但是用for循环调用generator时，发现拿不到generator的return语句的返回值。如果想要拿到返回值，必须捕获StopIteration错误，返回值包含在StopIteration的value中
g = fib(6)
while True:
	try:
		x=next(g)
		print('g:',x)
	except StopIteration as e:
		print('Generator return value:', e.value)
		break
		
#凡是可作用于for循环的对象都是Iterable类型；

#凡是可作用于next()函数的对象都是Iterator类型，它们表示一个惰性计算的序列；

#集合数据类型如list、dict、str等是Iterable但不是Iterator，不过可以通过iter()函数获得一个Iterator对象。



