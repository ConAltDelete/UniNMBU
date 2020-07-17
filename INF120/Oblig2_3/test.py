from lag_indeks import *

def indekser_bøker(mappe):
	indeks = dict()
	mappe = Path(mappe + "/")
	bokfil = None

	for fil in mappe.glob('*.bok'):
		bokfil = Path(fil)
		indeks.update(legg_til_bok_i_indeks(indeks,bokfil))
	
	return indeks

if __name__ == "__main__":
	indeks = indekser_bøker('bøker')
	print(indeks_søk.søk_i_indeks_med_streng(indeks, 'hound, sherlock'))