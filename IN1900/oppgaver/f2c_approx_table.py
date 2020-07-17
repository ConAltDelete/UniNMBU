# -*- coding: utf-8 -*-
"""
Created on Mon Sep  3 19:22:53 2018

@author: matsh
"""


maks_temp = 100 #definerer variabler
min_temp = 0
print("{:^5}--> {:^5} ~ {:^5}".format("c","f","approximately f")) #definerer koloner
for f in range(min_temp,maks_temp+1,10): #lager en for løkke
    c_n = (f-30)/2 #tilnærmet formel
    c = (5.0/9)*(f-32) #presis formel
    print("{:^5}--> {:^5} ~ {:^5}".format(f,round(c,2),c_n)) #printer liste