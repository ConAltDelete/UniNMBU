# -*- coding: utf-8 -*-
"""
Created on Sun Sep  2 10:43:16 2018

@author: matsh
"""

from math import exp

B = 50000.0; c = 9; k = 0.2; periode = 48
t = [x for x in range(0,periode+1)] #lager liste
n= [B/(1+c*(exp(-1*k*t))) for t in t] #formel for population
for z in zip(t,n):
    print("år{:^5}-->{:^12}".format(z[0],round(z[1],2)))