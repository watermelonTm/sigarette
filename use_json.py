import json
import datetime
import os
from os.path import join

class InvalidBarcode(Exception):
    "Raised when the input barcode is not found"
    pass

class Chiusura(Exception):
    "Raised when closing the console"
    pass

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

ready = True
print('-- Scansiona un barcode oppure digita "chiudi" o "quit" per terminare il programma\n')
while ready:
  try:
    valore_letto = input()
    if valore_letto.lower() in ["quit", "chiudi"]:
      ready = False
      raise Chiusura
    
    barcode_letto = float(valore_letto) if valore_letto.isnumeric() else 0
    # Check if input is in list of dictionaries
    check = any(dictionary.get('barcode') == barcode_letto for dictionary in lista_sigarette)
    if not check:
        raise InvalidBarcode
    else:
        for sigaretta in lista_sigarette:
          if barcode_letto == sigaretta['barcode']:
            nome_prodotto = sigaretta['nome']
            aams_prodotto = sigaretta['codice_aams']
            prezzo_prodotto = sigaretta['prezzo']
            # Aggiungi codice_aams e prezzo del prodotto scasionato
            aggiungi_scansionato(sigarette_vendute, nome_prodotto, aams_prodotto, prezzo_prodotto)
            # Stampa nome (alias) prodotto e prezzo
            alias_prodotto = sigaretta['alias'][0] if sigaretta['alias'][0] else nome_prodotto
            print(f'\nTrovato: {alias_prodotto} -- {prezzo_prodotto}€')
  except InvalidBarcode:
    print("Attenzione: Barcode mancante o non trovato!")
    pass
  except Chiusura:
    print("Comando ricevuto -- Chiusura del programma e salvataggio dati...")
    autosave_data()
    print("-- FINE TRASCRIZIONE DATI --")
  except KeyboardInterrupt:
    autosave_data(forced="AUTOSAVE")
    break