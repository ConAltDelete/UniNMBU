# -*- coding: utf-8 -*-
"""
Created on Fri Aug 24 15:32:01 2018

@author: matshol
"""

mass = float(input("masse(g): ")) #få masse
mol = 1 #Nå vet vi hvor mange mol er i en mol
mol2atom = 6.02e23 # 1 mol lik 6.02*10^23 partikler ca
c = float(input("antall karbon: ")) #Definerer hvor mange atomer
h = float(input("antall hydrogen: "))
o = float(input("antall oksygen: "))
cmass = c*12.01 #finner total molmassen til atomene
hmass = h*1.008
omass = o*16

totalmolmass = cmass + hmass + omass #finner totalmolmasse med å summere molmassen til atomene

molymass = mass / totalmolmass # molarmassen til molykylet
print("")
print("molarmassen: ",round(molymass))
print("antall mol: ",round(totalmolmass))
print("ca antall atomer: ", (totalmolmass*mol2atom))

"""
runfile('~/glucose.py')

masse: 3243

antall karbon: 6

antall hydrogen: 12

antall oksygen: 6

molarmassen:  18
antall mol:  180
ca antall atomer:  1.08453912e+26
"""