#!/usr/bin/python 
# -*-coding:utf-8 -*-
__author__ = '99K'

import pandas as pd

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
        for i in range(11):
            data2save[col + str(i)] = pd.Series(t[i:len(t) - 10 + i])
        if col == '油品出口温度':
            data2save[col + 'avg_0-5'] = sum([data2save[col + str(x)] for x in range(6)]) / 6
            data2save[col + 'avg_6-10'] = sum([data2save[col + str(x)] for x in range(6, 11)]) / 5
            data2save[col + 'avg_dif'] = data2save[col + 'avg_0-5'] - data2save[col + 'avg_6-10']
        else:
            data2save[col + 'dif-1-0'] = data2save[col + '1'] - data2save[col + '0']
            data2save[col + 'dif-3-0'] = data2save[col + '3'] - data2save[col + '0']
            data2save[col + 'dif-5-0'] = data2save[col + '5'] - data2save[col + '0']
        data2save[col + 'dif_rate'] = (data2save[col + '1'] - data2save[col + '0']) / data2save[col + '0']
        for i in range(11):
            del data2save[col + str(i)]
    for col in data:
        if col == 'time' or '阀' in col:
            continue
        data2save = data2save[abs(data2save[col + 'dif_rate']) < 0.1]
        del data2save[col + 'dif_rate']
    data2save = data2save[abs(data2save['油品出口温度avg_dif']) > 0.1]
    data2save.to_excel(out_name, index=False, encoding='utf-8_sig')
    print(out_name)


def data_corr(filename, outname):
    data = pd.read_excel(filename)
    del data['燃料阀开度dif_rate']
    t = data.corr()
    t.to_excel(outname, encoding='utf-8_sig')
    print(data.columns)


# preprocess('D:\PyCharmProjects\ZSH\data\常压炉1015-1026.xlsx', '常压炉前3列.xlsx')
# preprocess('D:\PyCharmProjects\ZSH\data\减压炉1015-1027.xlsx', '减压炉前3列.xlsx')

data_corr('常压炉前3列.xlsx', 'result2/常压炉累积量与燃料相关性.xlsx')
data_corr('减压炉前3列.xlsx', 'result2/减压炉累积量与燃料相关性.xlsx')
