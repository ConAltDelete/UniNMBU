# -*- coding: utf-8 -*-
"""
Created on Tue Mar 10 14:03:21 2020

@author: Roy Granheim
"""

from ferdig_indeks import last_in_indeks  # Her laster vi inn en ferdig søkeindeks

def fjern_spesialtegn(streng):
    """
    fjerner spesialtegnene ',', '.', '"', '\'', ':', ';', '(', ')', '-', '?', '!' 
    fra et gitt streng og fjerner whitespace fra begynnelsen og slutten av strengen
    """
    streng = streng.strip() # fjerner whitespace foran og bak strengen
    for r in [',', '.', '"', '\'', ':', ';', '(', ')', '-', '?', '!']: # en for loop som sjekker spesialtegn og sletter den
        streng = streng.replace(r, "")
    ren_streng = streng
    return ren_streng

def finn_unike_ord_i_streng(streng):
    """
    Deler opp et gitt streng på mellomrommene og gjør den om til en mengde
    """
    streng = streng.split(" ")  # splitter strengen til en liste basert på space
    unike_ord = set(streng)     # omformer listen til mengder
    return unike_ord

def finn_felles_ellement_i_flere_mengder(liste_av_mengder):
    """
    Finner felles ellementer i en liste av mengder
    """
    snitt_av_mengder = liste_av_mengder[0].intersection(*liste_av_mengder)  # Sjekker første ord mengden mot alle mengdene i listen
    return snitt_av_mengder

def søk_i_indeks_med_mengde(indeks, mengde_av_søkeord):
    """
    Henter fram en liste av mengder bøker basert på om det stemmer med mengdene med søkeord
    """
    liste_med_mengder = []  # danner en tom liste
    for nøkler in indeks:   # sjekker gjennom alle nøklene i indeksen
        if nøkler in mengde_av_søkeord:     # hvis en nøkkel stemmer med et søkeord så legger den deb tilhørende mengden inn i listen
            liste_med_mengder.append(indeks[nøkler])
        else:
            liste_med_mengder.append(set())
    
    mulige_bøker = finn_felles_ellement_i_flere_mengder(liste_med_mengder)

    return mulige_bøker

def klargjør_søkestreng(søkestreng):
    """
    Tar en søkestreng og gjør om uppercase til lowercase, deretter fjerner 
    alle spesialtegn så deler den opp i mengder unike ord
    """
    søkestreng = søkestreng.lower() # gjør om strengen til lowercase
    søkestreng = fjern_spesialtegn(søkestreng) # fjerner spesialtegn
    klargjort_streng = finn_unike_ord_i_streng(søkestreng)

    return klargjort_streng

def søk_i_indeks_med_streng(indeks, søkestreng):
    """
    Klargjører en streng som da blir brukt til å sjekke om den passer i 
    indeksen og gir ut mulige bøker basert på søkestrengen
    """
    klargjort_streng = klargjør_søkestreng(søkestreng)
    mulige_bøker = søk_i_indeks_med_mengde(indeks, klargjort_streng) # kaller på funksjoner

    return mulige_bøker

if __name__ == "__main__":
    søkestreng = "kay"
    indeks = last_in_indeks()  # Jeg (Yngve) har allerede lagd en indeks dere kan søke i
                               # Den henter vi ut her.

    print(søk_i_indeks_med_streng(indeks, søkestreng))
    # Denne skal printe
    #  {'Chronicles_of_Martin_Hewitt.bok', 'The_Hound_of_the_Baskervilles.bok'}