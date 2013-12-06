#!/usr/bin/env python
#-*-coding:utf-8-*-
#from PyNLPIR import *
from EMOTION import getEmotion
import sys,textOpe
import chardet,jieba,jieba.analyse

#将文本转换为自己需要的编码类型
def inverse_need_type(text,need_type):
    text_type = chardet.detect(text)
    codingType = text_type['encoding']
    if codingType != need_type:
        text = text.decode(codingType,'ignore').encode(need_type,'ignore')  
    return text

if __name__ == "__main__":
    filePath = "./DATA/test1.txt"
    file = open(filePath)
    text = file.read()
    keyWords = textOpe.getKeyWords(text,10)
    for each in keyWords:
        print each
        
    emotionType_result = textOpe.getTextEmotion(text)
    print emotionType_result
    '''
    encodeType = chardet.detect(text)
    text = text.decode(encodeType['encoding'],"ignore").encode("utf-8","ignore")
    
    keyWords = jieba.analyse.extract_tags(text,10)
    for each in keyWords:
        print each
        
    emotionType_result = getEmotion.getEmotionType(text)
    
    text = inverse_need_type(text,'utf-8')
    emotionType_result = getEmotion.getEmotionType(text)
    
    text = inverse_need_type(text,'gbk')
    text = text.split('\n')
    size = len(emotionType_result)
    
    num_0 = 0
    num_1 = 0
    num_2 = 0
    
    filePath = ['0.0','1.0','2.0']
    for each in filePath:
        file = open('./DATA/'+each+'.txt','w')
        file.write("")
        file.close()
        
    for i in range(0,size):
        if len(emotionType_result[i])>0:
            file = open('./DATA/'+emotionType_result[i]+'.txt','a')
            file.write(text[i]+'\n')
            file.close()
            if emotionType_result[i] == '0.0':
                num_0 += 1
            elif emotionType_result[i] == '1.0':
                num_1 += 1
            elif emotionType_result[i] == '2.0':
                num_2 += 1
    print num_0,inverse_need_type('的人支持\n','gbk'),num_1,inverse_need_type('的人反对\n','gbk'),num_2,inverse_need_type('的人中立','gbk')
   '''