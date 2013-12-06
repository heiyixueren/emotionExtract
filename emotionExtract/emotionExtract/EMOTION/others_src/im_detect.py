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

'''������թ�����س���'''
c_p = os.path.dirname(os.getcwd())+"/"

'''�����ļ�������'''
#filepath="G:/x��Ŀ/Taobao/����/������թ����/"
filepath="D:/��֪��/����/������թ����/"
files = ["qizha_test_20111010aa_gbk","qizha_test_20111010ab_gbk","qizha_test_20111010ac_gbk"]
#filename = "D:/��֪��/����/������թ����/im_info_2_gbk.txt"
tc_splitTag="\t"
str_splitTag ="^"
delete = False
indexes= [6,7,8,9,10]
change_decode=False
in_decode = "UTF-8" #the decode
out_encode ="GBK" # the encode

'''��ͨSVMģ�͵�����'''
model_main_path = c_p + "model/im_info/10.19_33000/model/"
svm_model_path=model_main_path+"im.model"
dic_path = model_main_path +"dic.key"

'''����ΪLSAģ�͵�����'''
decom_meas= 1
k=20
LSA_path = model_main_path+"lsa_ban_"+str(k)
LSA_model_path = model_main_path+"LSA_ban_"+str(k)+".model"
dust_save_path = model_main_path+"dust.txt"

'''�����ŵ�·��'''
result_indexes = [1,2,3,4,5,6,7,8,9,10] # ��Ҫͬ���һͬ���������
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
    cal_affect(f,X[:,0],X[:,1],"�����ռ�ģ��",first_range)
    cal_affect(f,X[:,0],X[:,2],"LSAģ��",first_range)   
    do_statis(f,X[:,0],X[:,1],"�����ռ�ģ��",second_range)
    do_statis(f,X[:,0],X[:,2],"LSAģ��",second_range)
    f.close()
  
def main():
    print "--------------��ӭʹ��������թ������ϵͳ------------------"
    choice = int(raw_input("1Ϊ������������¼�� 2Ϊ���������0Ϊ�˳�ģ��"))
    while choice!=0:
        if choice==1:
            for file in files:
                filename = filepath+file
                str_time = time.clock()
                result_save_path = os.path.dirname(model_main_path)+"/result"+str(time.strftime('%Y-%m-%d@%H-%M',time.localtime(time.time())))+"_im.result"
                ctm_predict(filename,indexes,dic_path,result_save_path,result_indexes,svm_model_path,str_splitTag=str_splitTag,tc_splitTag=tc_splitTag,delete=delete,change_decode=change_decode,in_decode=in_decode,out_encode=out_encode)
                print "ʱ��Ϊ",str(time.clock()-str_time)
        if choice==2:
            ban_static(result_save_path,statistics_result_save_path)

        choice = int(raw_input("1Ϊ���Υ��Ʒ�� 2Ϊ���������0Ϊ�˳�ģ��"))
main() 
    