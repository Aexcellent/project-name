

#要生成list [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
list(range(1,11))


#要生成[1x1, 2x2, 3x3, ..., 10x10]
L=[]
for x in range(1,11):
	L.append(x*x)
print(L)

#循环太繁琐，而列表生成式则可以用一行语句代替循环生成上面的list
[x*x for x in range(1,11)]

#for循环后面还可以加上if判断，这样我们就可以筛选出仅偶数的平方
[x*x for x in range(1,11) if x%2==0]

#还可以使用两层循环，可以生成全排列
[m + n for m in 'ABC' for n in 'XYZ']

#列出当前目录下的所有文件和目录名，可以通过一行代码实现
import os
[d for d in os.listdir('.')]

#列表生成式也可以使用两个变量来生成list
d = {'x':'A','y':'B','z':'C'}
[k+'='+v for k, v in d.items()]

#把一个list中所有的字符串变成小写
L=['Hello','World','IBM','Apple']
[s.lower() for s in L]


