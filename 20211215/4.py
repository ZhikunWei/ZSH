#!/usr/bin/python 
# -*-coding:utf-8 -*-
__author__ = '99K'

# 检查烟道挡板变化幅度

import pandas as pd
from datetime import datetime, timedelta


def check_change():
    changya = pd.read_csv('常压整理完成1215.csv')
    data2save = pd.DataFrame()
    yandao_dif05 = []
    yandao_dif06 = []
    lutangfuyaG_dif = []
    lutangfuyaH_dif = []
    for i in range(1, changya.shape[0]):
        t = datetime.fromisoformat(changya.iloc[i - 1, 0])
        t1 = datetime.fromisoformat(changya.iloc[i, 0])
        if t1 - timedelta(minutes=5) == t:
            yandao_dif05.append(changya.iloc[i, 9] - changya.iloc[i - 1, 9])
            yandao_dif06.append(changya.iloc[i, 10] - changya.iloc[i - 1, 10])
            lutangfuyaG_dif.append(changya.iloc[i, 7] - changya.iloc[i - 1, 7])
            lutangfuyaH_dif.append(changya.iloc[i, 8] - changya.iloc[i - 1, 8])
    data2save['常压炉烟道挡板变化值1'] = pd.Series(yandao_dif05)
    data2save['常压炉烟道挡板变化值2'] = pd.Series(yandao_dif06)
    
    jianya = pd.read_csv('减压整理完成1215.csv')
    yandao_dif03 = []
    lutangfuya_jainyaG_dif = []
    lutangfuya_jainyaH_dif = []
    for i in range(1, jianya.shape[0]):
        t = datetime.fromisoformat(jianya.iloc[i - 1, 0])
        t1 = datetime.fromisoformat(jianya.iloc[i, 0])
        if t1 - timedelta(minutes=5) == t:
            yandao_dif03.append(jianya.iloc[i, 9] - jianya.iloc[i - 1, 9])
            lutangfuya_jainyaG_dif.append(jianya.iloc[i, 7] - jianya.iloc[i - 1, 7])
            lutangfuya_jainyaH_dif.append(jianya.iloc[i, 8] - jianya.iloc[i - 1, 8])
    data2save['减压炉烟道挡板变化值'] = pd.Series(yandao_dif03)
    
    data2save['常压炉炉膛负压G变化值'] = pd.Series(lutangfuyaG_dif)
    data2save['常压炉炉膛负压H变化值'] = pd.Series(lutangfuyaH_dif)
    data2save['减压炉炉膛负压G变化值'] = pd.Series(lutangfuya_jainyaG_dif)
    data2save['减压炉炉膛负压H变化值'] = pd.Series(lutangfuya_jainyaH_dif)
    print(data2save.describe())
    data2save.describe().to_csv('变量数据变化幅度数据统计.csv', encoding='utf-8_sig')
    
    
check_change()