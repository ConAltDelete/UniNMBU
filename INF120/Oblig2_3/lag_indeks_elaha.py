# -*- coding: utf-8 -*-
from pathlib import Path
import indeks_søk    # Kanskje du skal bruke noen av funksjonene du lagde her?


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
    Vi kan oppdatere en tom mengde med ``set`` funksjonen og legge til
    mange element om gangen med ``update`` funksjonen.

    >>> mengde = set()
    >>> print(mengde)
    {}
    >>> mengde.update([1, 2, 'a'])
    >>> print(mengde)
    {1, 2, 'a'}
    >>> mengde.update([2, 'a', 'b', 1])
    >>> print(mengde)
    {'b', 1, 2, 'a'}

    Husk ``finn_unike_ord_i_streng`` du lagde før denne!

    Examples
    --------
    >>> strenger = ["Nå arbeider vi med INF120.", "Faktisk arbeider vi med siste oblig i INF120!"] 
    >>> finn_alle_unike_ord_i_liste_av_strenger(strenger)
    {'nå', 'arbeider', 'vi', 'med', 'inf120', 'faktisk', 'siste', 'oblig', 'i'}

    Merk at rekkefølgen på ordene ikke spiller noen rolle!
    """
    
    # Vi kan fjerne et tegn ved å skrive
    # Gjør til små bokstaver og fjern spesialtegn
    # streng = streng.replace(",", "")
    # Vi ønsker å fjerne alle tegnene i spesialtegn-lista
    
  #fjern_spesialtegn = [',', '.', '"', '\'', ':', ';', '(', ')', '-', '?', '!']
  
 
    
   # fjern_spesialtegn = [',', '.', '"', '\'', ':', ';', '(', ')', '-', '?', '!']
 
 
    unike_ord = set()
   
    for streng in liste_av_strenger:
        
        unike_ord.update(indeks_søk.finn_unike_ord_i_streng(streng))
        
        return unike_ord
        
        
#strenger = ["Nå arbeider vi med INF120.", "Faktisk arbeider vi med siste oblig i INF120!"] 
#print(finn_alle_unike_ord_i_liste_av_strenger(strenger))
    
        
        
        #strenger = strenger.lower()
        #strenger = fjern_spesialtegn(strenger)
       
        
        #ord_liste = strenger.split(" ")
        #unike_ord = set(ord_liste)
    
   # return unike_ord
 
 
  


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
    Om du prøver å gjøre et Path objekt om til en Path så endrer du ingen ting.

    >>> fil = 'books/The_Works_of_Edgar_Allan_Poe.txt'
    >>> fil = Path(fil)
    >>> fil
    WindowsPath('books/The_Works_of_Edgar_Allan_Poe.txt')
    >>> fil = Path(fil)
    >>> fil
    WindowsPath('books/The_Works_of_Edgar_Allan_Poe.txt')

    MERK: Om du bruker Mac eller Linux vil det være en UnixPath istedenfor
    en WindowsPath.

    Husk: Du lagde en funksjon som finner unike ord i en liste av strenger!

    >>> indeks_sok.finn_unike_ord_i_streng("Hei, hei, på deg.")
    {'hei', 'på', 'deg'}
    """
   # ord_i_bok = None  # Slett denne linja
    # Skriv kode her


    bokfil = "bøker\\The_Works_of_Edgar_Allan_Poe.bok"
    with open(bokfil, "r") as fil:
        liste_linjer = fil.readlines()
        ord_i_bok=finn_alle_unike_ord_i_liste_av_strenger(liste_linjer)
        
    return ord_i_bok
        
bokfil = "The_Works_of_Edgar_Allan_Poe.bok"
print(finn_unike_ord_i_bok(bokfil))











def legg_til_bok_i_indeks(indeks, bokfil):
    """
    Denne funksjonen skal legge til en ny bok i indeksen.

    Måten denne nye boken skal legges til i indeksen er følgende

    1. Finn de unike ordene i boka.
    2. Iterer gjennom hvert unikt ord og sjekk om det er del av indeksen
       allerede.

       * Hvis det er del av indeksen skal tittelen på denne bokfilen legges
         til i den korresponderende mengden med filnavn.
       * Hvis det ikke er del av sokeindeksen, så skal legges til som nøkkel
         i sokeindeksen, hvis korresponderende verdi skal være mengden som
         inneholder tittelen på denne bokfilen.

    Arguments
    ---------
    indeks : Dictionary[str] -> Set[str]
        En sokeindeks. Hver nøkkel er engelske ord som forekommer i minst
        en av bøkene som er indeksert. Nøkkelen "sherlock" peker på en
        mengde som inneholder filnavnet til alle bøker som inneholder
        ordet "sherlock".
    bokfil : Path or str
        Filplasseringen til bokfilen som skal legges til i sokeindeksen.

    Returns
    -------
    indeks : Dictionary[str] -> Set[str]
        En oppdatert sokeindeks. Hver nøkkel er engelske ord som forekommer i minst
        en av bøkene som er indeksert. Nøkkelen "sherlock" peker på en
        mengde som inneholder filnavnet til alle bøker som inneholder
        ordet "sherlock".

    Notes
    -----
    Vi kan legge til nye element i en mengde ved å bruke ``mengde.add``
    funksjonen.

    >>> mengde = set(['a', 'hei', 'hei', 'a'])
    >>> print(mengde)
    {'a', 'hei'}
    >>> mengde.add('b')
    >>> print(mengde)
    {'a', 'hei', 'b'}
    >>> mengde.add('a')
    {'a', 'hei', 'b'}

    Når du sjekker om et element er en del av en dictionary så sjekker du
    om det elementet er en nøkkel i den dictionaryen.

    >>> indeks = {'a': {'bok1.bok', 'bok2.bok'}, 'is': {'bok1.bok'}}
    >>> 'a' in indeks
    True
    >>> 'c' in indeks
    False

    Vi kan få filnavnet til en path ved å se på ``name`` attributten.

    >>> bokfil = Path('books/Benefactor.bok')
    >>> bokfil.name
    Benefactor.bok
    """
    # Skriv kode her

    return indeks


def indekser_bøker(mappe):
    r"""
    Lag en sokeindeks med alle filene i den spesifiserte mappen.

    Her skal du starte med å lage en tom sokeindeks, det vil si en tom
    dictionary. Så skal du iterere gjennom hver bokfil i den spesifiserte
    mappen og legge alle til i indeksen.

    Arguments
    ---------
    mappe : Path or str
        Mappen vi skal soke etter filer i. Hvis denne er en streng skal den
        gjøres om til en Path.

    Returns
    -------
    indeks : Dictionary[str] -> Set[str]
        En sokeindeks over alle bokfiler i den spesifiserte mappen.

    Notes
    -----    
    Om du prøver å gjøre et Path objekt om til en Path så endrer du ingen ting.

    >>> fil = 'books/The_Works_of_Edgar_Allan_Poe.bok'
    >>> fil = Path(fil)
    >>> fil
    WindowsPath('books/The_Works_of_Edgar_Allan_Poe.bok')
    >>> fil = Path(fil)
    >>> fil
    WindowsPath('books/The_Works_of_Edgar_Allan_Poe.bok')


    MERK: Om du bruker Mac eller Linux vil det være en UnixPath istedenfor
    en WindowsPath, men funksjonaliteten er den samme.

    Du kan iterere gjennom alle filer med en spesifikk filtype med
    ``Path.glob`` metoden

    >>> mappe = Path('books')
    >>> for bokfil in mappe.glob('*.bok'):
    ...     print(bokfil)
    books\A_Journey_to_the_Centre_of_the_Earth.bok
    books\Benefactor.bok
    ...
    books\Vulcans_Workshop.bok

    Alternativt kan du iterere gjennom alle filer i en mappe med
    ``Path.iterdir`` metoden og hente de filene med rett filtype med
    ``str.endwith`` metoden.

    >>> mappe = Path('books')
    >>> for bokfil in mappe.iterdir:
    ...     if bokfil.name.endswith('.bok'):
    ...         print(bokfil)
    books\A_Journey_to_the_Centre_of_the_Earth.bok
    books\Benefactor.bok
    ...
    books\Vulcans_Workshop.bok
    """
    indeks = None  # Slett denne linja
    # Skriv kode her

    return indeks


if __name__ == "__main__":
    
    
    

    indeks = indekser_bøker('books')
    print(indeks_søk.søk_i_indeks_med_streng(indeks, 'hound, sherlock'))
