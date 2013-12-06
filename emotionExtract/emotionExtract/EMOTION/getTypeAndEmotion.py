#-*- coding:utf-8 -*-
from src import tms
import sqlite3

def formatInput(text):
    text = text.split("\n")
    file = open("./twitterData/twitterTestData.txt","w")
    for each in text:
        file.write("0\t"+each.encode("utf-8","ignore")+"\n")
        
#返回的直接就是字符串型的类型    
def getTypeStr(text):
    dir = ["新闻，娱乐类","自然灾难","航空事件","食品药物安全","饮食","科教，教育","国际事件","招聘","犯罪事件","交通事故","经济金融类","环境问题","其他","煤矿事件","医疗，疾病","科技"]
    dir1 = ["积极","消极","中立"]
    formatInput(text)
    tms.tms_segment("./twitterData/twitterTestData.txt",[1],"./twitterData/twitterTestData1.txt","^","\t",1)
    
    #类型预测
    tms.tms_predict("./twitterData/twitterTestData1.txt","./twitterData/type_model/model/tms.config",result_save_path="./twitterData/tms.result")
    file = open("twitterData/tms.result")
    text = file.read()
    text = text.split("\n")
    
    #情感预测
    tms.tms_predict("./twitterData/twitterTestData1.txt","./twitterData/emotion/model/tms.config",result_save_path="./twitterData/emotion/tms.result")
    file1 = open("twitterData/emotion/tms.result")
    text1 = file1.read()
    text1 = text1.split("\n")
    
    result = []
    for i in range(0,len(text)):
        if len(text[i]) > 0:
            each = text[i].split("\t")
            point = int(float(each[0]))
            
            each1 = text1[i].split("\t")
            point1 = int(float(each1[0]))
            
            result.append([dir[point].decode("utf-8"),dir1[point1].decode("utf-8")])
    return result

#返回数值类型的类型结果
def getTypeInt(text):
    formatInput(text)
    tms.tms_segment("./twitterData/twitterTestData.txt",[1],"./twitterData/twitterTestData1.txt","^","\t",1)
    
    #类型预测
    tms.tms_predict("./twitterData/twitterTestData1.txt","./twitterData/type_model/model/tms.config",result_save_path="./twitterData/tms.result")
    file = open("twitterData/tms.result")
    text = file.read()
    text = text.split("\n")
    
    #情感预测
    tms.tms_predict("./twitterData/twitterTestData1.txt","./twitterData/emotion/model/tms.config",result_save_path="./twitterData/emotion/tms.result")
    file1 = open("twitterData/emotion/tms.result")
    text1 = file1.read()
    text1 = text1.split("\n")
    
    result = []
    for i in range(0,len(text)):
        if len(text[i]) > 0:
            each = text[i].split("\t")
            point = int(float(each[0]))
            
            each1 = text1[i].split("\t")
            point1 = int(float(each1[0]))
            
            result.append([point,point1])
    return result

def insertTypeAndEmotionToTwitter(cu,cx):
    cu.execute("SELECT `mid`,`tweet`,`date` FROM `eventProject_tweets`")
    twitters = cu.fetchall()
    point = 0
    for each in twitters:
        mid = str(each[0])
        twitterData = each[1]
        tdate = each[2]
        
        #cu.execute("select `date` from `eventProject_tweets` where `mid`="+mid)
        #tdate = cu.fetchall()
        
        if tdate<'2013-02-01' or tdate>'2013-02-30':
            continue
            
        result = getTypeInt(twitterData)
        type = str(result[0][0])
        emotion = str(result[0][1])
        
        cu.execute("UPDATE `eventProject_tweets` SET `topic`="+type+",`emotion`="+emotion+" WHERE `mid`="+mid)
        cu.fetchall()
        
        point += 1
        if point % 100 == 0:
            print point
            cx.commit()
            
    cx.commit()
    
def insertTypeAndEmotionToEntity(cu,twitter_id,id,cx):
    mid_list = twitter_id.split("|")
    type = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
    emotion = [0,0,0]
    
    for mid in mid_list:
        cu.execute("SELECT `topic`,`emotion` FROM `eventProject_tweets` WHERE `mid`="+mid)
        ss = cu.fetchall()
        if ss[0][0]<0 or ss[0][1] is None:
            continue
        ss0 = int(ss[0][0])
        ss1 = int(ss[0][1])
        type[ss0] += 1
        emotion[ss1] += 1
        
    n_type = type[0]
    n = 0
    for i in range(0,len(type)):
        if type[i] > n_type:
            n_type = type[i]
            n = i
    if n_type == 0:
        n_type = -1
        
    r_emotion = str(emotion[0])+"|"+str(emotion[1])+"|"+str(emotion[2])
    
    cu.execute("UPDATE `eventProject_calendarentry` SET `topic`="+str(n)+",`emotion`='"+r_emotion+"' WHERE `id`="+str(id))
    cu.fetchall()
    
if __name__ == "__main__":
    urlpath = "C:\\Users\\Administrator\\Desktop\\file4mk\\EventProject\\EventProject\\sqlite.db"
    cx= sqlite3.connect(urlpath)
    cu = cx.cursor()
    #cu.execute("alter table `eventProject_tweets` add column `emotion` int")
    #cu.fetchall()
    
    insertTypeAndEmotionToTwitter(cu,cx)
    '''
    cu.execute("select `date`,`topic` from `eventProject_calendarentry` limit 0,1")
    temp = cu.fetchall()
    print temp[0][0],temp[0][1]
    '''

    cu.execute("select `id`,`tweet` from `eventProject_calendarentry` limit 15000,35000")
    text = cu.fetchall()
    point = 0
    for each in text:
        id = each[0]
        twitter_id = each[1]
        point += 1
        insertTypeAndEmotionToEntity(cu,twitter_id,id,cx)
        
        if point % 100 == 0:
            print point
            cx.commit()
            
    cx.commit()
    #cu.execute("UPDATE `eventProject_calendarentry` SET `topic`="+type+" `emotion`="+emotion+" WHERE `id`="+id)
    
    