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
from emotionExtract import textOpe
from django import forms
from django.http import HttpResponseRedirect
from django.utils import simplejson

#open the home page
def openIndexPage(request):
    return render_to_response('index.html')
    
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