#-*- coding:utf-8 -*-
import hashlib,os
from django.core.exceptions import ObjectDoesNotExist
from emotionExtract.models import *
from emotionExtract.snownlp.snownlp import *
from emotionExtract import textOpe
import jieba.posseg as pseg
import random,string

def insertWords(arg):
    try:
        type = int(arg.get('type'))
        score = float(arg.get('score'))
        lang = int(arg.get('lang'))
        name = arg.get('words')
        if lang == 0:       #如果是中文，去除空格和点号
            name = name.replace('.','')
            name = name.replace(' ','')
        name = normal.zh2hans(name)
        sents = normal.get_sentences(name)
        wordsSet = []
        for each in sents:
            if len(each)>0:
                try:
                    obj = WordSet.objects.get(wordName = each,type = type)
                except ObjectDoesNotExist:
                    wordsSet.append(WordSet(wordName = each,type = type,score = score,lang = lang))
        WordSet.objects.bulk_create(wordsSet)
        
        result = {'flag':0,'info':'插入成功！'}
    except:
        result = {'flag':500,'info':'参数类型有误或漏填！'}
    return result
        
#字的统计
def statisticEachLetter(type):
    wordsSet = WordSet.objects.filter(type = type,lang = 0).values_list('wordName',flat = True)
    
    text = ''.join(wordsSet)
    text = text.replace(' ','')
    text = ''.join(sorted(text))
    '''
    filePath = os.path.join(os.path.dirname(__file__),'DATA/tmp.txt').replace('\\','/')
    file = open(filePath,'w')
    file.write(text.encode('utf-8'))
    file.close()
    '''
    letter = ''
    letterSet = []
    num = 0
    sumNum = 0
    for each in text:
        if each!=' ' and each!=letter:
            if letter=='':
                pass
            else:
                try:
                    obj = LetterSet.objects.get(letterName = letter,type = type)
                    obj.times += num
                    obj.save()
                except ObjectDoesNotExist:
                    letterSet.append(LetterSet(letterName=letter,times=num,score=type,type = type))
                sumNum += num
            letter = each
            num = 1
        elif each == letter:
            num+=1
            
    if len(letterSet)>0:
        LetterSet.objects.bulk_create(letterSet)
    try:
        obj = StatisticLetter.objects.get(stId = 1)
        if type == 1:
            obj.sumToPos += sumNum
        elif type == -1:
            obj.sumToNeg += sumNum
        obj.save()
    except ObjectDoesNotExist:
        if type == 1:
            obj = StatisticLetter(sumToPos = sumNum,sumToNeg = 0)
        else:
            obj = StatisticLetter(sumToPos = 0,sumToNeg = sumNum)
        obj.save()
    
def lettersStatistic():
    statisticEachLetter(-1)
    statisticEachLetter(1)
    return { 'info':'操作成功！','flag':0 }

def getWordScore(arg):
    flag = arg.get('flag')
    word = arg.get('word')
    obj = WordSet.objects.filter(wordName = word)
    tmp = []
    sum = 0
    type = 0
    if obj.count() > 0:
        for each in obj:
            tmp.append({'type':each.type,'score':each.score})
    else:
        s = SnowNLP(word)
        sum = s.sentiments-0.5
        sum = ("%.2f" % sum)
        sum = float(sum)
        if sum>0.1:
            type = 1
        elif sum <-0.1:
            type = -1
        else:
            sum = 0
        tmp = [{'score':sum,'type':type}]
    return tmp

def getSum(arg):
    wordsList = arg.get('wordsList')
    sum = 0
    size = len(wordsList)
    if size == 1:
        each = wordsList[0]
        tmp = each['judge']
        if len(tmp) == 1:
            sum = tmp[0]['score']
        elif len(tmp)>1:
            for each in tmp:
                if each['type'] == -1 or each['type'] == 1 or each['type'] == 3 :
                    sum+= each['score']
    elif size == 2:
        word1 = wordsList[0]['judge']
        sum = 0
        for each1 in word1:
            if each1['type'] == 2 or each1['type'] == 4:
                deep = each1['score']
                for eachT in wordsList[1]['judge']:
                    if eachT['type'] == 1 or eachT['type'] == -1 or eachT['type'] == 3:
                        sum += deep*eachT['score']
            elif each1['type'] == -1 or each1['type'] == 1 or each1['type'] == 3:
                sum += each1['score']
                for eachT in wordsList[1]['judge']:
                    if eachT['type'] == 1 or eachT['type'] == -1 or eachT['type'] == 3:
                        sum += eachT['score']
        
    elif size == 3:
        word0 = wordsList[0]['judge']
        word1 = wordsList[1]['judge']
        word2 = wordsList[2]['judge']
        sum = 0
        for each in word0:
            if each['type'] == 2:
                deep = each['score']
                for each1 in word1:
                    if each1['type'] == 2 or each1['type'] == 4:
                        deep1 = each1['score']
                        for eachT in word2:
                            if eachT['type'] == 1 or eachT['type'] == -1 or eachT['type'] == 3:
                                sum += deep1*eachT['score']
                    elif each1['type'] == -1 or each1['type'] == 1 or each1['type'] == 3:
                        sum += each1['score']
                        for eachT in word2:
                            if eachT['type'] == 1 or eachT['type'] == -1:
                                sum += eachT['score']
                sum = deep*sum
            elif each['type'] == 4:
                for each1 in word1:
                    if each1['type'] == 2:
                        deep1 = each1['score']
                        for eachT in word2:
                            if eachT['type'] == 1 or eachT['type'] == -1 or eachT['type'] == 3:
                                sum += deep1*eachT['score']
                        sum = sum*0.2
                    elif each1['type'] == 4:
                        for eachT in word2:
                            if eachT['type'] == 1 or eachT['type'] == -1 or eachT['type'] == 3:
                                sum += deep1*eachT['score']
                    elif each1['type'] == -1 or each1['type'] == 1 or each1['type'] == 3:
                        sum += each1['score']
                        for eachT in word2:
                            if eachT['type'] == 1 or eachT['type'] == -1 or eachT['type'] == 3:
                                sum += eachT['score']
            elif each['type'] == 1 or each['type'] == -1 or each['type'] == 3:   
                sum += each['score']
                for each1 in word1:
                    if each1['type'] == 2 or each1['type'] == 4:
                        deep1 = each1['score']
                        for eachT in word2:
                            if eachT['type'] == 1 or eachT['type'] == -1 or eachT['type'] == 3:
                                sum += deep1*eachT['score']
                    elif each1['type'] == -1 or each1['type'] == 1 or each1['type'] == 3:
                        sum += each1['score']
                        for eachT in word2:
                            if eachT['type'] == 1 or eachT['type'] == -1 or eachT['type'] == 3:
                                sum += eachT['score']
    return sum
                
def getWindowResult(arg):
    emotionWordsSet = arg.get('emotionWordsSet')
    wordsList = arg.get('wordsList')
    sum = 0
    size = len(wordsList)
    if size>0:
        for i in range(0,size):
            each = wordsList[i]
            if each.get('judge') == None:
                try:
                    obj = WordSet.objects.get(wordName = each.get('word'))
                    '''
                    wordsList[i]['type'] = obj.type
                    wordsList[i]['score'] = obj.score
                    '''
                    wordsList[i]['judge'] = [{'type':obj.type,'score':score}]
                except:
                    #还要做的是，判断不存在的字，或者是词的分数
                    tmp = getWordScore(wordsList[i])
                    '''
                    wordsList[i]['type'] = tmp.get('type')
                    wordsList[i]['score'] = tmp.get('score')
                    '''
                    if emotionWordsSet != None and len(tmp)==1:
                        for eachT in tmp:
                            if eachT.get('score')>0.5 and eachT.get('type')==1:
                                try:
                                    emotionWordsSet[1][each.get('word')] += 1
                                    break
                                except:
                                    emotionWordsSet[1][each.get('word')] = 1
                            elif eachT.get('score')<-0.5 and eachT.get('type')==-1:
                                try:
                                    emotionWordsSet[-1][each.get('word')] += 1
                                    break
                                except:
                                    emotionWordsSet[-1][each.get('word')] = 1
                            elif eachT.get('type')==0:
                                try:
                                    emotionWordsSet[0][each.get('word')] += 1
                                    break
                                except:
                                    emotionWordsSet[0][each.get('word')] = 1
                    wordsList[i]['judge'] = tmp
    
        #根据wordList中的结果集，求取结果和
        sum = getSum({'wordsList':wordsList})
    return sum

#判断某一段语句的情感
def judgeSti(arg):
    emotionWordsSet = arg.get('emotionWordsSet')
    sents = arg.get('sentence')
    sents = sents+'!'
    sents = normal.zh2hans(sents)
    words = pseg.cut(sents)
    #考虑将英文情感词加入到数据库
    wordsList = []
    sum = 0
    for w in words:
        if w.flag != 'x' and len(wordsList)<3:
            wordsList.append({'word':w.word,'flag':w.flag})
        else:
            sum += getWindowResult({'wordsList':wordsList,'emotionWordsSet':emotionWordsSet})
            wordsList = []
    sum = float('%.3f' % sum)
    json = { 'info':'判断成功','score':sum,'flag':0 }
    return json
    
#判断文本中句子的情感
def textTest(arg):
    emotionWordsSet = {1:{},0:{},-1:{}}
    text = arg.get('text')
    text = normal.zh2hans(text)
    sents = text.split('\n')
    result = []
    for each in sents:
        tmp = judgeSti({'sentence':each,'emotionWordsSet':emotionWordsSet})
        result.append(tmp.get('score'))
    for each in emotionWordsSet:
        emotionWordsSet[each] = sorted(emotionWordsSet[each],key=lambda x:emotionWordsSet[each][x],reverse=True)
    
    '''
    resultScore = '\n'.join(map(str,result))
    filePath = os.path.join(os.path.dirname(__file__),'DATA/result.txt').replace('\\','/')
    file = open(filePath,'w')
    file.write(resultScore)
    file.close()
    '''
    return { 'info':'判断成功','score':result,'flag':0,'emotionWords':emotionWordsSet }