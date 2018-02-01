

with open ('/path/to/file','r') as f:
	f.read()

	
#实现上下文管理是通过__enter__和__exit__这两个方法实现的

#@contextmanager

from contextlib import contextmanager

class Query(object):

    def __init__(self, name):
        self.name = name

    def query(self):
        print('Query info about %s...' % self.name)

@contextmanager
def create_query(name):
    print('Begin')
    q = Query(name)
    yield q
    print('End')
with create_query('Bob') as q:
    q.query()	
	
	
	
	
