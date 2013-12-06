#-*- coding: utf-8 -*-
import sqlite3
if __name__ == '__main__':

    cx= sqlite3.connect("C:\\Users\\Administrator\\Desktop\\file4mk\\data\\temporalTweet.db")
    cu = cx.cursor()
    cu.execute("SELECT name FROM sqlite_master WHERE type='table' ORDER BY name")
    tables = cu.fetchall()
    point = 0
    
    file = open("twitter.txt","w")
    for each in tables:
        cu.execute("select tweet from "+each[0])
        result = cu.fetchall()
        for i in range(0,len(result)-1):
            file.write(result[i][0].encode("gbk",'ignore')+"\n")
        point +=1 
        if point == 100:
            break
    cx.commit()

	
    '''
    file = open("twitter.txt")
    file1 = open("twitterData/twitterTestData.txt","w")
    
    text = file.read()
    text = text.split("\n")
    for each in text:
        if len(each) > 5:
            file1.write("0\t"+each+"\n")
    
    cx= sqlite3.connect("C:\\Users\\Administrator\\Desktop\\file4mk\\data\\temporalTweet.db")
    cu = cx.cursor()
    cu.execute("SELECT name FROM sqlite_master WHERE type='table' ORDER BY name")
    tables = cu.fetchall()
    point = 0
    
    file = open("twitter.txt","w")
    for each in tables:
        if point > 100:
            cu.execute("select tweet from "+each[0])
            result = cu.fetchall()
            for i in range(10,20):
                file.write(result[i][0].encode("gbk",'ignore')+"\n")
        point +=1 
        if point == 110:
            break
    cx.commit()
    '''