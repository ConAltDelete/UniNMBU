# -*- coding: utf-8 -*-
"""
Created on Sun Sep  2 11:26:47 2018

@author: matsh
"""

coor = {}
a = float(input("minimum: "))
b = float(input("maximum: "))
n = int(input("interval: "))
h = (b-a)/(n)
for i in range(0,n+1):
    x = a + i*h
    coor[i] = round(x,2)
    print("{:^12g} {:^12g}".format(i,x))
print(coor)
