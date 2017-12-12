d = {'Michael': 95,'Bob': 75,'Tracy': 85}
d['Michael']
d['Adam'] = 67     #把数据放入dict的方法，除了初始化时指定外，还可以通过key放入
d['Adam'] = 68     #由于一个key只能对应一个value，所以，多次对一个key放入value，后面的值会把前面的值冲掉


'Thomas' in d #通过in判断key是否存在
d get('Thomas')
d get('Thomas', -1)   #过dict提供的get()方法，如果key不存在，可以返回None，或者自己指定的value


d pop('Bob')  #要删除一个key，用pop(key)方法，对应的value也会从dict中删除


///
dict可以用在需要高速查找的很多地方，在Python代码中几乎无处不在，正确使用dict非常重要，需要牢记的第一条就是dict的key必须是不可变对象。

这是因为dict根据key来计算value的存储位置，如果每次计算相同的key得出的结果不同，那dict内部就完全混乱了。这个通过key计算位置的算法称为哈希算法（Hash）。

要保证hash的正确性，作为key的对象就不能变。在Python中，字符串、整数等都是不可变的，因此，可以放心地作为key。而list是可变的，就不能作为key
///


s = set([1,2,3])   #注意，传入的参数[1, 2, 3]是一个list，而显示的{1, 2, 3}只是告诉你这个set内部有1，2，3这3个元素，显示的顺序也不表示set是有序的。
s = set([1,1,2,2,3,3])   #重复元素在set中自动被过滤

s.add(4)
s.remove(4)

s1 = set([1,2,3])
s2 = set([2,3,4])
s1 & s2      #交集
s1 | s2      #并集

#set和dict的唯一区别仅在于没有存储对应的value，但是，set的原理和dict一样
#所以，同样不可以放入可变对象，因为无法判断两个可变对象是否相等，也就无法保证set内部“不会有重复元素”。
#把list放入set，会报错。


a = ['c','b','a']
a.sort()
a            #对于可变对象，比如list，对list进行操作，list内部的内容是会变化的


a = 'abc'
b = a.replace('a','A')
a
b
#对于不变对象来说，调用对象自身的任意方法，也不会改变该对象自身的内容。相反，这些方法会创建新的对象并返回，这样，就保证了不可变对象本身永远是不可变的。











       










