#!/usr/bin/python 
# -*-coding:utf-8 -*-
__author__ = '99K'

import pandas as pd
import numpy as np
import sklearn
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import PolynomialFeatures

x1_names = ['燃料流量', '鼓风机变频', '常压风门蝶阀开度之和', '减压风门蝶阀开度之和', '烟道挡板开度之和', '燃料气热值']
def evaluate(x, y):
    reg = LinearRegression()
    reg.fit(x, y)
    mse = sklearn.metrics.mean_squared_error(y, reg.predict(x))
    
    poly = PolynomialFeatures(2)
    x2 = poly.fit_transform(x)
    reg = LinearRegression()
    reg.fit(x2, y)
    mse2 = sklearn.metrics.mean_squared_error(y, reg.predict(x2))
    x_names = poly.get_feature_names_out(x1_names[:x.shape[1]])
    weights = reg.coef_
    bias = reg.intercept_
    data2save = pd.DataFrame()
    data2save['特征组合'] = pd.Series(x_names)
    data2save['系数'] = pd.Series([bias] + weights.tolist())
    data2save.to_excel('减压炉特征组合及系数.xlsx', index=False, encoding='utf-8_sig')
    return mse, mse2


def air_supply(filename):
    data = pd.read_csv(filename)
    x1_names = ['燃料流量', '鼓风机变频', '常压风门蝶阀开度之和', '减压风门蝶阀开度之和', '烟道挡板开度之和', '燃料气热值']
    x1 = data[x1_names].values
    x2 = data[x1_names[:-1]].values
    y1 = data['烟道氧含量均值'].values
    y2 = data['烟道氧含量最小值'].values
    mse1, mse2 = evaluate(x1, y1)
    # mse3, mse4 = evaluate(x1, y2)
    # mse5, mse6 = evaluate(x2, y1)
    # mse7, mse8 = evaluate(x2, y2)
    # print(mse1, mse3)
    # print(mse2, mse4)
    # print()
    # print(mse5, mse7)
    # print(mse6, mse8)
    # print()
    
    
# air_supply('常压整理完成1204.csv')
air_supply('减压整理完成1204.csv')
