#!/usr/bin/python 
# -*-coding:utf-8 -*-
__author__ = '99K'

import pandas as pd


def data_corr(filename, outname, out_tem_thre=0.05):
    data = pd.read_excel(filename)
    del data['time']
    data = data[abs(data['油品出口温度dif_real']) > out_tem_thre]
    for col in data:
        if '0' in col:
            del data[col]
    t = data.corr()
    t.to_excel(outname % out_tem_thre, encoding='utf-8_sig')
    print(outname % out_tem_thre)


data_corr('../20211103-code/常压炉前5列.xlsx', 'result1/常压炉相关性%f.xlsx', out_tem_thre=0.05)
data_corr('../20211103-code/常压炉前5列.xlsx', 'result1/常压炉相关性%f.xlsx', out_tem_thre=0.1)
data_corr('../20211103-code/常压炉前5列.xlsx', 'result1/常压炉相关性%f.xlsx', out_tem_thre=0.2)
data_corr('../20211103-code/常压炉前5列.xlsx', 'result1/常压炉相关性%f.xlsx', out_tem_thre=0.5)
data_corr('../20211103-code/减压炉前5列.xlsx', 'result1/减压炉相关性%f.xlsx', out_tem_thre=0.05)
data_corr('../20211103-code/减压炉前5列.xlsx', 'result1/减压炉相关性%f.xlsx', out_tem_thre=0.1)
data_corr('../20211103-code/减压炉前5列.xlsx', 'result1/减压炉相关性%f.xlsx', out_tem_thre=0.2)
data_corr('../20211103-code/减压炉前5列.xlsx', 'result1/减压炉相关性%f.xlsx', out_tem_thre=0.5)
