#读文件
try:
	f = open('/User/micheak/text.txt','r')
	print(f.read())
finally:
	if f:
	f.close()
	
#另一种简单写法

with open('/path/to/file', 'r') as f:
	print(f.read())

	
#二进制文件
f = open('/Users/michael/test.jpg','rb')
f.read()


#字符编码
#例如读取GBK编码的文件
f = open('/Users/michael/gbk.txt','r',encoding='gbk')
f.read()


#写文件
f = open('/Users/michael/test.txt','w')
f.write('Hello,world!')
f.close()

#/另一种写法
with open('/Users/michael/test.txt', 'w') as f:
    f.write('Hello, world!')











