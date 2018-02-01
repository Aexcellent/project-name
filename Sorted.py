

#Python内置的sorted()函数就可以对list进行排序
sorted([36,5,-12,9,-21])
#Python内置的sorted()函数就可以对list进行排序
sorted([36,5,-12,9,-21], key=abs)
#字母序排列
sorted(['bob','about','Zoo','Credit'],key=str.lower)
#上述反向排序
sorted(['bob','about','Zoo','Credit'],key=str.lower，reverse=True)
