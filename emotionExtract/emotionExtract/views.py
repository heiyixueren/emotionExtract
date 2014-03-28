#-*- coding:utf-8 -*-
from django.http import HttpResponse
from urllib import unquote
from django.template.loader import get_template
from django.shortcuts import render_to_response
from django.core.context_processors import csrf
from django.contrib.auth.models import User
from datetime import *
import random,string
import re,os
from emotionExtract import textOpe,chardet,dbOpe
from django import forms
from django.http import HttpResponseRedirect
from django.utils import simplejson

def getJson(json):
    return simplejson.dumps(json,ensure_ascii=False)
    
def releaseJson(json):
    return simplejson.loads(json)
    
#open the home page
def text(request):
    return render_to_response('text.html')
    
#open the home page
def pageList(request):
    return render_to_response('pageList.html')
    
#open the home page
def openIndexPage(request):
    return render_to_response('index.html')
    
#打开词语操作页面
def openWordsPage(requset):
    return render_to_response('insertWords.html')
    
#插入数据
def insertWords(request):
    myJson = None
    result = "插入成功"
    if request.method == 'POST':
        myJson = request.POST.get('content')
    else:
        myJson = request.GET.get('content')
        
    if myJson!=None:
        myJson = releaseJson(myJson)
        words = myJson.get('words')
        type = myJson.get('type')
        score = myJson.get('score')
        lang = myJson.get('lang')
        if lang == None:
            myJson['lang'] = 0
        if words!=None and type!=None and score!=None and len(words)>0:
            result = dbOpe.insertWords(myJson)
        else:
            result = "数据不完整！"
    else:
        result = "数据为空！"
    
    return HttpResponse(getJson(result))
    
def getMsg(request):
    if request.method == 'POST':
        text = request.POST.get('text')
        textType = int(request.POST.get('textType'))
        num = int(request.POST.get('keyNum'))
    else:
        text = request.GET.get('text')
        textType = int(request.GET.get('textType'))
        num = int(request.GET.get('keyNum'))
    if textType == 1:  
        text = textOpe.format_text(text)
    keywords = textOpe.getKeyWords(text,num)
    emotion = textOpe.getTextEmotion(text)
    emotionList = []
    
    filePath = ['0.0','1.0','2.0']
    dirPath = os.path.join(os.path.dirname(__file__), 'DATA/').replace('\\','/')
    for each in filePath:
        file = open(dirPath+each+'.txt')
        text = file.read()
        tmpKeyWords = textOpe.getKeyWords(text,num)
        emotionList.append(" ".join(tmpKeyWords))
        file.close()
    return HttpResponse(simplejson.dumps({'keywords':keywords,'emotion':emotion,'emotionList':emotionList}))
    
#统计字的频率
def lettersStatistic(request):
    json = dbOpe.lettersStatistic()
    return HttpResponse(getJson(json))
    
#判断情感
def judgeSti(request):
    if request.method == 'POST':
        myJson = request.POST.get('content')
        if myJson != None:
            myJson = releaseJson(myJson)
            sentence = myJson.get('sentence')
            if sentence!=None and len(sentence)>0:
                json = dbOpe.judgeSti(myJson)
            else:
                json = {'info':'参数为空！','flag':500}
        else:
            json = {'info':'参数为空！','flag':500}
    else:
        return render_to_response('judgeStiPage.html')
        
    return HttpResponse(getJson(json))
    
#判断文本情感
def textTest(request):
    if request.method == 'POST':
        myJson = request.POST.get('content')
        if myJson != None:
            myJson = releaseJson(myJson)
            text = myJson.get('text')
            if text!=None and len(text)>0:
                json = dbOpe.textTest(myJson)
            else:
                json = {'info':'参数为空！','flag':500}
        else:
            json = {'info':'参数为空！','flag':500}
    else:
        return render_to_response('textTest.html')
        
    return HttpResponse(simplejson.dumps(json,ensure_ascii=True))