# -*- coding: utf-8 -*-
"""
Created on Fri Aug 24 13:32:24 2018

@author: matshol
"""

from math import e

B = 50000.0     #defines numbers
c = 9
k = 0.2
t = float(input("time: ")) #what time is it?
n=B/(1+c*(e**(-1*k*t)))

print (round(n))
"""
python3: run('\population.py')
time: 24
46552
"""
