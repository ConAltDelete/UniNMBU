# -*- coding: utf-8 -*-
"""
Created on Sun Sep  2 14:45:28 2018

@author: matsh
"""
#Msmall = 47 
#Mlarge = 67 
#p =  1.038 
#c = 3.7 
#K = 5.4e-3
#Tw = 100 
#T0_fridge = 4+298
#T0_room = 20+298
#Ty = 70+298

def egg(m,t0,ty):
    from math import pi, log
    p =  1.038 
    c = 3.7 
    K = 5.4*10**(-3)
    Tw = 100 
    t1 = (m**(2.0/3)*c*p**(1.0/3))
    t2 = (K*pi**2*(4*pi/3)**(2.0/3))
    t3 = log(0.76*(t0-Tw)/(ty-Tw))
    t = (t1/t2)*t3
    return t
print(egg(67,4,70))