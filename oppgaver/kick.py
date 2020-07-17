# -*- coding: utf-8 -*-
"""
Created on Fri Aug 24 11:42:26 2018

@author: matshol
"""

from math import pi

V = float(input("Velocity of football in km/h "))/3.6# meters per second sheep
m = float(input("mass of football in kg ")) #kg
a = float(input("raduis of football in cm ")) / 100 #hopfully meters
Cd = 0.4
e = 1.2 #kg/(m**3)
A = pi*(a**2) #m**2
g = 9.81 #m/(s**2)

Fg = m*g #kg*m/(s**2)

Fd = 0.5*Cd*e*A*(V**2) #kg*m/(s**2)

print("Force of ball: {:e}".format(Fd)) #prints Fd (not standard form)
print("rasio of ball force and normal force: {:e}".format(Fd/Fg)) #printing the rasio of fd and fg

"""
python3: runfile('/kick.py')

Velocity of football in km/h 120

mass of football in kg 0.43

raduis of football in cm 11
Force of ball: 0.000010
rasio of ball force and normal force: 0.000002
"""
