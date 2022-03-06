#!/usr/bin/python 
# -*-coding:utf-8 -*-
__author__ = '99K'

# 得到炉膛负压之间的关系

import pandas as pd
from sklearn.linear_model import LinearRegression

def get_coef(filename):
    data = pd.read_csv(filename)
    x = data['炉膛负压G'].values
    y = data['炉膛负压H'].values
    reg = LinearRegression()
    reg.fit(x.reshape(-1, 1), y)
    print(reg.coef_, reg.intercept_)
    
    
get_coef('常压整理完成1215.csv')
get_coef('减压整理完成1215.csv')