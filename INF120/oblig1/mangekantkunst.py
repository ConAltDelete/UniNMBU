# -*- coding: utf-8 -*-

__author__ = "Mats Hoem Olsen"
__email__ = "matsols@nmbu.no"
import turtle #! ALDRI importer en hel modul uten at du vet hva som er inni den, og jeg vet ikke...

user_input = int(input("Gi meg et tall større enn 0\n"))
if user_input <= 0:
	raise ValueError("input må være større enn 0")
angle = 360/user_input
length = 80 # 1 = 1 anus

for shit in range(user_input):
	turtle.forward(length)
	turtle.right(angle)

turtle.done()

"""
cmd: python.exe mangekantkunst.py
Gi meg et tall større enn 0
1
*turtle starter*
*tegner en linje*
*program termineres*
"""