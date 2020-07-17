class Dato:
	def __init__(self,dato):
		dato_s = dato.split("-")
		self.dag = int(dato_s[-1])
		self.måned = int(dato_s[1])
		self.år = int(dato_s[0])

class Land:
	def __init__(self,land,landkode):
		self.land = land
		self.landkode = landkode

class Smitte: #Setter opp klasse
	def __init__(self,smitte,dato,land,landkode): #Setter opp konstruksjons funksjonen
		self.smitte = smitte
		self.dato = Dato(dato) #Refererer til 
		self.land = Land(land,landkode)

class Region:
	def __init__(self,navn,kode,land): #land er et objekt / referanse til objekt
		self.navn = navn #Navn på region
		self.kode = kode # Usikker, kanskje ubrukelig hvis regioner ikke har koder som land har
		self.land = list(land) #Hvis land er av type liste, så gjør denne ingenting, ellers gjør den landet til en liste med et element

#funksjoner/subrutiner
def d():
	pass
def q():
	quit()
#hoved program
if __name__ == "__main__": #alt inni her kan settes i egen main() eller bare være her.
	dic = {}
	file = open("covid.txt","r");file.readline() #Leser første linje pga headers
	for line in file:
		t = line.split(",") #lager liste med elementer separert av ","
		temp = Smitte(landkode=t[0],land=t[1],dato=t[2],smitte=t[3])
		if temp.dato not in dic: #Oppdaterer dictonary
			dic[temp.dato] = [temp]
		else:
			dic[temp.dato].append(temp)
	
	while True: #Menyløkken
		user_input = input(":> ")
		eval(f"{user_input}()")
