# -*- coding: utf-8 -*-
from pathlib import Path
import indeks_søk    # Kanskje du skal bruke noen av funksjonene du lagde her?
from functools import reduce

__author__ = "Mats Hoem Olsen"
__email__ = "matsols@nmbu.no"

def finn_alle_unike_ord_i_liste_av_strenger(liste_av_strenger):
	"""
	Lag en mengde med alle ordene som dukker opp i strengene i lista.
	
	Pass på at strengene kun inneholder små bokstaver (hvis store bokstaver
	er med i strengene skal de bli gjort om til små bokstaver). Mellomrom
	på slutten og starten av strengene skal også fjernes.
	
	De følgende spesialtegn må og fjernes:
	``[',', '.', '"', '\'', ':', ';', '(', ')', '-', '?', '!']``
	
	Arguments
	---------
	liste_av_strenger : str
		Strengene vi vil finne unike tegn i.
	
	Returns
	-------
	ord_i_streng : Set[str]
		Mengden med unike ord i alle strengene.
	
	Notes
	-----
	Gjennbruker kode fra forrige oblig. Men gjør liste om til en mega-string!
	"""
	# Skriv kode her

	return indeks_søk.klargjør_søkestreng(" ".join(liste_av_strenger))


def finn_unike_ord_i_bok(bokfil):
	"""
	Lag en mengde med alle ordene som dukker opp i en bok.
	
	Pass på at strengen kun inneholder små bokstaver, og at mellomrom
	på slutten og starten av linjer er fjernet.
	
	De følgende spesialtegnene skal og fjernes:
	``[',', '.', '"', '\'', ':', ';', '(', ')', '-', '?', '!']``
	
	Arguments
	---------
	bokfil : str eller pathlib.Path
		Filen som inneholder boka.
	
	Returns
	-------
	ord_i_bok : Set[str]
		Mengden med unike ord i boka
	
	Notes
	-----
	Igjen gjennbruker kode fra forrige oblig. Vi åpner filen, leser alt, erstatter ny linje med mellomrom.
	""" 
	# Skriv kode her

	return indeks_søk.klargjør_søkestreng((open(bokfil,"r").read()).replace("\n"," "))


def legg_til_bok_i_indeks(indeks, bokfil):
	"""
	Denne funksjonen skal legge til en ny bok i indeksen.

	Måten denne nye boken skal legges til i indeksen er følgende
	
	1. Finn de unike ordene i boka.
	2. Iterer gjennom hvert unikt ord og sjekk om det er del av indeksen 
	   allerede.

	   * Hvis det er del av indeksen skal tittelen på denne bokfilen legges
		 til i den korresponderende mengden med filnavn.
	   * Hvis det ikke er del av søkeindeksen, så skal legges til som nøkkel
		 i søkeindeksen, hvis korresponderende verdi skal være mengden som
		 inneholder tittelen på denne bokfilen.

	Arguments
	---------
	indeks : Dictionary[str] -> Set[str]
		En søkeindeks. Hver nøkkel er engelske ord som forekommer i minst
		en av bøkene som er indeksert. Nøkkelen "sherlock" peker på en
		mengde som inneholder filnavnet til alle bøker som inneholder
		ordet "sherlock".
	bokfil : Path or str
		Filplasseringen til bokfilen som skal legges til i søkeindeksen.
	
	Returns
	-------
	indeks : Dictionary[str] -> Set[str]
		En oppdatert søkeindeks. Hver nøkkel er engelske ord som forekommer i minst
		en av bøkene som er indeksert. Nøkkelen "sherlock" peker på en
		mengde som inneholder filnavnet til alle bøker som inneholder
		ordet "sherlock".
	
	Notes
	-----
	vi går igjennom alle ordene som vi har funnet og lager en dic som inneholder alt i boken.
	"""
	# Skriv kode her

	return {ord_: indeks[ord_].union({Path(bokfil).name}) if ord_ in indeks else {Path(bokfil).name} for ord_ in finn_unike_ord_i_bok(Path(bokfil))}



def indekser_bøker(mappe):
	r"""
	Lag en søkeindeks med alle filene i den spesifiserte mappen.

	Her skal du starte med å lage en tom søkeindeks, det vil si en tom 
	dictionary. Så skal du iterere gjennom hver bokfil i den spesifiserte
	mappen og legge alle til i indeksen.
	
	Arguments
	---------
	mappe : Path or str
		Mappen vi skal søke etter filer i. Hvis denne er en streng skal den
		gjøres om til en Path.
	
	Returns
	-------
	indeks : Dictionary[str] -> Set[str]
		En søkeindeks over alle bokfiler i den spesifiserte mappen.
	
	Notes
	-----
	Med statestikk finner vi bøkene i indeksen, bøkene som ikke er i indeksen, og delte ord. Der etter kombinerer vi alt siden det er nå garantert at ingenting overlapper.
	"""
	return reduce(lambda i,b: {**{ord_:i[ord_].union(b[ord_]) for ord_ in b if ord_ in i},**{ord_:b[ord_] for ord_ in b if ord_ not in i},**{ord_:i[ord_] for ord_ in i if ord_ not in b}},[legg_til_bok_i_indeks({} ,a) for a in Path(mappe + "/").glob('*.bok')],{})

if __name__ == "__main__":
	indeks = indekser_bøker('bøker')
	print(indeks_søk.søk_i_indeks_med_streng(indeks, 'hound, sherlock'))
