#!/usr/bin/python2.6
# coding: gbk
#Filename: dic.py

'''�����Ѿ��ִʺõ��ı��ļ�������ʵ䣬����ȥ��ͣ�ôʣ���Ƶ�ʣ���Ƶ��'''
import pickle
from dic_config import *
import math
from fileutil import save_list
dic = {} # �ʵ�
glo_aff =[] #ȫ������
rows=0.0
N1= 0.0
N2 =0.0

Label ={}
# dic����keyΪterm��ÿ��term��Ӧ��һ��dic�������dic��keyΪ����ID����1��ʼ��
#��˻�Ӧ����һ�����ӵı�ǩdic��
#�����ļ��ĸ�ʽ��label    value1    value2

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
        rows+=1 #ͳ��������������
#        if int(sample[0])==1: #ͳ��������������
#            N1+=1
#        if int(sample[0])==-1: #ͳ�Ʒ�����������
#            N2+=1
        #Label[count]=float(sample[0])#��ÿ�����������ǩ���뵽�ʵ��С�key=id��value=���ǩ
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
    print "��������������Ϊ"+str(rows)
    #remove_term_by_stopwords(stopwords_filename) 
    #remove_term_by_frequent(min,max)
    save_keys(key_save_path)
    save_dic(dic_save_path)
    #save_glo(glo_aff_save_path)
    del dic #ɾ��dic���ͷ��ڴ�

main()