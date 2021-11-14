#!/usr/bin/python 
# -*-coding:utf-8 -*-
__author__ = '99K'

import pandas as pd
import numpy as np

d1 = {'0201FIC11813.MV': '燃料阀开度', '0201FIC11813.PV': '燃料流量',
      '0201TI11704.PV': '油品出口温度'}
d2 = {'0201FIC20201.MV': '燃料阀开度', '0201FIC20201.PV': '燃料流量',
      '0201TIC20110.PV': '油品出口温度'}


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
    # data2save['time'] = data['time']
    for col in data:
        if col == 'time':
            continue
        print(col)
        t = data[col].values
        avg_m10_m6 = []
        avg_m5_0 = []
        dif_1_0 = []
        dif_3_0 = []
        dif_5_0 = []
        t0 = []
        for i in range(10, len(t)-5):
            avg_m10_m6.append(np.mean(t[i-10:i-5]))
            avg_m5_0.append(np.mean(t[i-5:i+1]))
            dif_1_0.append(t[i+1] - t[i])
            dif_3_0.append(t[i+3] - t[i])
            dif_5_0.append(t[i+5] - t[i])
            t0.append(t[i])
        if col == '油品出口温度':
            data2save[col + 'avg_-10_-6'] = pd.Series(avg_m10_m6)
            data2save[col + 'avg_-5_0'] = pd.Series(avg_m5_0)
            data2save[col + 'avg_dif'] = data2save[col + 'avg_-5_0'] - data2save[col + 'avg_-10_-6']
        else:
            data2save[col + 'dif-3-0'] = pd.Series(dif_3_0)
            data2save[col + 'dif-5-0'] = pd.Series(dif_5_0)
        data2save[col + 'dif-1-0'] = pd.Series(dif_1_0)
        data2save[col + 't0'] = pd.Series(t0)
        data2save[col + 'dif_rate'] = data2save[col + 'dif-1-0'] / data2save[col + 't0']
        
    for col in data:
        if col == 'time' or '阀' in col:
            continue
        data2save = data2save[abs(data2save[col + 'dif_rate']) < 0.1]
        del data2save[col + 'dif_rate']
    # data2save = data2save[abs(data2save['油品出口温度avg_dif']) > 0.1]
    
    data2save.to_excel(out_name, index=False, encoding='utf-8_sig')
    print(out_name)


def data_corr(filename, outname, thre):
    data = pd.read_excel(filename)
    data = data[abs(data['油品出口温度avg_dif']) >= thre]
    del data['燃料阀开度dif_rate']
    t = data.corr()
    t.to_excel(outname % thre, encoding='utf-8_sig')
    print(outname % thre)
    

# preprocess('D:\PyCharmProjects\ZSH\data\常压炉1015-1026.xlsx', '常压炉前3列.xlsx')
# preprocess('D:\PyCharmProjects\ZSH\data\减压炉1015-1027.xlsx', '减压炉前3列.xlsx')

data_corr('常压炉前3列.xlsx', 'result2/常压炉累积量与燃料相关性-阈值%f.xlsx', 0.2)
data_corr('常压炉前3列.xlsx', 'result2/常压炉累积量与燃料相关性-阈值%f.xlsx', 0.3)
data_corr('常压炉前3列.xlsx', 'result2/常压炉累积量与燃料相关性-阈值%f.xlsx', 0.4)
data_corr('减压炉前3列.xlsx', 'result2/减压炉累积量与燃料相关性-阈值%f.xlsx', 0.2)
data_corr('减压炉前3列.xlsx', 'result2/减压炉累积量与燃料相关性-阈值%f.xlsx', 0.3)
data_corr('减压炉前3列.xlsx', 'result2/减压炉累积量与燃料相关性-阈值%f.xlsx', 0.4)
