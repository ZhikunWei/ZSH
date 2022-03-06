#!/usr/bin/python 
# -*-coding:utf-8 -*-
__author__ = '99K'

import pandas as pd


def data_corr(filename, outname, item='油品出口温度dif_real', out_tem_thre=0.05):
    data = pd.read_csv(filename)
    del data['time']
    data = data[abs(data[item]) > out_tem_thre]
    for col in data:
        if '0' in col or 'min' in col or 'rate' in col:
            del data[col]
    print(filename, out_tem_thre, data.shape)
    if item == '常压油品出口温度设定值dif_real' and out_tem_thre==0.01:
        data.to_csv('check_data.csv', index=False, encoding='utf-8_sig')
    t = data.corr()
    t.to_excel(outname % out_tem_thre, encoding='utf-8_sig')
    print(outname % out_tem_thre)
    if '常' in filename:
        return t['常压燃料阀开度1'].rename('常压燃料阀开度1_%.2f' % out_tem_thre)
    else:
        return t['减压燃料阀开度1'].rename('减压燃料阀开度1_%.2f' % out_tem_thre)
    

# data_corr('常12号位置数据前6列.csv', 'result1/常压炉相关性出口温度%f.xlsx', item='常压油品出口温度dif_real', out_tem_thre=0.05)
# data_corr('常12号位置数据前6列.csv', 'result1/常压炉相关性出口温度%f.xlsx', item='常压油品出口温度dif_real', out_tem_thre=0.1)
# data_corr('常12号位置数据前6列.csv', 'result1/常压炉相关性出口温度%f.xlsx', item='常压油品出口温度dif_real', out_tem_thre=0.2)
# data_corr('常12号位置数据前6列.csv', 'result1/常压炉相关性出口温度%f.xlsx', item='常压油品出口温度dif_real', out_tem_thre=0.5)
# t = []
# for i, thre in enumerate([0, 0.01, 0.03, 0.05, 0.1, 0.2, 0.3, 0.4]):
#     x = data_corr('常12号位置数据前6列.csv', 'result1/常压炉相关性温度设定值与观测值差值%f.xlsx', item='常压温度设定值与观测值差值dif_real', out_tem_thre=thre)
#     t.append(x)
# all = pd.concat(t, axis=1)
# all.to_excel('result1/常压炉相关性温度设定值与观测值差值_all.xlsx')

# t = []
# for i, thre in enumerate([0, 0.01, 0.03, 0.05, 0.1, 0.2, 0.3, 0.4]):
#     x = data_corr('减12号位置数据前6列.csv', 'result1/减压炉相关性温度设定值与观测值差值%f.xlsx', item='减压温度设定值与观测值差值dif_real', out_tem_thre=thre)
#     t.append(x)
# all = pd.concat(t, axis=1)
# all.to_excel('result1/减压炉相关性温度设定值与观测值差值_all.xlsx')

data_corr('减12号位置数据前6列.csv', 'result1/减压炉相关性出口温度%f.xlsx', item='减压油品出口温度dif_real', out_tem_thre=0.04)
data_corr('减12号位置数据前6列.csv', 'result1/减压炉相关性出口温度%f.xlsx', item='减压油品出口温度dif_real', out_tem_thre=0.5)
# data_corr('减12号位置数据前6列.csv', 'result1/减压炉相关性出口温度%f.xlsx', item='减压油品出口温度dif_real', out_tem_thre=0.1)
# data_corr('减12号位置数据前6列.csv', 'result1/减压炉相关性出口温度%f.xlsx', item='减压油品出口温度dif_real', out_tem_thre=0.2)
# data_corr('减12号位置数据前6列.csv', 'result1/减压炉相关性出口温度%f.xlsx', item='减压油品出口温度dif_real', out_tem_thre=0.5)
# data_corr('减12号位置数据前6列.csv', 'result1/减压炉相关性温度设定值%f.xlsx', item='减压油品出口温度设定值dif_real', out_tem_thre=0.01)
# data_corr('减12号位置数据前6列.csv', 'result1/减压炉相关性温度设定值%f.xlsx', item='减压油品出口温度设定值dif_real', out_tem_thre=0.03)
# data_corr('减12号位置数据前6列.csv', 'result1/减压炉相关性温度设定值%f.xlsx', item='减压油品出口温度设定值dif_real', out_tem_thre=0.05)
# data_corr('减12号位置数据前6列.csv', 'result1/减压炉相关性温度设定值%f.xlsx', item='减压油品出口温度设定值dif_real', out_tem_thre=0.1)
