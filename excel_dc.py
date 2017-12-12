import xlwt
import mysqlclient

def excel_dc(table_name):
conn=mysqlclient.connect(host='localhost',user='root',passwd='××××',db='test')
cursor=conn.cursor()
count = cursor.execute('select * from '+table_name)

print ('has %s record'% count)

cursor.scroll(0,mode='absolute')   #重置游标位置

results = cursor.fetchall()   #搜取所有结果 results=[[],[]]  len(results)个[],[]中有len(fields)个数
#测试代码，print results
#获取MYSQL里的数据字段
fields = cursor.description      #得到字段名称 field=[[],[],[]]

wbk = xlwt.Workbook()      #创建工作簿
sheet = wbk.add_sheet('sheet1',cell_overwrite_ok=True)  #创建sheet
for ifs in range(0,len(fields)):
    sheet.write(0,ifs,fields[ifs][0])  #将字段写入到EXCEL新表的第一行
ics=1
jcs=0
for ics in range(1,len(results)+1):   #从第二行开始写
    for jcs in range(0,len(fields)):
        sheet.write(ics,jcs,results[ics-1][jcs])
wbk.save('×××××/Desktop/'+table_name+'.xlsx')
