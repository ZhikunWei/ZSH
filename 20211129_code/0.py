#!/usr/bin/python 
# -*-coding:utf-8 -*-
__author__ = '99K'

import pandas as pd
import numpy as np


changya_coef = pd.read_excel(r'常压热值2阶组合系数.xlsx')
jianya_coef = pd.read_excel(r'减压热值2阶组合系数.xlsx')
changya_fea2coef = {}
for i in range(len(changya_coef['特征组合'])):
    changya_fea2coef[changya_coef['特征组合'][i]] = changya_coef['系数'][i]
jianya_fea2coef = {}
for i in range(len(jianya_coef['特征组合'])):
    jianya_fea2coef[jianya_coef['特征组合'][i]] = jianya_coef['系数'][i]
    
changya = pd.read_csv('D:\PyCharmProjects\ZSH\data\常压炉300秒加油品210418（剔除无效数据）.csv')
changya['油品温度差'] = changya['油品出口温度'] - changya['油品入口温度']
changya['油品比热容'] = changya['燃料气压力'] - changya['燃料气压力']
for x in changya_fea2coef:
    name = x.split()
    print(name)
    if len(name) > 1:
        changya['油品比热容'] += changya[name[0]] * changya[name[1]] * changya_fea2coef[x]
    else:
        if '^2' in name[0]:
            changya['油品比热容'] += changya[name[0][:-2]] * changya[name[0][:-2]] * changya_fea2coef[x]
        elif name[0] == '1':
            changya['油品比热容'] += changya_fea2coef[x]
        else:
            changya['油品比热容'] += changya[name[0]] * changya_fea2coef[x]
    
changya['燃料气热值'] = changya['油品比热容'] * (changya['油品出口温度'] - changya['油品入口温度']) * changya['常压炉油品流量'] / changya['燃料流量']

jianya = pd.read_csv('D:\PyCharmProjects\ZSH\data\减压炉300秒加油品210418（剔除无效数据）.csv')
jianya['油品温度差'] = jianya['油品出口温度'] - jianya['油品入口温度']
jianya['油品比热容'] = jianya['燃料气压力'] - jianya['燃料气压力']
for x in jianya_fea2coef:
    name = x.split()
    print(name)
    if len(name) > 1:
        jianya['油品比热容'] += jianya[name[0]] * jianya[name[1]] * jianya_fea2coef[x]
    else:
        if '^2' in name[0]:
            jianya['油品比热容'] += jianya[name[0][:-2]] * jianya[name[0][:-2]] * jianya_fea2coef[x]
        elif name[0] == '1':
            jianya['油品比热容'] += jianya_fea2coef[x]
        else:
            jianya['油品比热容'] += jianya[name[0]] * jianya_fea2coef[x]
    
jianya['燃料气热值'] = jianya['油品比热容'] * (jianya['油品出口温度'] - jianya['油品入口温度']) * jianya['常压炉油品流量'] / jianya['燃料流量']


changya['常压风门蝶阀开度之和'] = changya['风门蝶阀01'] + changya['风门蝶阀02'] + changya['风门蝶阀03'] + changya['风门蝶阀04']
changya['烟道挡板开度之和'] = changya['烟道挡板05'] + changya['烟道挡板06']
changya['烟道氧含量均值'] = (changya['烟道氧含量01'] + changya['烟道氧含量02'] + changya['烟道氧含量03'] + changya['烟道氧含量04'])/4
changya['烟道氧含量最小值'] = changya[['烟道氧含量01', '烟道氧含量02', '烟道氧含量03', '烟道氧含量04']].min(axis=1)

jianya['减压风门蝶阀开度之和'] = jianya['风门蝶阀01'] + jianya['风门蝶阀02']
jianya['烟道挡板开度之和'] = jianya['烟道挡板03']
jianya['烟道氧含量均值'] = (jianya['烟道氧含量01'] + jianya['烟道氧含量02']) / 2
jianya['烟道氧含量最小值'] = jianya[['烟道氧含量01', '烟道氧含量02']].min(axis=1)

changya2save = changya[['时间', '燃料流量', '鼓风机变频', '常压风门蝶阀开度之和', '烟道挡板开度之和', '燃料气热值', '烟道氧含量均值', '烟道氧含量最小值']]
jianya2save = jianya[['时间', '燃料流量', '鼓风机变频', '减压风门蝶阀开度之和', '烟道挡板开度之和', '燃料气热值', '烟道氧含量均值', '烟道氧含量最小值']]

changya2save = pd.merge(changya2save, jianya[['时间', '减压风门蝶阀开度之和']], on='时间')
changya2save.to_csv('常压整理完成1204.csv', index=False, encoding='utf-8_sig')
jianya2save = pd.merge(jianya2save, changya[['时间', '常压风门蝶阀开度之和']], on='时间')
jianya2save.to_csv('减压整理完成1204.csv', index=False, encoding='utf-8_sig')