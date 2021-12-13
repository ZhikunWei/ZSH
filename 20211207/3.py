#!/usr/bin/python 
# -*-coding:utf-8 -*-
__author__ = '99K'

import pandas as pd
from sklearn.linear_model import LinearRegression

changya = pd.read_csv('常压整理完成1207.csv')
jianya = pd.read_csv('减压整理完成1207.csv')

y1 = changya['烟道氧含量01'].values
y2 = changya['烟道氧含量02'].values
y3 = changya['烟道氧含量03'].values
y4 = changya['烟道氧含量04'].values
ys = [y1, y2, y3, y4]
x = changya[['鼓风机变频', '烟道挡板05', '烟道挡板06', '燃料流量', '常压风门蝶阀开度之和', '减压风门蝶阀开度之和', '燃料气热值']].values
# x = changya[['鼓风机变频', '烟道挡板05', '烟道挡板06',]].values
coefs = []
regs = []
y_preds = []
losses = []
pred_loss = []

hy1 = 2.273193
hy2 = 2.327515
hy3 = 2.188531
hy4 = 2.386542
hys = [hy1, hy2, hy3, hy4]

for i in range(4):
    reg = LinearRegression()
    reg.fit(x, ys[i])
    y_pred = reg.predict(x)
    y_preds.append(y_pred)
    regs.append(reg)
    coefs.append(reg.coef_[:3])
    losses.append(sum((ys[i] - hys[i]) ** 2)/len(ys[i]))
    pred_loss.append(sum((y_pred - hys[i])**2)/len(ys[i]))
print('coef', coefs)
print(losses)
print(pred_loss)
for i in range(3):
    delta = 2*sum([(hy1 - y_preds[j]) * coefs[j][i] for j in range(4)]) / 4
    # print(delta)
    x[:, i] = x[:, i] - delta

new_y_preds = []
new_loss = []
for i in range(4):
    new_y = regs[i].predict(x)
    new_y_preds.append(new_y)
    new_loss.append(sum((new_y - hys[i])**2)/len(ys[i]))
print(new_loss)
