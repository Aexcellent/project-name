import numpy

x = numpy.round(numpy.random.normal(0,1,100),2)
#round方法四舍五入，保留两位小数
#numpy.random.normal 令μ等于0，σ等于1，按正态分布抽样100次

y = numpy.round(numpy.random.uniform(1,5,100),2)
#numpy.random.uniform 在区间[1,5]上按均匀分布抽取100次

z = numpy.round(numpy.random.binomial(100,1/2,100),2)
#numpy.random.binomial 令n=100 p=1/2按二项分布抽取100次

n = numpy.round(numpy.random.poisson(2,100),0)
#numpy.random.poisson 令λ=2 按泊松分布抽取100次

m = numpy.round(numpy.random.exponential(5,100)，2)
#numpy.random.exponential 令λ=5 按指数分布抽取100次
