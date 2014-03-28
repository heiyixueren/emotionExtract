#-*- coding:utf-8 -*-
from django.db import models
from django.contrib import admin

class LetterSet(models.Model):
    letterId = models.AutoField('ID', primary_key=True)
    letterName = models.CharField(max_length = 10)              #字的名字
    times = models.IntegerField(default = 0)                    #出现的次数
    type = models.IntegerField()                                #类型 >0积极 =0中 <0消极
    score = models.FloatField()                                 #该字的评分
    
    def __unicode__(self):
        return self.letterId
        
class WordSet(models.Model):
    wordId = models.AutoField('ID',primary_key=True)
    wordName = models.CharField(max_length = 50)
    type = models.IntegerField()                                #-1消极 0中 1积极 2程度副词 3语气词 4否定词
    score = models.FloatField()                                 #该词语的评分
    lang = models.IntegerField(default = 0)                     #语言，默认为中文
    
    def __unicode__(self):
        return self.wordId
        
class StatisticLetter(models.Model):
    stId = models.AutoField('ID',primary_key=True)
    sumToNeg = models.IntegerField(null = True)                 #消极词汇统计
    sumToPos = models.IntegerField(null = True)                 #积极词汇统计
    
    def __unicode__(self):
        return self.stId
