#-*- coding: utf-8 -*-
import tms
import datetime
import time

def timediff(timestart, timestop):
    t  = (timestop-timestart)
    time_day = t.days
    s_time = t.seconds
    ms_time = t.microseconds / 1000000
    usedtime = int(s_time + ms_time)
    time_hour = usedtime / 60 / 60
    time_minute = (usedtime - time_hour * 3600 ) / 60
    time_second =  usedtime - time_hour * 3600 - time_minute * 60
    time_micsecond = (t.microseconds - t.microseconds / 1000000) / 1000
    retstr = "%d天%d小时%d分%d秒%d毫秒"  %(time_day, time_hour, time_minute, time_second, time_micsecond)
    return retstr

if __name__ == '__main__':
    beginTime = datetime.datetime.now()
    tms.tms_train("../twitterData/twitterTrain.txt",main_save_path="./",seg=1,global_fun ='idf')
    tms.tms_segment("../twitterData/twitterTestData.txt",[1],"../twitterData/twitterTestData1.txt","^","\t",1)
    tms.tms_predict("../twitterData/twitterTestData1.txt","./model/tms.config",result_save_path="../twitterData/tms.result")
    endTime = datetime.datetime.now()
    d = timediff(beginTime , endTime)
    print d
