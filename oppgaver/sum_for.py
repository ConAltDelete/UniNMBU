# -*- coding: utf-8 -*-
"""
Created on Mon Sep 10 20:12:25 2018

@author: matsh
"""
"""
s = 0; M = 3 #k er ikke definert
for i in range(M): #M går ikke hele veien til maks verdi
    s += 1/2*k**2  #det er ikke flyt tall, mangler parantes
print(s) 
"""
s = 0; M = 3; k = 1 #k er ikke definert
for i in range(M+1): #M går ikke hele veien til maks verdi
    s += 1.0/((2*k)**2) #det er ikke flyt tall, mangler parantes
print(s) 

s = 0; M = 3; k = 1; i = 0
while i <= M: 
    s += 1.0/((2*k)**2) 
    i += 1
print(s) 