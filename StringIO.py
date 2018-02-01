

from io import StringIO

#把str写入StingIO
f = StringIO()
f.write('hello')
f.write(' ')
f.write('world!')
print(f.getvalue())

#读取StringIO
f = StringIO('Hello!\nHi\nGoodbye！')
while True
	s=f.readline()
	if s =='':
		break
	print(s.strip())
	
	
from io import BytesIO	
#二进制操作
f = BytesIO()
f.write('中文'.encode('utf-8'))
print(f.getvalue())

#读取
f=BytesIO(b'\xe4\xb8\xad\xe6\x96\x87')
f.read()




