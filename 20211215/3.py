#!/usr/bin/python 
# -*-coding:utf-8 -*-
__author__ = '99K'

import pandas as pd
from sklearn.linear_model import LinearRegression
import numpy as np


def control_model(filename, hy1, hy2):
    changya = pd.read_csv(filename)
    # changya = changya.iloc[changya.shape[0]*4//5, :]

    y1 = changya['炉膛负压G'].values
    y2 = changya['炉膛负压H'].values
    
    ys = [y1, y2]
    x_names = ['鼓风机变频', '引风机变频', '空气预热温度（空气入炉温度）', '烟气出炉温度', '燃料气热值', '燃料流量',
               '常压风门蝶阀01', '常压风门蝶阀02', '常压风门蝶阀03', '常压风门蝶阀04', '减压风门蝶阀01', '减压风门蝶阀02']
    if "常压" in filename:
        x_names = ['烟道挡板05', '烟道挡板06'] + x_names
    else:
        x_names = ['烟道挡板03'] + x_names
    x = changya[x_names].values
    coefs = []
    regs = []
    y_preds = []
    losses = []
    pred_loss = []

    hys = [hy1, hy2]
    
    for i in range(2):
        reg = LinearRegression()
        reg.fit(x, ys[i])
        y_pred = reg.predict(x)
        y_preds.append(y_pred)
        regs.append(reg)
        coefs.append(reg.coef_[:2])
        losses.append(np.sqrt(sum((ys[i] - hys[i]) ** 2)/len(ys[i])))
        pred_loss.append(np.sqrt(sum((y_pred - hys[i])**2)/len(ys[i])))
    print('coef', coefs)
    print('losses', losses)
    print('pred_loss', pred_loss)
    if "常压" in filename:
        x_num = 2
    else:
        x_num = 1
    for i in range(x_num):
        delta = 2*sum([(hy1 - y_preds[j]) * coefs[j][i] for j in range(2)]) / 2
        print('delta', delta)
        x[:, i] = x[:, i] - delta
    
    new_y_preds = []
    new_loss = []
    for i in range(2):
        new_y = regs[i].predict(x)
        new_y_preds.append(new_y)
        new_loss.append(np.sqrt(sum((new_y - hys[i])**2)/len(ys[i])))
    print('new_loss', new_loss)


control_model('常压整理完成1215.csv', -54.9, -46.74)
print()
control_model('减压整理完成1215.csv', -49.9, -50.14)