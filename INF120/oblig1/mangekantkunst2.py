# -*- coding: utf-8 -*-

__author__ = "Mats Hoem Olsen"
__email__ = "matsols@nmbu.no"
import turtle #! samme beskjed som i forrige oppgave...

user_input = int(input("gi et tall større enn 0\n"))
if user_input <= 0:
	raise ValueError("input må være større enn 0")
blad_tall = int(input("hvor mange blader vil du ha? n > 0\n"))
if blad_tall <= 0:
	raise ValueError("input må være større enn 0")

length = 80
penta = 360/user_input #vi sier navnet er informativt... Dette er veldig kort kode, gled deg til oppgave 3
blad = 360/blad_tall

for b in range(blad_tall):
	for l in range(user_input):
		turtle.forward(length)
		turtle.right(penta)
	turtle.right(blad)
turtle.done()

"""
cmd: python.exe mangekantkunst2.py
gi et tall større enn 0
6
hvor mange blader vil du ha?
3
*turtle kjører*
*turtle tegner 3 6-kanter hvor sidene er rører hverandre.*
cmd: python.exe mangekantkunst2.py
gi et tall større enn 0
0
*viser en feilmelding*
*Program termineres*

"""