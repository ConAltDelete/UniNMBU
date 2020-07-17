from ferdig_indeks import last_in_indeks  # Her laster vi inn en ferdig søkeindeks


def fjern_spesialtegn(streng):
    streng = streng.lower()
   
    spesialtegn = (',', '.', '"', '\'', ':', ';', '(', ')', '-', '?', '!')
   
    for tegn in spesialtegn:
        streng = streng.replace(tegn,"")
    return streng

# streng = "abs1, hei pø deg. Hva heter du?"       ## Eksmempel, test
# fjern_spesialtegn(streng)

def finn_unike_ord_i_streng(streng):
   streng = fjern_spesialtegn(streng)
   streng = streng.strip()
   ord_liste = streng.split(" ")
   unike_ord = set(ord_liste)

   return unike_ord


def finn_felles_ellement_i_flere_mengder(liste_av_mengder):
 
    felles_element = set()
    mengde1 = liste_med_mengder[0]
    
    for k in (liste_med_mengder):
        felles_element = k.intersection(mengde1)
        
    return felles_element
    


def søk_i_indeks_med_mengde(indeks, mengde_av_søkeord):
    
    mulige_bøker = set() 
    felles_ord_indeks = set()
    felles_ord_indeks = finn_felles_ellement_i_flere_mengder(indeks) # alle felles ord
    antall_mengder_av_søkeord = len(mengde_av_søkeord)
    mulige_søkeord = set()
    
    for søkeord in range(mengde_med_søkeord): # Skjekker om hvert enkelt ord i mengde_med_søkeod
                                              # er i dictionary (felles_ord_indeks)
        if søkeord in felles_ord_indeks == true :
            mulige_søkeord.add(søkeord)
    
    antall_søkeord = range(mulige_søkeord) # Finner lengden ti mulige_søkeord
    mulige_bøker = mulige_søkeord[antall_søkeord]  # finner elementene til alle mulige søkeord
    
    
    return mulige_bøker


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
    Kan du gjenbruke en funksjon du lagde tidligere i obligen?

    Examples
    --------
    >>> streng = "abc1, hei på deg. Hva heter du?"
    >>> klargjør_søkestreng(streng)
    "abc1 hei på deg Hva heter du"

    >>> streng = "  Hei på deg!!!\n"
    >>> klargjør_søkestreng(streng)
    "Hei på deg"
    """
    klargjort_streng = None  # Slett denne linja
    # Skriv kode her

    return klargjort_streng


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
    Husk ``søk_i_indeks_med_mengde`` og ``klargjør_søkestreng`` funksjonene
    dine.

    Examples
    --------
    >>> indeks = last_inn_indeks()
    >>> søk_i_indeks_med_streng(indeks, "Sherlock Holmes, scarlet")
    {'Chronicles_of_Martin_Hewitt.bok', 'The_Hound_of_the_Baskervilles.bok'}
    >>> søk_i_indeks_med_streng(indeks, "Dette er ikke i indeksen")
    {}
    """
    mulige_bøker = None  # Slett denne linja
    # Skriv kode her

    return mulige_bøker


if __name__ == "__main__":
    søkestreng = "Sherlock Holmes, scarlet"
    indeks = last_in_indeks()  # Jeg (Yngve) har allerede lagd en indeks dere kan søke i
                               # Den henter vi ut her.

    print(søk_i_indeks_med_streng(indeks, søkestreng))
    # Denne skal printe
    #  {'Chronicles_of_Martin_Hewitt.bok', 'The_Hound_of_the_Baskervilles.bok'}