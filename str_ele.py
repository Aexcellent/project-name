

print ('I\'m ok.')  #\为转义字符
print ('I\'m learning\npython') #\n为换行符
print ('\\\t\\') #输出为：\		\
print (r'\\\t\\') #输出为：\\\t\\，r''表示''内内容默认不转义
print ('''line1
line2
line3''')  #'''...'''表示多行内容





print ('包含中文的str')
ord ('A')  #输出为：65      获取字符整数表示
ord ('中') #输出为： 20013
chr (66)   #输出为：'B'     把编码转换成对应字符
chr (25991)#输出为：'文'



///由于Python的字符串类型是str，在内存中以Unicode表示，一个字符对应若干个字节。如果要在网络上传输，或者保存到磁盘上，就需要把str变为以字节为单位的bytes。

Python对bytes类型的数据用带b前缀的单引号或双引号表示：///

x = b'Abc'
#要注意区分'ABC'和b'ABC'，前者是str，后者虽然内容显示得和前者一样，但bytes的每个字符都只占用一个字节。


#以Unicode表示的str通过encode()方法可以编码为指定的bytes
'ABC'.encode('ascii')
'中文'.encode('utf-8')
///
纯英文的str可以用ASCII编码为bytes，内容是一样的，含有中文的str可以用UTF-8编码为bytes。含有中文的str无法用ASCII编码，因为中文编码的范围超过了ASCII编码的范围，Python会报错。

在bytes中，无法显示为ASCII字符的字节，用\x##显示。
///

b'ABC'.decode('ascii')
b'\xe4\xb8\xad\xe6\x96\x87'.decode('utf-8') #输出：'中文'


len('ABC')   #显示字符数
len(b'ABC')  #显示字节数








#格式化方法
'Hello, %s' %'world'
'Hi, %s, you have $%d.' %('Michael', 100000) 
///
占位符	替换内容
%d	整数
%f	浮点数
%s	字符串
%x	十六进制整数
///

'Hello, {0},成绩提升了 {1:.1f}%'.format('小明', 17.125)














