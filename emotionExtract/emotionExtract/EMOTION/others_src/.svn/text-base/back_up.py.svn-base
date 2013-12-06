#!/usr/bin/python2.6
# coding: gbk
#Filename: back_up.py
'''里面存放了一些已经做过的测试程序，为了以后的查找或者是其他原因暂时保留起来'''

def two_dim_svm():
    f= file('../train_0825.txt','w')
    p_n = 1000 #正样本1000个
    n_n = 1000 #反样本1000个
    p_s = creat_dot_in_range((2,2),(4,4),p_n)
    n_s = creat_dot_in_range((-1,-1),(1,1),n_n)
    X=array(p_s+n_s)  
    y,x=cons_stand_svm_vec(X,p_n,n_n)
    m=svm_train(y,x)
    
def creat_dot_in_range(A,B,num):
    '''在A，B定义的区间内，生成num个点'''
    dot_set=[]
    for i in range(num):
        x = uniform(A[0],B[0])
        y= uniform(A[1],B[1])
        dot_set.append([x,y])
    #dot_set = array(dot_set)
    return dot_set

def cre_set(A,B,p_n,n_n,filename,append):
    #构造训练集
    p_s = creat_dot_in_range(A,B,p_n+n_n)
    cons_arr_for_cla(array(p_s),p_n,n_n,filename,append)