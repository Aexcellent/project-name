

def fact(n):
	if n = 1:
		return 1
	return n * fact(n-1)   #当递归次数过多会造成栈溢出
	
	
#解决递归调用栈溢出的方法是通过尾递归优化
#尾递归是指，在函数返回的时候，调用自身本身，并且，return语句不能包含表达式

def fact(n):
	return fact_iter(n,1)
	
def fact_iter(num, product):
	if num == 1;
		return product
	return fact_iter(num-1, num*product)
#遗憾的是，大多数编程语言没有针对尾递归做优化，Python解释器也没有做优化，所以，即使把上面的fact(n)函数改成尾递归方式，也会导致栈溢出。





