#!/usr/bin/python 
# -*-coding:utf-8 -*-
__author__ = '99K'

import pandas as pd

d1 = {'0201FIC11813.MV': '燃料阀开度', '0201FIC11813.PV': '燃料流量', '0201TI11701.PV': '油品入口温度',
      '0201TI11704.PV': '油品出口温度', '0201FIQ11709A.IN': '常压炉油品流量', }
d2 = {'0201FIC20201.MV': '燃料阀开度', '0201FIC20201.PV': '燃料流量', '0201TI20101.PV': '油品入口温度',
      '0201TIC20110.PV': '油品出口温度', '0201FIQ20103A.IN': '减压炉油品流量'}


def preprocess(filename, out_name):
    data = pd.read_excel(filename)
    data2save = pd.DataFrame()
    if '常压' in filename:
        d = d1
    else:
        d = d2
    for k in d:
        data2save[d[k]] = data[k]
    data2save['time'] = data['time']
    
    data = data2save
    data2save = pd.DataFrame()
    data2save['time'] = data['time']
    for col in data:
        if col == 'time':
            continue
        print(col)
        t = data[col].values
        data2save[col+'1'] = pd.Series(t[1:])
        data2save[col+'0'] = pd.Series(t[:-1])
        data2save[col+'dif'] = (data2save[col+'1'] - data2save[col+'0']) / data2save[col+'0']
        data2save[col+'dif_real'] = data2save[col+'1'] - data2save[col+'0']
    for col in data:
        if col == 'time' or '阀' in col:
            continue
        data2save = data2save[(data2save[col+'dif'] < 0.1) & (data2save[col+'dif']>-0.1)]
        del data2save[col+'dif']
        data2save[col + '_min'] = data2save[col + '1'] - data2save[col + '1'].min()
    data2save.to_excel(out_name, index=False, encoding='utf-8_sig')

preprocess('D:\PyCharmProjects\ZSH_20211103\data\常压炉1015-1026.xlsx', '常压炉前5列.xlsx')
preprocess('D:\PyCharmProjects\ZSH_20211103\data\减压炉1015-1027.xlsx', '减压炉前5列.xlsx')


    
