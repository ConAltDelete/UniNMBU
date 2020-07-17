# -*- coding: utf-8 -*-

__author__ = "Mats Hoem Olsen"
__email__ = "matsols@nmbu.no"
#import unidecode
"""
et leksikon for konvertering.
16A0 + (0-84)
æ == ae
ø == ee
å == aa
0 --> 24 == A --> Z
25 --> 49 == a --> z
output er unicode (int)
"""
class num_spell: #konverterer tall til bokstaver
	def __init__(self,text):
		self.text = text
		self.gen_num = ["null","en","to","tre","fire","fem","seks","syv","åtte","ni"]
		self.ord_liste = ["en","ti","hundre","tusen","million","milliard"]
		self.pow_liste = [0,1,2,3,6,9]


	def find_min_max(self,num):
		liste = []
		for n in self.pow_liste:
			if n+1 == len(str(num)):
				return n
			elif n+1 > len(str(num)):
				liste.append(self.pow_liste[self.pow_liste.index(n)-1])
				liste.append(n)
				return liste
			else:
				pass

	def num_count(self,num, firs = True, prifix = True):
		num = str(num)
		temp_l = []
		num_len = len(num)
		if not prifix:
			for i in num:
				temp_l.append(self.gen_num[i])
			return temp_l
		if num_len > 1:
			if type(self.find_min_max(num)) is list:
				temp_l += self.num_count(num[:-self.find_min_max(num)[0]],firs=False)
				temp_l += self.num_count(num[-self.find_min_max(num)[0]-1:], firs = True)[1:]
			else:
				temp_l.append(self.num_count(num[0]))
				temp_l.append(self.ord_liste[self.pow_liste.index(self.find_min_max(num))])
				temp_l.append(self.num_count(num[1:],firs =True))
		elif firs:
			temp_l.append(self.gen_num[int(num[0])])
		return temp_l

	def isInt_float(self,s):
		try:
			return float(str(s)).is_integer()
		except:
			return False

	def join_list(self,liste):
		tem = []
		for x in liste:
			if type(x) is list:
				for t in self.join_list(x):
					tem.append(t)
			else:
				tem.append(x)
		return tem
	
	def sort_num(self, num):
		num = str(num)
		num_l = []
		seperator = None
		for i in num:
			if not self.isInt_float(i):
				seperator = i
				break
		num_s = num.split(seperator)
		if len(num_s) == 1:
				num_l.append(self.num_count(num_s[0]))
		elif len(num_s) < 1:
			pass
		else:
			for element in num_s[:-1]:
				num_l.append(self.sort_num(element)); num_l.append(seperator)
			num_l.append(self.sort_num(num_s[-1]))
		return self.join_list(num_l)

	def num_split(self):
		text = self.text
		text = text.split(" ")
		for x in text:
			if any(n.isdigit() for n in x):
				t = text.index(x)
				text[t] = self.sort_num(x)
		text = " ".join(self.join_list(text))
		return text

class lex:
	"""
	class lex 
	Fungerer kun med unikode
	listen må være på form [alfabet,spesiele karakterer, kombo]
	Har spesial bokstaver for formatering av ord
	har sepsial kombo for konvertering av ord
	returnerer en liste med int som kan bli enkoded med utf-8 eller annet som en ønsker.
	"""
	def __init__(self,word,dik):
		if type(dik) is dict:
			self.dik_alfa = list(dik.values())[0]
			self.dik_spesial_char = list(dik.values())[1]
			self.dik_spesial_combo = list(dik.values())[2]
		elif type(dik) is list:
			self.dik_alfa = dik[0]
			self.dik_spesial_char = dik[1]
			self.dik_spesial_combo = dik[2]
		else:
			raise TypeError("must be list or dict, not", type(dik))
		#self.word = unidecode.unidecode(self.contain(num_spell(word).num_split(),self.dik_spesial_char)).lower()
		self.word = self.contain(num_spell(word).num_split(),self.dik_spesial_char).lower()
	def contain(self,word,dik): #hvis spesial bokstav i ord, erstatt.
		for a in dik:
			if a in word.lower():
				word = word.lower().replace(a,dik[a])
				word = self.contain(word,dik)
		return word
	def rip(self,word, dik = 'self.dik_spesial_combo'): #finner spesial combo
		if type(dik) is str:
			dik = eval(dik)
		temp_dik_list = []
		temp_dik = {}
		new_word_list = []
		for a in dik:
			if a in word:
				temp_dik_list.append(a)
		if len(temp_dik_list) == 0:  #? finn ut hvor stor bokstav skiller liten bokstav. Tror det er her i if statment.
			for l in word:
				new_word_list.append(self.encode_letter(l))
		else:
			for combo in temp_dik_list:
				temp_dik[combo] = dik[combo]
			q = list(temp_dik.keys())[0] #henter combo ord
			sub_word_list = word.split(q) #Deler opp order med combo ord
			for sub_word in sub_word_list[:-1]: #tar hvert delord (untatt siste) og skjekker dem.
				sub_word = self.rip(sub_word,temp_dik)
				for p in sub_word: #Etter skjekk legger vi hver bokstav tilbake
					new_word_list.append(p)
				new_word_list.append(temp_dik[q]) #legger på combo ord
			sub_word = self.rip(sub_word_list[-1],temp_dik)
			for p in sub_word: #Etter skjekk legger vi hver bokstav tilbake
				new_word_list.append(p)
		return new_word_list #returnerer ferdig enkodet ord.

	def encode_letter(self,letter): #enkoder bokstaver
		letter = letter.lower()
		try:
			return self.dik_alfa[letter]
		except:
			return ord(letter)

	def word_encode(self):
		return self.rip(self.word)

if __name__ == "__main__":
	word = 'Dette tok meg en måned å gjøre dette klart, altså 4 uker, 28 dager, eller veldig mange timer. Hvem skulle ha trudd det.'
	print(num_spell(word).num_split())
