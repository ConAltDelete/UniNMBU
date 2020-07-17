# -*- coding: utf-8 -*-
"""
Created on Sat Sep  1 10:38:39 2018

@author: matsh
"""
import pprint
g = 9.81; v0 = float(input("speed: ")); n = int(input("interval: ")) #masse variabler
t0 = [x*(2*v0/(n*g)) for x in range(0,n+1)] #definerer t
y0 = [round((v0*i)-(0.5*g*i**2),2) for i in t0] #definerer y
ty1 = [[round(t,2),y] for t,y in zip(t0,y0)]
print("{:^12} --> {:^12}".format("time","hight"))
for z in ty1:
    print("{:^12} --> {:^12}".format(z[0],z[1])) #colomn

#for z in ty1: #henter lister
#    for u in z:       
#        v = round(u,2) #runder tid med 2 desimaler
#        print("") #litt pusterom
#        print("{}: {}".format(v,u)) #printer lister med 2 desimaler

pprint.pprint(ty1) #row