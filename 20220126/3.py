#!/usr/bin/python 
# -*-coding:utf-8 -*-
__author__ = '99K'

import pandas as pd
import numpy as np

d1 = {
    '0201TIC11704.PV': '油品出口温度',
    '0201TIC11704.SV': '油品出口温度设定值',
    '0201FIC11813.MV': '燃料阀开度',
    '0201FIC11813.PV': '燃料流量',
}
d2 = {
    '0201TIC20110.PV': '油品出口温度',
    '0201TIC20110.SV': '油品出口温度设定值',
    '0201FIC20201.MV': '燃料阀开度',
    '0201FIC20201.PV': '燃料流量'
}


def preprocess(filename, leibie, out_name):
    data = pd.read_csv(filename,  low_memory=False)
    data2save = pd.DataFrame()
    if leibie == '常':
        d = d1
    else:
        d = d2
    for k in d:
        data2save[d[k]] = data[k]
    data2save['time'] = data['time']
    data2save['出口温度设定值与观测值之差'] = data2save['油品出口温度设定值'] - data2save['油品出口温度']
    
    data = data2save
    data2save = pd.DataFrame()
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
        for i in range(10, len(t) - 5):
            avg_m10_m6.append(np.mean(t[i - 10:i - 5]))
            avg_m5_0.append(np.mean(t[i - 5:i + 1]))
            dif_1_0.append(t[i + 1] - t[i])
            dif_3_0.append(t[i + 3] - t[i])
            dif_5_0.append(t[i + 5] - t[i])
            t0.append(t[i])
        if col in ['油品出口温度', '油品出口温度设定值', '出口温度设定值与观测值之差']:
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
    
    data2save.to_csv(out_name, index=False, encoding='utf-8_sig')
    print(out_name)


def data_corr(filename, outname, item, thre):
    data = pd.read_csv(filename)
    data = data[abs(data[item]) >= thre]
    print(filename, thre, data.shape)
    for col in data:
        if 'rate' in col:
            del data[col]
    t = data.corr()
    t = t[['燃料阀开度dif-3-0', '燃料阀开度dif-5-0', '燃料阀开度dif-1-0', '燃料阀开度t0', '燃料流量dif-3-0', '燃料流量dif-5-0',
           '燃料流量dif-1-0', '燃料流量t0']]
    t = t.loc[['油品出口温度avg_-10_-6', '油品出口温度avg_-5_0', '油品出口温度avg_dif',
               '油品出口温度设定值avg_-10_-6','油品出口温度设定值avg_-5_0', '油品出口温度设定值avg_dif',
               '出口温度设定值与观测值之差avg_-10_-6', '出口温度设定值与观测值之差avg_-5_0', '出口温度设定值与观测值之差avg_dif'
               ]]
    print(t)
    t.to_excel(outname % thre, encoding='utf-8_sig')
    print(outname % thre)


# preprocess('12号位置数据.csv', '常', '常压炉前3列.csv')
# preprocess('12号位置数据.csv', '减', '减压炉前3列.csv')

data_corr('常压炉前3列.csv', 'result2/常压炉累积量与燃料相关性-出口温度阈值%f.xlsx', '油品出口温度avg_dif', 0.1)
data_corr('常压炉前3列.csv', 'result2/常压炉累积量与燃料相关性-出口温度设定值阈值%f.xlsx', '油品出口温度设定值avg_dif', 0.01)

data_corr('减压炉前3列.csv', 'result2/减压炉累积量与燃料相关性-出口温度阈值%f.xlsx', '油品出口温度avg_dif', 0.1)
data_corr('减压炉前3列.csv', 'result2/减压炉累积量与燃料相关性-出口温度设定值阈值%f.xlsx', '油品出口温度设定值avg_dif', 0.01)
