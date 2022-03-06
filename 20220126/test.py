#!/usr/bin/python 
# -*-coding:utf-8 -*-
__author__ = '99K'

import pandas as pd

data = pd.read_csv('常压炉前3列.csv')
print(data.columns)
t = data.describe()
