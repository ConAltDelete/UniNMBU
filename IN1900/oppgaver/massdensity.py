# -*- coding: utf-8 -*-
"""
Created on Fri Aug 24 15:26:28 2018

@author: matshol
"""

mass = float(input("Mass(g): "))/1000
volum = float(input("volum(cm^3): "))/(100**3)
dens = mass/volum

print(round(dens))


if dens <= 110:
    print("oh my, that't light man.")
elif dens > 110 and dens <= 400:
    print("probaly kork.")
elif dens > 400 and dens <= 21235:
    print("quite likely Rhenium.")
elif dens > 21235:
    print("must be platnium.")
else:
    print("that's some dense thing. Beyond human knowlage.")

"""
Mass(g): 828

volum(cm^3): 40
20700
quite likely Rhenium.
"""