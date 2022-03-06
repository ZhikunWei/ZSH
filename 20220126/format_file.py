#!/usr/bin/python 
# -*-coding:utf-8 -*-
__author__ = '99K'
import pandas as pd

all_file = pd.read_csv('D:\PyCharmProjects\ZSH\data/12位号DCS数据/2021-12-18.csv')
all_file.drop_duplicates(subset=['time'], inplace=True)
for i in range(19, 32):
    file = pd.read_csv('D:\PyCharmProjects\ZSH\data/12位号DCS数据/2021-12-%d.csv' % i)
    file.drop_duplicates(subset=['time'], inplace=True)
    all_file = pd.concat([all_file, file], ignore_index=True)
    print(i, all_file.shape)
all_file.to_csv('12号位置数据.csv', index=False)
for i in range(1, 18):
    file0 = pd.read_csv('D:\PyCharmProjects\ZSH\data/12位号DCS数据/2022-01-%02d常.csv' % i)
    file0.drop_duplicates(subset=['time'], inplace=True)
    file1 = pd.read_csv('D:\PyCharmProjects\ZSH\data/12位号DCS数据/2022-01-%02d减.csv' % i)
    file1.drop_duplicates(subset=['time'], inplace=True)
    file = pd.merge(file0, file1, on='time')
    print(i, file.shape)
    all_file = pd.concat([all_file, file], ignore_index=True)
    print(i, all_file.shape)
all_file.to_csv('12号位置数据.csv', index=False)
for i in range(18, 26):
    file = pd.read_csv('D:\PyCharmProjects\ZSH\data/12位号DCS数据/2022-01-%d.csv' % i)
    file.drop_duplicates(subset=['time'], inplace=True)
    all_file = pd.concat([all_file, file], ignore_index=True)
    print(i, all_file.shape)
all_file.to_csv('12号位置数据.csv', index=False)