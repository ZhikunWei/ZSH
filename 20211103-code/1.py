#!/usr/bin/python 
# -*-coding:utf-8 -*-
__author__ = '99K'

import pandas as pd


def data_corr(filename, outname):
    data = pd.read_excel(filename)
    del data['time']
    for col in data:
        if '0' in col:
            del data[col]
    t = data.corr()
    t.to_excel(outname, encoding='utf-8_sig')
    print(outname)


data_corr('常压炉前5列.xlsx', '常压炉相关性.xlsx')
data_corr('减压炉前5列.xlsx', '减压炉相关性.xlsx')