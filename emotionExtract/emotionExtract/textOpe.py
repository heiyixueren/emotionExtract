#-*-coding:utf-8-*-
from emotionExtract.EMOTION import getEmotion
from emotionExtract import chardet
import jieba,jieba.analyse,os

#将文本转换为自己需要的编码类型
def inverse_need_type(text,need_type):
    text_type = chardet.detect(text)
    codingType = text_type['encoding']
    if codingType != need_type:
        if isinstance(text, unicode):
            text = text.encode(need_type,'ignore')
        else:
            text = text.decode(codingType,'ignore').encode(need_type,'ignore')
    return text
    
#获取关键词
def getKeyWords(text,num):
    text = inverse_need_type(text,'utf-8')
    
    keyWords = jieba.analyse.extract_tags(text,num)
    return keyWords

#获取文本的情感
def getTextEmotion(text):
    text = inverse_need_type(text,'utf-8')
    emotionType_result = getEmotion.getEmotionType(text)
    
    text = text.split('\n')
    size = len(emotionType_result)
    
    num_0 = 0
    num_1 = 0
    num_2 = 0
    
    filePath = ['0.0','1.0','2.0']
    dirPath = os.path.join(os.path.dirname(__file__), 'DATA/').replace('\\','/')
    for each in filePath:
        file = open(dirPath+each+'.txt','w')
        file.write("")
        file.close()
        
    for i in range(0,size):
        if len(emotionType_result[i])>0:
            file = open(dirPath+emotionType_result[i]+'.txt','a')
            file.write(text[i]+'\n')
            file.close()
            if emotionType_result[i] == '0.0':
                num_0 += 1
            elif emotionType_result[i] == '1.0':
                num_1 += 1
            elif emotionType_result[i] == '2.0':
                num_2 += 1
    return {'support':num_0,'oppose':num_1,'neutral':num_2}
    
#格式化文件，提取文件中的微博主要内容
def format_text(text):
    text = text.split("\n")
    size = len(text) - 1
    
    encodeType = chardet.detect(text[1])
    result = ""
    
    print encodeType
    for i in range(0,size):
        text[i] = text[i].split("\t")
        result = result + text[i][10].decode(encodeType['encoding'],"ignore").encode("gbk","ignore") + "\n"
    file.close()
    
    file = open('./data/test.txt','w')
    file.write(result)
    file.close()
    return result