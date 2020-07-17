# -*- coding: utf-8 -*-
"""
Created on Fri Aug 24 11:24:21 2018

@author: matshol
"""

def rate(a,n,p):
    core = float(1 + (p*0.01))
    intrest = float(a*(core**n))
    return intrest

a = int(input("amount "))
n = int(input("years "))
p = int(input("persent "))

print ("you have " + str(rate(a,n,p)) + " euro after " + str(n) + " years.")

'''
python3: runfile('~/interest_rate.py')

amount 100

years 3

persent 5
you have 1157.6250000000002 euro after 3 years.
'''
