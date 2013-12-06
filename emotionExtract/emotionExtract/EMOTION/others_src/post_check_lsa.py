#!/usr/bin/python2.6
# coding: gbk
#Filename: ban_check.py

from ctm_train_model import cons_vec_for_cla,cons_svm_problem
from svmutil import svm_predict,svm_load_model
from fileutil import read_list,read_dic
from result_anlysis import *
from numpy import *
from lsa import *
import time
import os.path
c_p = os.path.dirname(os.getcwd())+"/"

#filename=c_p+"model/model_0829_dic1/post.test" #测定阈值用&比较效果用.data
#filename = "D:/张知临/源代码/python_ctm/Dictionary/ctm/Dic1_title_content.key"
filename = "D:/张知临/数据/社区帖子数据/0906/t10w_gbk_57000"
tc_splitTag="\t"
str_splitTag ="^"

k=500

model_main_path = c_p + "model/model_0829_dic1/0915_lsa/k="+str(k)+"/"

svm_model_path=model_main_path+"title_content_1.model"
LSA_path = model_main_path+"lsa_title_content_"+str(k)
LSA_model_path = model_main_path+"LSA_title_content"+str(k)+".model"
dust_save_path = model_main_path+"dust.txt"

decom_meas= 1
dic_path  = "Dictionary/ctm/"
dic_name = "Dic_all"
key_path = c_p+dic_path+dic_name+".key"
glo_aff_path = c_p+dic_path+dic_name+"_1.glo"

line_length = 5
indexes= [1,2]
delete = False

result_save_path = model_main_path+str(time.strftime('%Y-%m-%d',time.localtime(time.time())))+"_ban.result"
statistics_result_save_path = model_main_path+str(time.strftime('%Y-%m-%d',time.localtime(time.time())))+"_ban.statistics"

'''禁售品监测的程序
# input file format:label content
'''

def cons_train_sample_for_cla(filename,indexes,dic_path,glo_aff_path,result_save_path,model_path,LSA_path,LSA_model_path,decom_meas,delete):
    dic_list = read_dic(dic_path,dtype=str)
    glo_aff_list = read_list(glo_aff_path)
    f= file(filename,'r')
    fs = file(result_save_path,'w')
    fd = file(dust_save_path,'w')
    m= svm_load_model(model_path)
    lsa_m = svm_load_model(LSA_model_path)
    U = load_lsa_model(LSA_path,"U")
    for line in f.readlines():
        text = line.strip().split(tc_splitTag)
        if len(text)!=line_length:
            fd.write(line)
            continue
        text_temp=""
        for i in indexes:
            text_temp+=str_splitTag+text[i]  
        vec = cons_vec_for_cla(text_temp.strip().split(str_splitTag),dic_list,glo_aff_list)
        y,x=cons_svm_problem(text[0],vec)
        p_lab,p_acc,p_sc=svm_predict(y,x,m)
 
        if  decom_meas==1:
            weight = cal_weight(p_sc[0][0])
            #vec = [value*weight for value in vec ] 
            vec = [0]*len(vec)
            for key in x[0].keys():
               vec[int(key)-1]= weight*float(x[0][key])    
            vec = pre_doc_svds(vec,U)
            y,x=cons_svm_problem(text[0],vec)
            lsa_lab,lsa_acc,lsa_sc = svm_predict(y,x,lsa_m)
            fs.write(text[0]+"\t"+str(p_sc[0][0])+"\t"+str(lsa_sc[0][0])+"\t"+text[1]+"\t"+text[2]+"\n")
        else :
            fs.write(text[0]+"\t"+str(p_sc[0][0])+"\t"+text[1]+"\t"+text[2]+"\n")
    f.close()
    fs.close()

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
    print "--------------欢迎使用社区帖子监控LSA系统------------------"
    choice = int(raw_input("1为监控社区帖子； 2为评估结果；0为退出模型"))
    while choice!=0:
        if choice==1:
            #cons_train_sample_for_cla(filename,indexes,key_path,glo_aff_path,result_save_path,svm_model_path,delete)
            cons_train_sample_for_cla(filename,indexes,key_path,glo_aff_path,result_save_path,svm_model_path,LSA_path,LSA_model_path,decom_meas,delete)
        if choice==2:
            ban_static(result_save_path,statistics_result_save_path)

        choice = int(raw_input("1为监控社区帖子； 2为评估结果；0为退出模型"))
main() 
    
