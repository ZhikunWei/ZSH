#!/usr/bin/python 
# -*-coding:utf-8 -*-
__author__ = '99K'

import pandas as pd
import matplotlib.pyplot as plt

changya = pd.read_csv('常压整理完成1207.csv')
jianya = pd.read_csv('减压整理完成1207.csv')
changya_o2_descr =changya[['烟道氧含量均值', '烟道氧含量最小值', '烟道氧含量01', '烟道氧含量02', '烟道氧含量03', '烟道氧含量04']].describe()
changya_o2_descr.to_csv('常压炉烟道氧含量数据分布情况.csv', encoding='utf-8_sig')
changya_corr = changya[['烟道氧含量均值', '烟道氧含量最小值', '烟道氧含量01', '烟道氧含量02', '烟道氧含量03', '烟道氧含量04']].corr()
changya_corr.to_csv('常压炉烟道氧含量corr.csv', encoding='utf-8_sig')

changya[['烟道氧含量均值', '烟道氧含量最小值', '烟道氧含量01', '烟道氧含量02', '烟道氧含量03', '烟道氧含量04']].hist(bins=1000)
plt.rcParams['font.sans-serif'] = ['SimHei']
plt.show()
print(changya_o2_descr)
print(changya_corr)

jianya_o2 = jianya[['烟道氧含量均值', '烟道氧含量最小值', '烟道氧含量01', '烟道氧含量02']].describe()
jianya_o2.to_csv('减压炉烟道氧含量数据分布情况.csv', encoding='utf-8_sig')
jianya_corr = jianya[['烟道氧含量均值', '烟道氧含量最小值', '烟道氧含量01', '烟道氧含量02']].corr()
jianya_corr.to_csv('减压炉烟道氧含量corr.csv', encoding='utf-8_sig')
jianya[['烟道氧含量均值', '烟道氧含量最小值', '烟道氧含量01', '烟道氧含量02']].hist(bins=1000)
plt.rcParams['font.sans-serif'] = ['SimHei']
plt.show()
print(jianya_o2)
print(jianya_corr)
