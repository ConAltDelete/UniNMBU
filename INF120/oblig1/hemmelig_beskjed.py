# -*- coding: utf-8 -*-

__author__ = "Mats Hoem Olsen"
__email__ = "matsols@nmbu.no"
import turtle
import bokstav_modul as bm
from lex import *  # Laget av meg, derfor importerer jeg alt

eld_futhark = {
	'dik_alfa':
		{'a': 5803, 'b': 5842, 'd': 5854, 'e': 5846, 'f': 5843, 'g': 5815, 'h': 5818, 'i': 5825, 'j': 5827, 'k': 5810, 'l': 5850, 'm': 5847, 'n': 5822, 'o': 5855, 'p': 5832, 'r': 5809, 's': 5835, 'z':5833, 't': 5839, 'u': 5794, 'w': 5817, " ":5868},
	'dik_spesial_char':
		{"æ":"ae","ø":"ee","å":"aa","x":"es","c":"se","q":"ku","v":"we","y":"ii"},
	'dik_spesial_combo' :
		{"ng":5852,"th":5798,"ii":5831}} #bibliotek for alfabet, lexen trenger dette for å konvertere fra latin til annen unicode.

beskjed = "Jeg har en beskjed til deg. Du er søt og turtle er treig."
# test beskjed ved debugging av font
beskjed_test = "th"

avdrag = 0

encodet = lex(beskjed,eld_futhark).word_encode() #Vår frelser og herre, Lexen! Den oversetter str til liste med int. All int i str blir til char i str

#Testing code, åpne for å se unicode versjon for å feilsøke
"""
temp = ""
for le in encodet:
	temp += chr(le)
print(temp)
"""

limit = 501

hight = 0

counter = 0

turtle.speed(200)

screen_hight = 20 * (2 + int(len(encodet)*10 / limit)) #guide for å få riktig størrelse, må ses nærmere på

turtle.setup(width = 3/2 * limit, height = screen_hight + 10) #Bruker vennlighet

turtle.penup() #Må ha for å sette posisjon
for letter in encodet:
	temp_lenght_counter = 10*counter + 1 - avdrag
	hight = hight - 15 if temp_lenght_counter > limit else hight # Når man ønsker å gå lavere på slutten av en linje
	avdrag = 0 if temp_lenght_counter > limit else avdrag # ved å la avdraget være uforandret får vi skråtekst
	counter = 0 if 10*counter + 1 - avdrag > limit else counter #Speeeeeeeeeed
	turtle.goto(-250 + 10*counter + 1 - avdrag,screen_hight / 2 + hight - 25) #Start på font
	letterl = chr(letter) #oversetter fra int til en bokstav, fjernes ved mangel på lexen
	turtle.pendown()
	avdrag += eval("bm.tegn_{}()".format(letterl)) if letterl not in [" ",".",",","᛬"] else eval("bm.tegn_{}()".format({",":"kom",".":"punk"," ":"sp","᛬":"sp"}[letterl])) #tegner og opdaterer avdrag, SPEED CODE!
	turtle.setheading(0)
	counter += 1 #Oppdatering
turtle.hideturtle() #trengs ikke men bør være med for å lese siste font.
turtle.done()

#program simulering
"""
cmd: python.exe hemmelig_beskjed.py
*encodet tekst vises*
*turtle kjører*
*turtle tegner encodet tekst*
*program termineres*
"""