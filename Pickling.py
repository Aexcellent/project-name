
#pickle.dumps()方法把任意对象序列化成一个bytes
import pickle
d = dict(name='Bob', age=20, score=88)
pickle.dumps(d)


#pickle.dump()直接把对象序列化后写入一个file-like Object
f = open('dump.txt','wb')
pickle.dump(d,f)
f.close()

#反序列化
f = open('dump.txt','rb')
d = pickle.load(f)
f.close()
d

#将python对象转换为JOSN格式
import json
d = dict(name='Bob', age=20, score=80)
json.dumps(d)
#把JOSN反序列化为python对象
json_str='{"age":20,"score":88,"name":"Bob"}'
json.loads(json_str)


#json进阶
import json

class Student(object):
	def __init__(self,name,age,score):
		self.name=name
		self.score=score
		self.age=age
def student2dict(std):
	return {
		'name':std.name
		'age':std.age
		'score':std.score
	}
s=Student('Bob',20,88)
print(json.dumps(s,default=student2dict))
#把任意class的实例变为dict
print(json.dumps(s, default=lambda obj: obj.__dict__))





























