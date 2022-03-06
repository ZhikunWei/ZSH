#!/usr/bin/python 
# -*-coding:utf-8 -*-
__author__ = '99K'

import pandas as pd

d1 = {
    '0201FIQ11709A.IN': '常压炉油品流量',
    '0201TI11701.PV': '常压油品入口温度',
    '0201TIC11704.PV': '常压油品出口温度',
    '0201TIC11704.SV': '常压油品出口温度设定值',
    '0201FIC11813.MV': '常压燃料阀开度',
    '0201FIC11813.PV': '常压燃料流量',
    
}
d2 = {
    '0201FIQ20103A.IN': '减压炉油品流量',
    '0201TI20101.PV': '减压油品入口温度',
    '0201TIC20110.PV': '减压油品出口温度',
    '0201TIC20110.SV': '减压油品出口温度设定值',
    '0201FIC20201.MV': '减压燃料阀开度',
    '0201FIC20201.PV': '减压燃料流量'
}

file = pd.read_csv('12号位置数据.csv', low_memory=False)
del file['device_code']


def process(prefix='常'):
    data = pd.DataFrame()
    data['time'] = file['time']
    if '常' in prefix:
        d = d1
    else:
        d = d2
    for k in d:
        data[d[k]] = file[k]
    data[prefix + '压温度设定值与观测值差值'] = data[prefix + '压油品出口温度设定值'] - data[prefix + '压油品出口温度']
    data2save = pd.DataFrame()
    data2save['time'] = data['time']
    for col in data:
        if col == 'time':
            continue
        print(col)
        t = data[col].values
        data2save[col + '1'] = pd.Series(t[1:])
        data2save[col + '0'] = pd.Series(t[:-1])
        data2save[col + 'dif_rate'] = (data2save[col + '1'] - data2save[col + '0']) / data2save[col + '0']
        data2save[col + 'dif_real'] = data2save[col + '1'] - data2save[col + '0']
    print(data2save.shape)
    for col in data:
        if col == 'time' or '阀' in col:
            if 'dif_rate' in col:
                del data2save[col + 'dif_rate']
            continue
        data2save = data2save[(data2save[col + 'dif_rate'] < 0.1) & (data2save[col + 'dif_rate'] > -0.1)]
        del data2save[col + 'dif_rate']
        data2save[col + '_min'] = data2save[col + '1'] - data2save[col + '1'].min()
    print(data2save.shape)
    data2save.to_csv(prefix+'12号位置数据前6列.csv', index=False, encoding='utf-8_sig')


process('常')
process('减')