# -*- coding: utf-8 -*-
"""
Created on Fri Jan 18 09:27:30 2019

@author: Mr.Reliable
"""

import pandas as pd
import numpy as np
import math
from scipy.linalg import solve
from scipy.stats import t
import os
os.chdir(r'C:\Users\Mr.Reliable\Desktop\MOS')

def add_flag(col):
    #为每一个算法加上一个算法标签
    if 'baseline_1' in col['wav']:
        return 'baseline_1'
    elif 'baseline_2' in col['wav']:
        return 'baseline_2'
    elif 'GT_1' in col['wav']:
        return 'GT_1'
    elif 'GT_2' in col['wav']:
        return 'GT_2'
    elif 'our_model_1' in col['wav']:
        return 'our_model_1'
    else:
        return 'our_model_2'


def MOSinterval(mos_data,algorithm):
    #计算MOS，数据格式：M行N列，M为句子，N为试听人
    #计算均值和方差
    mu = mos_data.mean().mean()
    var_uw = (mos_data.std(axis=1)**2).mean()
    var_su = (mos_data.std(axis=0)**2).mean()
    mos_data_series = []
    for i in mos_data.columns:
        for j in mos_data.index:
            if not math.isnan(mos_data.loc[j,i]):
                mos_data_series.append(mos_data.loc[j,i])
    var_swu = np.array(mos_data_series).std()**2
    
    #求解方程组计算总体方差
    x = np.array([[0,1,1],[1,0,1],[1,1,1]])
    y = np.array([var_uw,var_su,var_swu])
    [var_s,var_w,var_u] = solve(x,y)    #求解三元方程组
    M = min(mos_data.count(axis=0))
    N = min(mos_data.count(axis=1))
    var_mu = var_s/M + var_w/N +var_u/(M*N)
    df = min(M,N)-1   #t分布自由度
    t_interval = t.ppf(0.975,df,loc=0,scale=1)
    interval = t_interval*np.sqrt(var_mu)
    print("{}的MOS 95%置信区间：{} ± {}".format(algorithm,round(mu,3),round(interval,3)))
    

def main():
    fpath = 'MOS数据.xlsx'   
    data = pd.read_excel(fpath)  #读入数据
    wav = data['wav']
    mu_per = data.mean(axis=1).values #计算每一句话的平均得分
    data['mu_per'] = mu_per           
    corr_dataframe = data.corr()   #计算dataframe的相关系数
    corr_mu = corr_dataframe.iloc[:,len(corr_dataframe['mu_per'])-1].tolist() #将相关系数提取出来并转化为list
    corr_mu.insert(0,-1)  #插入-1，用以填补位置
    mos_t = data.T    #数据转置并插入
    mos_t['corr_mu'] = corr_mu

    data_clean = mos_t[mos_t['corr_mu'] > 0.25]      #选取相关系数大于0.25的部分
    data_clean = data_clean.drop(['corr_mu'],axis = 1).T
    data_clean['wav'] = wav                          #重新加入wav变量
    data_clean['flag'] = data_clean.apply(add_flag,axis=1)   #为每一行数据加入标签
    for algorithm in set(data_clean['flag']):
        mos_data = data_clean[data_clean['flag']==algorithm]
        check_null = mos_data.isnull().sum(axis=0).sort_values(ascending=False)/float(len(mos_data))
        mos_data = mos_data.dropna(thresh=len(mos_data)*0.5,axis=1)     #删除缺失值
        mos_data = mos_data.drop(['wav','flag'],axis=1)    #删除除分数之外的列
        MOSinterval(mos_data,algorithm)


if __name__ == '__main__':
    main()    