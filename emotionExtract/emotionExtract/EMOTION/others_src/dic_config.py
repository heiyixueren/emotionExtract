#!/usr/bin/python2.6
# coding: gbk
#Filename: dic_config.py
import os.path

c_p = os.path.dirname(os.getcwd())+"/"
'''-------------������թ��Ĵʵ乹��------------------------------'''
filepath = "D:/��֪��/����/������թ����/"
files = ["im_info_1.txt","im_info_2.txt"]
#filename =  c_p+ "model/model_0830_ban/adult_for_train.txt" #adult_for_train

dic_path  ="Dictionary/im_info/"
dic_name = "im_info_all"

key_save_path = c_p+dic_path+dic_name+".key"
dic_save_path = c_p+dic_path+dic_name+".dic"
glo_aff_save_path = c_p+dic_path+dic_name+".glo"

stopwords_filename = c_p+"Dictionary/im_info/stopwords.txt"
dust_save_path = c_p+ "model/model_0830_ban/dust.txt"
dic_load_path = dic_save_path
tc_splitTag="\t"
str_splitTag ="^"
line_length = 2
indexes= [6]

min = 0
max = 500000


'''--------------�������Ӽ�شʵ乹��-,�ܹ���55898������
filename =  c_p+ "data/20110820_all_data/post_all_data.txt"

dic_path  = "Dictionary/"
dic_name = "Dic_ban_1"

key_save_path = c_p+dic_path+dic_name+".key"
dic_save_path = c_p+dic_path+dic_name+".dic"
glo_aff_save_path = c_p+dic_path+dic_name+".glo"
stopwords_filename = c_p+"Dictionary/stopwords.txt"
dust_save_path = c_p+ "data/20110820_all_data/dust.txt"
dic_load_path = dic_save_path
tc_splitTag="\t"
str_splitTag ="^"
line_length = 5
indexes= [1,2]

min = 20
max = 50000
-------------------'''
