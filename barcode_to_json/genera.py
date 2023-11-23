import json
import datetime
import os
from os.path import join
import pandas as pd

df_barcode = pd.read_excel("elenco_barcode.xlsx")
elenco_barcode = df_barcode["barcode"].values.tolist()

def autosave_data(forced=None):
  newfolder = './File json sigarette vendute' 
  if not os.path.exists(newfolder):
    os.makedirs(newfolder)
  ora_locale = datetime.datetime.now().strftime("%d_%b_ora%H%M")
  path = f'Venduti_{ora_locale}.json' if not forced else f'Venduti_{ora_locale}_AUTOSAVE.json'
  with open(join(newfolder, path), "w+") as outfile:
    json.dump(sigarette_vendute, outfile)
   
with open("sigarette.json", "r") as jsonFile:
  elenco = json.load(jsonFile)
lista_sigarette = elenco['lista_sigarette']

def aggiungi_scansionato(dict, nome, aams, prezzo):
  if nome not in dict:
    dict[nome] = {
       "nome": nome,
       "aams": aams,
       "prezzo": prezzo,
       "numero_pz": 0
    }
  dict[nome]['numero_pz'] += 1

sigarette_vendute = dict()


for barcode in elenco_barcode:
  barcode_letto = str(barcode)[:-2]
  # Check if input is in list of dictionaries
  check_singolo = any(dictionary.get('barcode') == barcode_letto for dictionary in lista_sigarette)
  check_stecca = any(dictionary.get('barcode_stecca') == barcode_letto for dictionary in lista_sigarette)
  if not check_singolo and not check_stecca:
      print("Attenzione: Barcode mancante o non trovato!")
      pass
  else:
      for sigaretta in lista_sigarette:
        if barcode_letto == sigaretta['barcode']:
          nome_prodotto = sigaretta['nome']
          aams_prodotto = sigaretta['codice_aams']
          # prezzo_prodotto = format(sigaretta['prezzo'], '.2f')
          prezzo_prodotto = sigaretta['prezzo']
          
          # Stampa nome (alias) prodotto e prezzo
          alias_prodotto = sigaretta['alias'][0] if sigaretta['alias'][0] else nome_prodotto
          print(f'\nPacchetto {alias_prodotto} -- {prezzo_prodotto}€')

          # Aggiungi codice_aams e prezzo del prodotto scasionato
          aggiungi_scansionato(sigarette_vendute, alias_prodotto, aams_prodotto, prezzo_prodotto)
        if barcode_letto == sigaretta['barcode_stecca']:
          nome_prodotto = sigaretta['nome']
          aams_prodotto = sigaretta['codice_aams']
          prezzo_prodotto = format(round(sigaretta['prezzo_conv'] * sigaretta['min_kgc']), '.2f')
          
          # Stampa nome (alias) prodotto e prezzo stecca
          alias_prodotto = sigaretta['alias'][0] if sigaretta['alias'][0] else nome_prodotto

          # Aggiungi codice_aams e prezzo della stecca scasionata
          aggiungi_scansionato(sigarette_vendute, alias_prodotto, aams_prodotto, prezzo_prodotto)
          print(f'\nConfezione {alias_prodotto} -- {prezzo_prodotto}€')
      autosave_data()

