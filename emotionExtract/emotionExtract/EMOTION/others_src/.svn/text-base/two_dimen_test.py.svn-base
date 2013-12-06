#!/usr/bin/python2.6
# coding: gbk
#Filename: two_dimen_test.py
'''在二维空间中的测试。随机选取若干个点进行测试'''

import random

def random_float(min,max,number):
    x=[]
    for i in range(number):
        x+=[random.uniform(min,max)]
    return x

def random_two_sel_point(f,label,x_min,x_max,y_min,y_max,number):
    x = random_float(x_min,x_max,number)
    y = random_float(y_min,y_max,number)
    for i in range(number):
        f.write(str(label)+"\t")
        f.write("1:"+str(x[i])+" 2:"+str(y[i])+"\n")
        
f = file("D:/test/test.txt",'w')
random_two_sel_point(f,1,1,2,1,2,50)
random_two_sel_point(f,2,2,3,2,3,100)
random_two_sel_point(f,3,3,4,3,4,20)
random_two_sel_point(f,4,4,5,4,5,200)
random_two_sel_point(f,-1,-10,0,-10,0,200)
f.close()

    