#!/usr/bin/python 
# -*-coding:utf-8 -*-
__author__ = '99K'

import pandas as pd
import sklearn
from sklearn.linear_model import LinearRegression

def gate_control(filename):
    data = pd.read_csv(filename)
    prefix = '常' if '常' in filename else '减'
    del data['time']
    data = data[abs(data[prefix+'压温度设定值与观测值差值dif_real']) > 0.3]
    for col in data:
        if '0' in col or 'min' in col or 'rate' in col:
            del data[col]
    
    y1 = data[prefix+'压炉油品流量1'].values
    y2 = data[prefix+'压油品入口温度1'].values
    y3 = data[prefix+'压温度设定值与观测值差值1'].values
    x = data[prefix+'压燃料阀开度1'].values.reshape(-1, 1)
    
    reg1 = LinearRegression()
    reg1.fit(x, y1)
    print(reg1.coef_)
    
    reg2 = LinearRegression()
    reg2.fit(x, y2)
    print(reg2.coef_)

    reg3 = LinearRegression()
    reg3.fit(x, y3)
    print(reg3.coef_)
    
gate_control(r'D:\PyCharmProjects\ZSH\20220126\常12号位置数据前6列.csv')
gate_control(r'D:\PyCharmProjects\ZSH\20220126\减12号位置数据前6列.csv')