#!/usr/bin/python2.6
# coding: gbk
#Filename: im_detect.py

from ctm_predict_model import *
from ctm_train_model import cons_vec_for_cla,cons_svm_problem
from svmutil import svm_predict,svm_load_model
from fileutil import read_list,read_dic
from ban_check_config import *
from result_anlysis import *
from numpy import *
from lsa import *
import time

'''旺旺欺诈聊天监控程序'''
c_p = os.path.dirname(os.getcwd())+"/"

'''输入文件的配置'''
#filepath="G:/x项目/Taobao/数据/旺旺欺诈聊天/"
filepath="D:/张知临/数据/旺旺欺诈聊天/"
files = ["qizha_test_20111010aa_gbk","qizha_test_20111010ab_gbk","qizha_test_20111010ac_gbk"]
#filename = "D:/张知临/数据/旺旺欺诈聊天/im_info_2_gbk.txt"
tc_splitTag="\t"
str_splitTag ="^"
delete = False
indexes= [6,7,8,9,10]
change_decode=False
in_decode = "UTF-8" #the decode
out_encode ="GBK" # the encode

'''普通SVM模型的配置'''
model_main_path = c_p + "model/im_info/10.19_33000/model/"
svm_model_path=model_main_path+"im.model"
dic_path = model_main_path +"dic.key"

'''以下为LSA模型的配置'''
decom_meas= 1
k=20
LSA_path = model_main_path+"lsa_ban_"+str(k)
LSA_model_path = model_main_path+"LSA_ban_"+str(k)+".model"
dust_save_path = model_main_path+"dust.txt"

'''结果存放的路径'''
result_indexes = [1,2,3,4,5,6,7,8,9,10] # 需要同结果一同保存的数据
#result_save_path = model_main_path+str(time.strftime('%Y-%m-%d@%H-%M',time.localtime(time.time())))+"_im.result"
statistics_result_save_path =os.path.dirname(model_main_path)+"/result/"+str(time.strftime('%Y-%m-%d@%H-%M',time.localtime(time.time())))+"_im.statistics"
best_param_result_save_path= model_main_path+str(time.strftime('%Y-%m-%d@%H-%M',time.localtime(time.time())))+"_im.best_param"


def read_result(result_save_path):
    f = file(result_save_path,'r')
    X=[]
    for line in f.readlines():
        arr = line.strip().split("\t")
        X+=[arr]
    return X
    
def ban_static(result_save_path,statistics_result_save_path,first_range=[x/10.0 for x in range(0,10)],second_range=[0,0.5]):
    X=read_result(result_save_path)
    X=array(X)
    f= file(statistics_result_save_path,'w')
    cal_affect(f,X[:,0],X[:,1],"向量空间模型",first_range)
    cal_affect(f,X[:,0],X[:,2],"LSA模型",first_range)   
    do_statis(f,X[:,0],X[:,1],"向量空间模型",second_range)
    do_statis(f,X[:,0],X[:,2],"LSA模型",second_range)
    f.close()
  
def main():
    print "--------------欢迎使用旺旺欺诈聊天监控系统------------------"
    choice = int(raw_input("1为监控旺旺聊天记录； 2为评估结果；0为退出模型"))
    while choice!=0:
        if choice==1:
            for file in files:
                filename = filepath+file
                str_time = time.clock()
                result_save_path = os.path.dirname(model_main_path)+"/result"+str(time.strftime('%Y-%m-%d@%H-%M',time.localtime(time.time())))+"_im.result"
                ctm_predict(filename,indexes,dic_path,result_save_path,result_indexes,svm_model_path,str_splitTag=str_splitTag,tc_splitTag=tc_splitTag,delete=delete,change_decode=change_decode,in_decode=in_decode,out_encode=out_encode)
                print "时间为",str(time.clock()-str_time)
        if choice==2:
            ban_static(result_save_path,statistics_result_save_path)

        choice = int(raw_input("1为监控违禁品； 2为评估结果；0为退出模型"))
main() 
    