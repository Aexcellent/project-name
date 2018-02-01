

class Student(object):
	def __int__(self,name,score):
	self.name=name 
	self.__score=score   #外部无法访问
	
	def get_score(self):
		return self.__score
	def set_score(self, score):
		if 0<=score<=100:
			self.__score=score
		else:
			raise ValueError('bad score')
	def print_score(self):
		print('%s:%s',self.name,self.score)
		
	def get_grade(self):
		if self.score >= 90:
			return 'A'
		elif self.score >= 60:
			return 'B'
		else:
			return 'C'