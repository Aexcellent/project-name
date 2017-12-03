import xlrd
import pymysql
#读取EXCEL中内容到数据库中
wb = xlrd.open_workbook('/×.xlsx')  #打开excel文件
sh = wb.sheet_by_index(0) #sh 为excel中的sheet1
dfun=[]
nrows = sh.nrows  #行数
ncols = sh.ncols  #列数
fo=[]

fo.append(sh.row_values(0)) #fo列表中添加sheet1中的第一行数据
for i in range(1,nrows):
      dfun.append(sh.row_values(i))  #dfun列表添加sheet1中的第二行到最后一行数据

conn=pymysql.connect(host='localhost',user='root',passwd='××××××',db='db') #连接数据库
cursor=conn.cursor()  #创建游标

cursor.execute("create table test4("+fo[0][0]+" varchar(100));")  #创建table命名test4，添加第一个字段名

for i in range(1,ncols):
    cursor.execute("alter table test4 add "+fo[0][i]+" varchar(100);")  #按列数，添加新字段名到table
val=''
for i in range(0,ncols):  #1到最后一列
    val = val+'%s,'   #%s指向字段名
print (dfun)

cursor.executemany("insert into resources_networkdevice values("+val[:-1]+");" ,dfun) #数据存入数据库
conn.commit()
cursor.close()
conn.close()

