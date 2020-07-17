# -*- coding: utf-8 -*-
"""
Created on Fri Aug 31 09:50:17 2018

@author: matsh
"""

Msmall = 47 
Mlarge = 67 
p =  1.038 
c = 3.7 
K = 5.4e-3
Tw = 100 
T0_fridge = 4+298
T0_room = 20+298
Ty = 70+298

from math import pi, log
t1 = ((Mlarge**(2/3))*c*(p**(1/3)))/(K*(pi**2)*((((4*pi)/3)**(2/3))))
t2 = log(0.76*((T0_fridge - Tw)/(Ty - Tw)))
t = t1*t2

print(t)