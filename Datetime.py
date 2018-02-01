

from datetime import datetime

#获取当前日期和时间
now = datetime.now()
print(now)

#获取指定日期和时间
dt=datetime(2015,4,19,12,20)

#一个datetime类型转换为timestamp
dt.timestamp()
#反过来
t=1429417200.0
print(datetime.fromtimestamp(t))
#转换到UTC标准时区的时间
print(datetime.utcfromtimestamp(t))

#str转为datetime
cday = datetime.striptime('2015-6-1 18:19:59','%Y-%m-%d %H:%M:%S')
#反过来
now=datetime.now()
print(now.strftime('%a,%b %d %H:%M'))

#datetime加减
from datetime import datetime, timedelta
now=datetime.now
now + timedelta(hours=10)
now - timedelta(days=1)
now + timedelta(days=2,hours=12)


#本地时间转换为UTC时间

#强制设置时区
from datetime import datetime,timedelta,timezone
tz_utc_8 = timezone(timedelta(hours=8))
now=datetime.now()
dt = now.replace(tzinfo=tz_utc_8)

#时区转换通过utcnow()拿到当前utc时间
utc_dt = datetime.utcnow().replace(tzinfo=timezone.utc)
# astimezone()将转换时区为北京时间:
bj_dt = utc_dt.astimezone(timezone(timedelta(hours=8)))






































