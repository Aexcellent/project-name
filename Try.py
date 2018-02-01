

try：
	print('try...')
	r=10/0
	print('result:',r)
except ZeroDivisionError as e:
	print('except:',e)
finally:
	print('finally...')
print('END')

#同样是出错，但程序打印完错误信息后会继续执行，并正常退出
import logging

def foo(s):
	return 10/int(s)

def bar(s):
	return foo(s)/2
	
def main():
	try: 
		bar('0')
	except Exception as e:
		logging.exception(e)
		
import pdb

s='0'
n=int(s)
pdb.set_trace()  # 运行到这里会自动暂停
print (10/n)














		
	
	
	
	
	