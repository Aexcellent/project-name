

#namedtuple
from collections import namedtuple
Point = namedtuple('Point',['x','y'])
p.Point(1,2)
# namedtuple('名称', [属性list]):


#deque是为了高效实现插入和删除操作的双向列表，适合用于队列和栈
from collections import deque
q = deque(['a','b','c'])
q.append('x')
q.appendleft('y')

#defaultdict
#如果希望key不存在时，返回一个默认值，就可以用defaultdict
from collections import defaultdict
dd=defaultdict(lambda:'N/A')


#OrderedDict保持Key的顺序
from collections import OrderedDict
od = OrderedDict([('a',1),('b',2)])


#Counter简单的计数器
from collections import Counter
c=Counter()
for ch in 'programing':
	c[ch]=c[ch]+1

















