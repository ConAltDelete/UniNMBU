# To add a new cell, type '# %%'
# To add a new markdown cell, type '# %% [markdown]'
# %% [markdown]
# Oppgave 1
# =========
# %% [markdown]
# A
# ---

# %%
import matplotlib.pyplot as plt
import pandas as pd

# %% [markdown]
# B
# ----

# %%
rådata = pd.read_csv("data.csv",index_col=0)

# %% [markdown]
# C
# ---

# %%
rådata.info()

# %% [markdown]
# <class 'pandas.core.frame.DataFrame'>
# Int64Index: 541909 entries, 0 to 541908
# Data columns (total 8 columns):
#  #   Column       Non-Null Count   Dtype  
# ---  ------       --------------   -----  
#  0   InvoiceNo    541909 non-null  object 
#  1   StockCode    541909 non-null  object 
#  2   Description  540455 non-null  object 
#  3   Quantity     541909 non-null  int64  
#  4   InvoiceDate  541909 non-null  object 
#  5   UnitPrice    541909 non-null  float64
#  6   CustomerID   406829 non-null  float64
#  7   Country      541909 non-null  object 
# dtypes: float64(2), int64(1), object(5)
# memory usage: 37.2+ MB
# %% [markdown]
# D
# ---

# %%
print(rådata["InvoiceDate"])
rådata["InvoiceDate"] = pd.to_datetime(
rådata["InvoiceDate"], format="%m/%d/%Y %H:%M"
)
print(rådata.info())

# %% [markdown]
# Her henter koden kolonnen "InvoiceDate" og konverterer den til et standard dato format i form av en  dato-type.
# %% [markdown]
# E
# ---
# For å regne ut totalprisen må vi ta pris per enhet og gange det med antall enheter.

# %%
antall_produkt = rådata["Quantity"]
pris_per_enhet = rådata["UnitPrice"]
salgspris = antall_produkt*pris_per_enhet

# %% [markdown]
# F
# ----

# %%
rådata["Salgspris"] = salgspris

# %% [markdown]
# G
# ---

# %%
rådata.set_index('InvoiceDate',inplace=True)
print(rådata)

# %% [markdown]
# Dette kallet gjør "InvoiceDate" til en id som vi sorterer etter id istedet for en int. Vet du hva "RED WOOLLY HOTTIE WHITE HEART" er? [Se i rådata 2010-12-01 08:26:00 nr 5 (nr 4 hvis indeks[0] = 0)]
# %% [markdown]
# H
# ---

# %%
månedsgrupper = rådata["Salgspris"].groupby(pd.Grouper(freq="M"))
månedssalg = månedsgrupper.sum()
dagsgrupper = rådata["Salgspris"].groupby(pd.Grouper(freq="D"))
dagssalg = dagsgrupper.sum()
print(månedssalg.head())
print(dagssalg.head())

# %% [markdown]
# Månedssalg viser totalen per måned mens dagssalg viser per dag. Dette kan vi se på indeksene som viser dato.
# %% [markdown]
# Oppgave 2
# =========
# A
# ---

# %%
linjeplot_figur = plt.figure()
månedssalg_akser = linjeplot_figur.add_subplot(2, 1, 1)
dagssalg_akser = linjeplot_figur.add_subplot(2, 1, 2)
# Linja over sier at vi ønsker to rader og en kolonne med akser
# Så ber den om første settet med akser (det øverste)
månedssalg.plot(ax=månedssalg_akser)
dagssalg.plot(ax=dagssalg_akser)

# %% [markdown]
# B
# ---

# %%
plt.tight_layout()
# Linja over forteller matplotlib at det er trangt
# så vi må gjøre aksene våre mindre enn normalt.
plt.show()

# %% [markdown]
# Vi kan se på dagssalg at vi har noen dager som ikke har noe salg i det heletatt. Disse gapene ser veldig frekvente ut.
# %% [markdown]
# Oppgave 3
# =========
# A
# ---

# %%
ukedag = rådata.index.weekday
ukedagsgrupper = rådata["Salgspris"].groupby(ukedag)
ukedagssalg = ukedagsgrupper.sum()
print("Salg per ukedag:")
print(ukedagssalg)
# Ukedag 0 er mandag, ukedag 6 er søndag

# %% [markdown]
# Alle linjene gjør sitt beste. Ukedagssalg viser totalsummmen for hver dag mens Ukedagsgrupper grupperer dataen etter dag. 
# %% [markdown]
# B
# ---
# Vi kan se at lørdag ikke har noen salg. Dette ser vi i oppgave 3a hvor indeks 5 mangler, noe som tilsvarer lørdag.
# %% [markdown]
# C
# --
# Vi vet vi mangler noen dager, spesifikt lørdag men vi later som vi ikke vet det. Dette betyr at vi har minst en søyle som ikke eksisterer. 
# Vi løser dette ved å anta at salgene er i kronologisk rekkefølge, mandag til søndag. Derfor kan salg indeks 0 være mandag, indeks 1 være tirsdag, osv... dette bruker vi til vår fordel slik at det vi har data på blir representert. 

# %%
dag_navn = [
"Mandag", "Tirsdag", "Onsdag", "Torsdag",
"Fredag", "Lørdag", "Søndag"
]
ukedagsdata_dagnummer = ukedagssalg.index
ukedagssalg_dagnavn = [dag_navn[d] for d in ukedagsdata_dagnummer]
print(ukedagsdata_dagnummer)

# %% [markdown]
# D
# ---

# %%
dager = plt.figure()
dager_ax = dager.add_subplot()
dager_ax.bar(ukedagssalg_dagnavn,ukedagssalg)
plt.show()

