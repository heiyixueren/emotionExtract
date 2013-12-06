#!/usr/bin/python2.6
# coding: gbk
#Filename: post_train_wrapper.py

''' A wrapper that encaping the process of training the ctm model
title.train title_content.train title.model title_content.model
step 1 : construct the svm_format for libsvm training
step 2: using the proper param to train the model

'''
#4Ϊ����LSAģ�ͣ�5Ϊѵ��LSA���ɵ�ģ��;6Ϊ��ԭģ��������ԭ�����е�������7Ϊ��LSAģ��������ԭ������������
from ctm_train_model import *
import os.path
c_p = os.path.dirname(os.getcwd())+"/"

save_main_path = c_p+"model/ctm/"
dic_main_path = c_p+"Dictionary/ctm/"
# step 1 :����SVMѵ��������
#filename,indexs,dic_path,glo_aff_path,sample_save_path,delete
filename  = c_p+"model/ctm_credit/credit.train"
#D:\��֪��\Դ����\python_ctm\model\model_0829_dic1
#----------------------title------------------------

category = "credit/"
title_indexs = [1]
title_dic_path =dic_main_path+category+"title.key"
#title_glo_aff_path  = dic_main_path+"Dic1_title_1.glo"
title_M=895 # the size of dictionary
title_sample_save_path = save_main_path+category+"title.train"

#----------------------title+content-----------------------
title_content_indexs = [1,2]
title_content_dic_path =dic_main_path+category+"title_content.key"
#title_content_glo_aff_path  = dic_main_path+"Dic1_title_content_1.glo"
title_content_M=3807 # the size of dictionary
title_content_sample_save_path = save_main_path+category+"title_content.train"

delete =True
tc_splitTag="\t"
str_splitTag ="^"

# step 2 :ѵ��ģ��
#sample_save_path,param,model_save_path
title_svm_model_save_path = save_main_path+category+"title.model"
title_svm_param='-c 2.0 -g 0.5' 

title_content_svm_model_save_path = save_main_path+category+"title_content.model"
title_content_svm_param='-c 8.0 -g 0.5' 


#step 3: ��ģ��������ԭ�����е�����
extra_filename = save_main_path +"����ѵ������0915.txt"




print "--------------��ӭʹ��CTMģ��ѵ��ϵͳ------------------"
choice = int(raw_input("1Ϊ����SVMѵ���������� 2Ϊѵ��ģ�ͣ�3Ϊ��ģ��������ԭ�����е�������0Ϊ�˳�ģ��"))
while choice!=0:
    if choice==1:
        cons_train_sample_for_cla(filename,title_indexs,title_dic_path,title_sample_save_path,delete,str_splitTag)
        cons_train_sample_for_cla(filename,title_content_indexs,title_content_dic_path,title_content_sample_save_path,delete,str_splitTag)
    if choice==2:
        title_m=ctm_train_model(title_sample_save_path,title_svm_param,title_svm_model_save_path) 
        title_content_m=ctm_train_model(title_content_sample_save_path,title_content_svm_param,title_content_svm_model_save_path)
    if choice==3:
        add_sample_to_model(extra_filename,title_indexs,title_dic_path,title_sample_save_path,delete,str_splitTag)
        add_sample_to_model(extra_filename,title_content_indexs,title_content_dic_path,title_content_sample_save_path,delete,str_splitTag)
    choice = int(raw_input("1Ϊ����SVMѵ���������� 2Ϊѵ��ģ�ͣ�3Ϊ��ģ��������ԭ�����е�������0Ϊ�˳�ģ��"))
    
