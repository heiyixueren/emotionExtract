#!/usr/bin/python2.6
# coding: gbk
#Filename: measure.py
'''里面实现了一些基本的特征权重的计算公式
aij= L(i,j)*G(i)
以及一些距离度量函数：Cosine、Pearson
'''
import math

def L_fun(fun,aij):
    #传入的参数为计算局部权重的函数名称和aij
    return fun(aij)

def Loc_1(aij):
    #第一种计算局部权重的函数
    #不变化，还是返回aij
    return aij
def Loc_2(aij):
    # 第二种计算局部权重的函数
    # log(aij+1)
    aij = float(aij)
    base=2
    return math.log(aij+1)
    

def G_fun(fun,ai):
    #传入的参数为计算全局权重的函数名称和ai
    return fun(ai)
    
def Glo_1(ai):
    #第一种计算全局权重的函数
    #全局权重为1
    return 1.0

def Glo_2(ai):
    #第二种计算全局权重的函数
    #aij 为第i,j个元素值，ai为第i行的值
    # sum(-p*log(p))
    lsum=sum(ai)
    
    n=len(ai)
    ran=range(n)

    base=2
    if lsum==0   : #总和为0，可能存在负值或者是全0
        count=0
        for i in range(len(ai)):
            if ai[i]!=0:
                break
        if i>=len(ai)-1: #说明这一行为全0
            return 1e20
        else:  #说明这一行存在负值
            return 1.0
    else:
        p_i=[float(ai[i])/lsum for i in ran]
    
        #0log0=0 但是在计算的时候不能这样直接计算，需要把p_i[i]=0的先排除掉
        entropy=0.0
        for i in ran:
            if p_i[i]!=0:
                entropy+=p_i[i]*math.log(p_i[i])
    ##    #-sum([p_i[i]*math.log(p_i[i],base) for i in ran])
    #需要考虑到一行只有一个值，而且此值为1的情况，这样计算出来的熵为0
        return -entropy
       # return -sum([p_i[i]*math.log(p_i[i],base) for i in ran if p_i[i]!=0])

def Glo_3(ai):
    #第二种计算全局权重的函数
    #  (1-sum(-p*log(p)))/log(n)
    lsum=sum(ai)
    
    n=len(ai)
    ran=range(n)

    base=2

    if lsum==0   : #总和为0，可能存在负值或者是全0
        count=0
        for i in range(len(ai)):
            if ai[i]!=0:
                break
        if i>=len(ai)-1: #说明这一行为全0
            return 1e20
        else:  #说明这一行存在负值
            return 1.0
    else:
        p_i=[float(ai[i])/lsum for i in ran]

    #0log0=0 但是在计算的时候不能这样直接计算，需要把p_i[i]=0的先排除掉
    entropy=0.0
    for i in ran:
        if p_i[i]!=0:
            entropy+=p_i[i]*math.log(p_i[i])
    entropy = -entropy

    return (1+entropy)/math.log(n)

def Glo_4(ai):
    #第4种计算全局权重的函数 TF*IDF
    #  log(N/n) N represents all documents number,n represents number of document containing term

    
    N=len(ai)
    n=0.0
    base=2
    ran=range(N)
    for i in ran:
        if ai[i]!=0:
            n+=1
    if n==0:
        n+=0.01  # 为了避免n=0，加一个因子进行权衡
    return math.log(float(N)/n)
    

def Glo_5(ai):
    #第二种计算全局权重的函数
    #  (1-sum(-p*log(p)))/log(n)
    lsum=sum(ai)
    
    n=len(ai)
    ran=range(n)

    base=2

    if lsum==0   : #总和为0，可能存在负值或者是全0
        count=0
        for i in range(len(ai)):
            if ai[i]!=0:
                break
        if i>=len(ai)-1: #说明这一行为全0
            return 1e20
        else:  #说明这一行存在负值
            return 1.0
    else:
        p_i=[float(ai[i])/lsum for i in ran]

    #0log0=0 但是在计算的时候不能这样直接计算，需要把p_i[i]=0的先排除掉
    entropy=0.0
    for i in ran:
        if p_i[i]!=0:
            entropy+=p_i[i]*math.log(p_i[i])
    entropy = -entropy

    return 1+entropy/math.log(n)

def pearson(x,y):
    n=len(x)
    vals=range(n)

    #Simple sum
    sumx=sum([float(x[i]) for i in vals])
    sumy=sum([float(y[i]) for i in vals])

    #Sum of square
    sumxSq =sum([x[i]**2.0 for i in vals])
    sumySq =sum([y[i]**2.0 for i in vals])

    #sum up the dot product
    psum = sum([x[i]*y[i] for i in vals])

    #calulate the Pearson score
    num=psum-(sumx*sumy/n)
    den=((sumxSq-pow(sumx,2)/n)*(sumySq-pow(sumy,2)/n))**0.5

    if den==0:return 0

    r=num/den
    return r


def cosine(x,y):
    n=len(x)
    ran=range(n)
    #cacalte the product betwen x and y
    psum=sum([x[i]*y[i] for i in ran])

    #caculate size of x,y respectly
    xs=sum([x[i]**2.0 for i in ran])**0.5
    ys=sum([y[i]**2.0 for i in ran])**0.5
  #  print  psum,xs*ys
    if psum==0 or xs==0 or ys==0:
        return 0
    return psum/(xs*ys)


def main():
    x=[2,3,4]
    y=[3,2,5]

    print "x,y pearson distance:"
    print pearson(x,y)

    print "x,y cosine distance"
    print cosine(x,y)