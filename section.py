

L = ['Michael', 'Sarah', 'Tracy', 'Bob', 'Jack']
L[:3]
L[1:3]
L[-2:]
L[-1:]


L = list(range(100))
L
L = [:10]
L = [-10:]
L[:10:2]  #前10个数，每两个取一个
L[::5]    #所有数，每5个取一个
L[:]     #只写[:]就可以原样复制一个list


#tuple和str的切片操作类似