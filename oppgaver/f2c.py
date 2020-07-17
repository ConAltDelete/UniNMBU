# -*- coding: utf-8 -*-
"""
Created on Sun Sep  2 18:25:28 2018

@author: matsh
"""

def c(f):
    c = (5.0/9.0)*(f-32)
    return c
def f(c):
    f = ((9.0*c)/5.0)+32
    return f

print(c(1))
