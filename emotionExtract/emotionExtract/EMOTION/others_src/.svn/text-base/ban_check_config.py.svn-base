#!/usr/bin/python2.6
# coding: gbk
#Filename: ban_check_config.py
import os.path
import time
c_p = os.path.dirname(os.getcwd())+"/"

filename=c_p+"model/model_0830_ban/adult_all_data.txt" #adult_all_data.txt
tc_splitTag="\t"
str_splitTag =" "

k=20

model_main_path = c_p + "model/model_0830_ban/LSA_K/k="+str(k)+"/"

svm_model_path=model_main_path+"ban.model"
LSA_path = model_main_path+"lsa_ban_"+str(k)
LSA_model_path = model_main_path+"LSA_ban_"+str(k)+".model"
dust_save_path = model_main_path+"dust.txt"

decom_meas= 1
dic_path  = "Dictionary/ban/"
dic_name = "Dic_ban"
key_path = c_p+dic_path+dic_name+".key"
glo_aff_path = c_p+dic_path+dic_name+".glo"

line_length = 2
indexes= [1]
delete = False

result_save_path = model_main_path+str(time.strftime('%Y-%m-%d',time.localtime(time.time())))+"_ban.result"
statistics_result_save_path = model_main_path+str(time.strftime('%Y-%m-%d',time.localtime(time.time())))+"_ban.statistics"