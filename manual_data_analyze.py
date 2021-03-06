import numpy as np
import datetime
import time

data = [['6-25-2016/7:48:03',  5.0],['6-25-2016/7:50:04', 5.2],['6-25-2016/7:50:54', 4.4],['6-25-2016/7:52:04', 5.8],['6-25-2016/7:53:36', 3.9],['6-25-2016/7:55:12', 4.9],['6-25-2016/7:57:00',  3.5],['6-25-2016/7:59:20', 4.8],['6-25-2016/8:00:37', 5.8],
['6-25-2016/8:06:04', 8.6],['6-25-2016/8:07:57', 10.7],['6-25-2016/8:11:03', 8.3],['6-25-2016/8:13:32', 10.4],['6-25-2016/8:15:23', 3.0],['6-25-2016/8:19:40', 9.4],['6-25-2016/8:21:47', 6.6],['6-25-2016/8:23:12', 10.2],['6-25-2016/8:24:30', 12.3],['6-25-2016/8:26:27', 9.8],
['6-25-2016/8:31:11', 8.0],['6-25-2016/8:32:47', 10.9],['6-25-2016/8:34:20', 6.8],['6-25-2016/8:36:39', 7.7],['6-25-2016/8:40:00', 7.7]]

mdata =  np.asarray(data)

newdata = []
dtime = ''
ddepth = ''
length = mdata.shape[0]
for i in range(length):
    dtime =  time.mktime((datetime.datetime.strptime(mdata[i,0], '%m-%d-%Y/%H:%M:%S')).timetuple())    
    ddepth = mdata[i,1]
    newdata.append([dtime , ddepth])
    
print newdata
