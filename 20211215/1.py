#!/usr/bin/python 
# -*-coding:utf-8 -*-
__author__ = '99K'

import pandas as pd
import matplotlib.pyplot as plt

changya = pd.read_csv('常压整理完成1215.csv')
jianya = pd.read_csv('减压整理完成1215.csv')
changya_o2_descr =changya[['炉膛负压G', '炉膛负压H',]].describe()
changya_o2_descr.to_csv('常压炉炉膛负压数据分布情况.csv', encoding='utf-8_sig')
changya_corr = changya[['炉膛负压G', '炉膛负压H']].corr()
changya_corr.to_csv('常压炉炉膛负压corr.csv', encoding='utf-8_sig')

changya[['炉膛负压G', '炉膛负压H',]].hist(bins=1000)
plt.rcParams['font.sans-serif'] = ['SimHei']
plt.rcParams['axes.unicode_minus'] = False
plt.show()
print(changya_o2_descr)
print(changya_corr)

jianya_o2 = jianya[['炉膛负压G', '炉膛负压H',]].describe()
jianya_o2.to_csv('减压炉炉膛负压数据分布情况.csv', encoding='utf-8_sig')
jianya_corr = jianya[['炉膛负压G', '炉膛负压H',]].corr()
jianya_corr.to_csv('减压炉炉膛负压corr.csv', encoding='utf-8_sig')
jianya[['炉膛负压G', '炉膛负压H',]].hist(bins=1000)
plt.rcParams['font.sans-serif'] = ['SimHei']
plt.rcParams['axes.unicode_minus'] = False
plt.show()
print(jianya_o2)
print(jianya_corr)
