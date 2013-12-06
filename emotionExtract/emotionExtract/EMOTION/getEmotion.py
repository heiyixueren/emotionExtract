#-*- coding:utf-8 -*-
from src import tms
import os

def formatInput(text):
    text = text.split("\n")
    curpath = os.path.join(os.path.dirname(__file__), 'twitterData/twitterTestData.txt').replace('\\','/')
    #file = open("./EMOTION/twitterData/twitterTestData.txt","w")
    file = open(curpath,'w')
    for each in text:
        file.write("0\t"+each+"\n")
        
def getEmotionType(text):
    formatInput(text)
    curpath = os.path.join(os.path.dirname(__file__), 'twitterData/').replace('\\','/')
    #tms.tms_segment("./EMOTION/twitterData/twitterTestData.txt",[1],"./EMOTION/twitterData/twitterTestData1.txt","^","\t",1)
    tms.tms_segment(curpath+"twitterTestData.txt",[1],curpath+"twitterTestData1.txt","^","\t",1)
    
    #情感预测,0积极，1消极，2中立
    tms.tms_predict(curpath+"twitterTestData1.txt",curpath+"emotion/model/tms.config",result_save_path=curpath+"emotion/tms.result")
    file1 = open(curpath+"emotion/tms.result")
    text1 = file1.read()
    text1 = text1.split("\n")
    result = []
    for each in text1:
        each = each.split('\t')
        result.append(each[0])
    return result