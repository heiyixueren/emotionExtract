#!/usr/bin/python2.6
# coding: gbk
#Filename: dic.py

'''读入已经分词好的文本文件，构造词典，可以去除停用词，低频词，高频词'''
import pickle
from dic_config import *
import math
from fileutil import save_list
dic = {} # 词典
glo_aff =[] #全局因子
rows=0.0
N1= 0.0
N2 =0.0

Label ={}
# dic里面key为term，每个term对应这一个dic，里面的dic的key为帖子ID，从1开始。
#因此还应该有一个帖子的标签dic，
#输入文件的格式：label    value1    value2

def cons_dic(filename,length,indexes):
    global dic
    global rows
    global Label
    #global N1
    #global N2
    count=0
    f= file(filename,'r')
    fd= file(dust_save_path,'w')
    for line in f.readlines():
        sample = line.strip().split(tc_splitTag)
#        if len(sample)!=line_length:
#            fd.write(line+"\n")
#            continue
        count+=1
        rows+=1 #统计样本的总行数
#        if int(sample[0])==1: #统计正样本的行数
#            N1+=1
#        if int(sample[0])==-1: #统计反样本的行数
#            N2+=1
        #Label[count]=float(sample[0])#将每个样本的类标签加入到词典中。key=id，value=类标签
        string =""
        string = sample[indexes[0]]
        if len(indexes)>1:
            for i  in range(1,len(indexes)):
                string += str_splitTag+sample[indexes[i]]
        for term in string.strip().split(str_splitTag):
            if len(term.strip())==0:
                continue
            term = term.strip()
            if term in dic:
                if count in dic[term]:
                    dic[term][count]+=1
                else:
                    dic[term][count]=1
            else:
                dic[term]={}
                dic[term][count]=1
    f.close()  
    fd.close()          
    return dic

def cal_glo_aff(fun):
    global dic
    global rows
    global glo_aff
    glo_aff=[]
    for key in dic.keys():
        glo_aff +=[fun(dic[key])]
    return glo_aff
def Glo1(dic):
    return 1

def Glo2(dic):
    #log(N/n)
    return math.log(float(rows)/float(len(dic)))

def Glo3(dic):
    #log(|n1-n2|+1)
    n1=0
    n2=0
    for key in dic.keys():
        if Label[key]==1:
            n1+=1
        if Label[key]==-1:
            n2+=1
    return math.log(abs(n1-n2)+1.1)

def Glo4(dic):
    #log(|n1/N1-n2/N2|+1)
    n1=0
    n2=0
    for key in dic.keys():
        if Label[key]==1:
            n1+=1
        if Label[key]==-1:
            n2+=1
    return math.log(abs(n1/float(N1)-n2/float(N2))+1.1)

def Glo5(dic):
    #log(|n1*N2-n2*N1|/N+1)
    n1=0
    n2=0
    for key in dic.keys():
        if Label[key]==1:
            n1+=1
        if Label[key]==-1:
            n2+=1
    return math.log(abs(n1*N2-n2*N1)/float(rows)+1.1)

def remove_term_by_stopwords(stopwords_filename):
    global dic 
    for line in file(stopwords_filename,'r').readlines():
        if line.strip() in dic:
            del dic[line.strip()]
        
def remove_term_by_frequent(min,max): 
    global dic     
    for key in dic.keys():
        if len(dic[key])<min or len(dic[key])>max:
            del dic[key]

def save_keys(save_path):
    '''the format of the key :keys,index,frequant'''
    global dic      
    f = file(save_path,'w')
    count=0
    for key in dic.keys():
        count+=1
        f.write(key.strip()+"\t"+str(count)+"\t"+str(len(dic[key]))+"\n")
    f.close()

def save_dic(save_path): 
    global dic   
    pickle.dump(dic,open(save_path,'w')) 
def load_dic(load_path):
    global dic 
    dic2= pickle.load(open(load_path,'r'))

def save_glo(save_path):
    save_list(save_path,glo_aff)
def main():
    global glo_aff
    global dic
    for filename in files:
       filename = filepath+filename
       cons_dic(filename,line_length,indexes)
    print "处理样本的行数为"+str(rows)
    #remove_term_by_stopwords(stopwords_filename) 
    #remove_term_by_frequent(min,max)
    save_keys(key_save_path)
    save_dic(dic_save_path)
    #save_glo(glo_aff_save_path)
    del dic #删除dic，释放内存

main()