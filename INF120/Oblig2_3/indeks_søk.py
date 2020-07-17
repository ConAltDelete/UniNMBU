# -*- coding: utf-8 -*-
from ferdig_indeks import last_in_indeks  # Her laster vi inn en ferdig søkeindeks

__author__ = "Mats Hoem Olsen"
__email__ = "matsols@nmbu.no"

def fjern_spesialtegn(streng):
	r"""
	Fjern de følgende spesialtegnene fra input strengen:
		``[',', '.', '"', '\'', ':', ';', '(', ')', '-', '?', '!']``
	
	Arguments
	---------
	streng : str
		Input strengen som spesialtegn skal fjernes fra
	
	Returns
	-------
	ren_streng : str
		Strengen etter at spesialtegn er fjernet.
	
	Note
	----
	Vi ser igjennom strengen karakter for karakter mens vi filtrerer bort uønskede tegn.
	"""

	return "".join([t for t in streng if t not in [',', '.', '"', '\'', ':', ';', '(', ')', '-', '?', '!']])

def finn_unike_ord_i_streng(streng):
	"""
	Lag en mengde med alle ordene som dukker opp i strengen.
	
	Pass på at strengen kun inneholder små bokstaver (hvis store bokstaver
	er med i strengen skal de bli gjort om til små bokstaver). Mellomrom
	på slutten og starten av linjer skal også fjernes.
	
	De følgende spesialtegn må og fjernes:
	``[',', '.', '"', '\'', ':', ';', '(', ')', '-', '?', '!']``
	
	Arguments
	---------
	streng : str
		Strengen vi vil finne unike tegn i.
	
	Returns
	-------
	ord_i_streng : Set[str]
		Mengden med unike ord i strengen.
	
	Notes
	-----
	Vi fjerner spesialtegn (og konverterer stor til liten). Ved å sette listen, generert av split(), i et set() fjerner vi duplikater. 
	"""
	return set(fjern_spesialtegn(streng).split())

def finn_felles_ellement_i_flere_mengder(liste_av_mengder):
	"""
	Lag en funksjon som finner felles element i en samling av mengder (set).
	
	Arguments
	---------
	liste_av_mengder : List[Set]
		En liste hvor hvert element er en mengde (set på engelsk).
	
	Returns
	-------
	snitt_av_mengder : Set[str]
		En mengde som kun inneholder de elementene som er del av ALLE
		mengdene i ``liste_av_mengder``.
	
	Notes
	-----
	Vi samler settene i en string forså sette alt i en string-versjon av 
	funksjonen vår, deretter kjører vi en eval for å kjøre funksjonen.
	"""
	return liste_av_mengder[0].intersection(*liste_av_mengder[1:]) if len(liste_av_mengder) > 0 else set()

def søk_i_indeks_med_mengde(indeks, mengde_av_søkeord):
	"""
	Finn alle dokument som inneholder alle søkeordene i ``mengde_av_søkeord``.

	Denne funksjonen skal ta to argument som input, en søkeindeks og 
	en mengde med søkeord.

	Søkeindeksen er en dictionary med engelske ord som nøkler og mengden med alle
	dokument som inneholder det ordet som verdi.

	Mengden med søkeord er en mengde (set på Engelsk) som beskriver hva
	som søkes etter.

	Det som returneres er mengden med dokument som inneholder ALLE søkeordene.

	Arguments
	---------
	indeks : dict[str] -> Set[str]
		Søkeindeksen.
	mengde_av_søkeord : Set[str]
		Mengden med søkeord.

	Returns
	-------
	relevante_bøker : Set[str]
		Mengden med bøker som inneholder alle ordene i ``mengde_av_søkeord``.

	Notes
	-----
	Vi henter et søkeord av gangen, hvis den er i indeksen henter vi alle bøkene 
	som har ordet, ellers ignorerer vi det. Til slutt finner vi fellesen av alle mengdene.
	Denne funksjonen blir ikke brukt i denne filen.... yeahhhh..... Fungerer i teorien. 😁
	"""
	return finn_felles_ellement_i_flere_mengder([indeks[w] if w in indeks else set() for w in mengde_av_søkeord])

def klargjør_søkestreng(søkestreng):
	r"""
	Ta inn en søkestreng og klargjør den for å søke i en søkeindeks.

	Strengen skal behandles på samme måte som vi behandler nye strenger
	som skal indekseres. Store bokstaver skal gjøres om til små,
	spesialtegn skal fjernes og "whitespace" tegn på starten og slutten
	av strengen skal fjernes. Til slutt skal strengen splittes ved 
	alle mellomrom og duplikatord skal fjernes.

	Arguments
	---------
	søkestreng : str
		Strengen vi vil finne unike tegn i.
	
	Returns
	-------
	ord_i_streng : Set[str]
		Mengden med unike ord i strengen.
	
	Notes
	-----
	Vi bruker tidligere funksjoner. Blant annet finn_unike_ord_i_streng().
	Og kanskje lower() metoden... 
	"""
	return finn_unike_ord_i_streng(søkestreng.lower())

def søk_i_indeks_med_streng(indeks, søkestreng):
	"""
	Finn alle dokument som inneholder alle søkeordene i ``søkestreng``.

	Denne funksjonen skal ta to argument som input, en søkeindeks og 
	en mengde med søkeord.

	Søkeindeksen er en dictionary med engelske ord som nøkler og mengden med alle
	dokument som inneholder det ordet som verdi.

	Søkestrengen skal først klargjøres. Dette gjøres ved å gjøre strengen til
	små bokstaver og å fjerne spesialtegn. I tillegg skal og whitespace på 
	starten og slutten av strengen fjernes. Deretter skal hvert ord i 
	søkestrengen hentes ut. Disse ordene brukes når det skal søkes i
	de indekserte dokumentene.

	Det som returneres er mengden med dokument som inneholder ALLE søkeordene.

	Arguments
	---------
	indeks : dict
		Søkeindeksen.
	mengde_av_søkeord : str
		Mengden med søkeord.

	Returns
	-------
	relevante_bøker : Set[str]
		Mengden med bøker som inneholder alle ordene i ``mengde_av_søkeord``.

	Notes
	-----
	Denne starter med å hente alle mengdene i indeks, men hvis søkerordet ikke eksisterer 
	så settes in et tomt set. Dette kunne erstates med en return for å spare tid siden 
	intersection av ingenting er ingenting. Til slutt finner den felleselementer.
	"""
	return finn_felles_ellement_i_flere_mengder([indeks[o] if o in indeks else set() for o in klargjør_søkestreng(søkestreng)])


if __name__ == "__main__":
	søkestreng = "Sherlock Holmes, scarlet"
	indeks = last_in_indeks()  # Jeg (Yngve) har allerede lagd en indeks dere kan søke i
							   # Den henter vi ut her.
	#open("test.txt","w").write(str(indeks))

	print(søk_i_indeks_med_streng(indeks, søkestreng))
	# Denne skal printe
	#  {'Chronicles_of_Martin_Hewitt.bok', 'The_Hound_of_the_Baskervilles.bok'}