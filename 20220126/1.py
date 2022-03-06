#!/usr/bin/python 
# -*-coding:utf-8 -*-
__author__ = '99K'

import pandas as pd


def data_corr(filename, outname):
    data = pd.read_csv(filename)
    del data['time']
    for col in data:
        if '0' in col:
            del data[col]
    t = data.corr()
    if '常' in filename:
        t = t[['常压燃料流量dif_real', '常压燃料流量1', '常压燃料阀开度dif_real', '常压燃料阀开度1',]]
    else:
        t = t[['减压燃料流量dif_real', '减压燃料流量1', '减压燃料阀开度dif_real', '减压燃料阀开度1', ]]
    t.to_excel(outname, encoding='utf-8_sig')
    print(outname)


data_corr('常12号位置数据前6列.csv', '常压炉相关性.xlsx')
data_corr('减12号位置数据前6列.csv', '减压炉相关性.xlsx')
