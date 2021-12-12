#!/usr/bin/python 
# -*-coding:utf-8 -*-
__author__ = '99K'

import pandas as pd
import matplotlib.pyplot as plt

changya = pd.read_csv('常压整理完成1207.csv')
jianya = pd.read_csv('减压整理完成1207.csv')

t = pd.DataFrame()
t['鼓风机变频'] = changya['鼓风机变频']
t['常压炉烟道挡板05'] = changya['烟道挡板05']
t['常压炉烟道挡板06'] = changya['烟道挡板06']
t['减压炉烟道挡板03'] = jianya['烟道挡板03']
x = t.describe()
x.to_csv('可控制变量数据特征统计.csv', encoding='utf-8_sig')
t.hist(bins=1000)
plt.rcParams['font.sans-serif'] = ['SimHei']
plt.show()
print(x)
