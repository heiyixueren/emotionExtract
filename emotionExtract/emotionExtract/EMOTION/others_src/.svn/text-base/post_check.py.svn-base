#!/usr/bin/python2.6
# coding: gbk
#Filename: post_check_new.py

from ctm_predict_model import cal_sc_optim,ctm_predict_multi
from svmutil import svm_predict,svm_load_model
from fileutil import read_list,read_dic
from result_anlysis import *
from numpy import *
from lsa import *
import time
import os.path

c_p = os.path.dirname(os.getcwd())+"/"

'''输入文件的配置'''
#filename = "D:/张知临/数据/社区帖子数据/0906/t10w_gbk_100000"
#filename = "D:/张知临/源代码/python_ctm/data/20110820_all_data/post_all_data.txt"
#filename = "D:/张知临/源代码/python_ctm/model/model_0829_dic1/测定阈值用&比较效果用.data"
#filename=c_p+"model/ctm/weijin/weijin.test"#ctm_post_5230.data
#filename = "G:/x项目/Taobao/数据/社区帖子数据/0906/t10w_gbk_57000"
#filename="G:/x项目/Taobao/源代码/python_ctm/model/model_0829_dic1/train_set.txt"
#filename = c_p+"data/t10w"
#filepath="G:/x项目/Taobao/数据/旺旺欺诈聊天/"
filepath=c_p+"model/ctm/weijin_all_kinds/"
files = ["t10w"]
tc_splitTag="\t"
str_splitTag ="^"
delete = False
indexes_lists= [[1],[1,2]]
change_decode=False
in_decode = "UTF-8" #the decode
out_encode ="GBK" # the encode

'''普通SVM模型的配置'''
model_main_path = c_p + "model/ctm/weijin_all_kinds/model/"
model_path_list=[model_main_path+"title.model",model_main_path+"title_content.model"]
dic_path_list = [model_main_path +"title.key",model_main_path +"title_content.key"]
result_indexes =[0,1,2]

result_save_path = os.path.dirname(os.path.dirname(model_main_path))+"/result/"+str(time.strftime('%Y-%m-%d@%H-%M',time.localtime(time.time())))+"_im.result"
statistics_result_save_path =model_main_path+str(time.strftime('%Y-%m-%d',time.localtime(time.time())))+"_ctm.statistics"
best_param_result_save_path= model_main_path+str(time.strftime('%Y-%m-%d',time.localtime(time.time())))+"_ctm.best_param"


'''社区帖子监测的程序'''

'''
 input file format: label(or ID) title content    #if first is ID ,then no result analysis can be done
 #output file format :label(or ID) title_score content_score title+content_score title content
'''
''''''

def post_result_analysis(result_path,statistics_result_save_path,indexes,true_index=2,title_index=0,title_content_index=1):
    result_path ="D:/张知临/源代码/python_ctm/model/ctm/weijin/result/2011-10-20@14-25_im.result"
    statistics_result_save_path = "../result"  
    indexes=[0,1,2]
    X=read_result(result_path,indexes)
    f= file(statistics_result_save_path,'w')
    f.write( "\n标题\n")
    rate= cal_f(X[:,true_index].tolist(),X[:,title_index].tolist())
    f.write( "\n利用标题各个类别的F值、召回率、准确率\n类别\tF值\t召回率\t准确率\n")
    save_result(f,rate)
    
    rate = cal_f_binary(X[:,true_index].tolist(),X[:,title_index].tolist())
    f.write( "\n利用标题违规类别的F值、召回率、准确率\n类别\tF值\t召回率\t准确率\n")
    save_result(f,rate)
    
    rate,micro,macro = cal_multi_rate(X[:,true_index].tolist(),X[:,title_index].tolist())
    f.write( "\n利用标题各个类别的分类准确率。其实就是召回率\n类别\t准确率\n")
    save_result(f,rate)
    f.write("\n微观分类准确率=%g,宏观分类准确率=%g\n"%(micro,macro))

    f.write( "\n标题+内容\n")
    rate= cal_f(X[:,true_index].tolist(),X[:,title_content_index].tolist())
    f.write( "\n利用标题+内容各个类别的F值、召回率、准确率\n类别\tF值\t召回率\t准确率\n")
    save_result(f,rate)
    
    rate = cal_f_binary(X[:,true_index].tolist(),X[:,title_content_index].tolist())
    f.write( "\n利用标题+内容违规类别的F值、召回率、准确率\n类别\tF值\t召回率\t准确率\n")
    save_result(f,rate)
    
    rate,micro,macro = cal_multi_rate(X[:,true_index].tolist(),X[:,title_content_index].tolist())
    f.write( "\n利用标题+内容各个类别的分类准确率。其实就是召回率\n类别\t准确率\n")
    save_result(f,rate)
    f.write("\n微观分类准确率=%g,宏观分类准确率=%g\n"%(micro,macro))
    

    f.close()


print "--------------欢迎使用社区帖子监控系统------------------"
choice = int(raw_input("1为监控社区帖子； 2对结果进行分析；3为评估结果；4为选择最优的参数；5为对未知样本进行评估；0为退出模型"))
while choice!=0:
    if choice==1:
        for file in files:
            strat_time = time.clock()
            filename = filepath+file
            str_time = time.clock()
            result_save_main_path = os.path.dirname(os.path.dirname(model_main_path))+"/result/"
            if os.path.exists(result_save_main_path) is False:
                os.mkdir(result_save_main_path)
            result_save_path = os.path.dirname(os.path.dirname(model_main_path))+"/result/"+str(time.strftime('%Y-%m-%d@%H-%M',time.localtime(time.time())))+"_im.result"
            ctm_predict_multi(filename,indexes_lists,dic_path_list,result_save_path,result_indexes,model_path_list,str_splitTag,tc_splitTag,delete=False,change_decode=False,in_decode="UTF-8",out_encode="GBK")
            print "花费的时间为："+str(time.clock()-strat_time)
    if choice==2:
        post_result_analysis(result_save_path,statistics_result_save_path,indexes=[0,1,2],true_index=2,title_index=0,title_content_index=1)
    if choice==3:
        statis_with_result(result_save_path,statistics_result_save_path)
    if choice==4:
        grid_search(result_save_path,best_param_result_save_path)
    if choice==5:
        big_data_statis(result_save_path,statistics_result_save_path)
    choice = int(raw_input("1为监控社区帖子； 2为评估结果；3为选择最优的参数；4为对大规模样本进行评估；0为退出模型"))

    