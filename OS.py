
import os

os.environ
os.environ.get('PATH')

# 查看当前目录的绝对路径:
os.path.abspath('.')
# 在某个目录下创建一个新目录，首先把新目录的完整路径表示出来:
os.path.join('/Users/michael','testdir')
# 然后创建一个目录:
os.mkdir('/Users/michael/testdir')
# 删掉一个目录:
os.rmdir('/Users/michael/testdir')
#把一个路径拆分为两部分
os.path.split('/Users/michael/testdir/file.txt')
#os.path.splitext()可以直接让你得到文件扩展名
os.path.splitext('/path/to/file.exe')

os.rename('test.txt','test.py')
os.remove('test.py')

#列出当前目录下的所有目录：
[x for x in os.listdir('.') if os.path.isdir(x)]
#列出所有的.py文件：
[x for x in os.listdir('.') if os.path.isfile(x) and os.path.splitext(x)[1]=='.py']









