import json
import os
from os.path import join
import pandas as pd
import locale
locale.setlocale(locale.LC_NUMERIC, 'it_IT')

df_sigarette = pd.read_excel("elenco_sigarette.xlsx")

# custom_header = ['codice aams', 'nome', 'confez', '€/kg conv', 'prezzo']
df_codice_aams = df_sigarette["codice aams"].values.tolist()
df_nome = df_sigarette["nome"].values.tolist()
df_conv = df_sigarette["€/kg conv"].values.tolist()
df_prezzo = df_sigarette["prezzo"].values.tolist()

path = "sigarette.json"

dictionary = {
  "lista_sigarette": []
  }
with open(path, "w+") as outfile:
  json.dump(dictionary, outfile)

with open(path, "r") as jsonFile:
  elenco = json.load(jsonFile)

for (codice, nome, conv, prezzo) in zip(df_codice_aams, df_nome, df_conv, df_prezzo):
  elenco['lista_sigarette'].append({
  "nome": nome,
  "codice_aams": int(codice),
  "prezzo": locale.atof(prezzo),
  "prezzo_conv": locale.atof(conv),
  "alias": ["", "", "", "", "", ""],
  "barcode": 000,
  "barcode_stecca": 000,
  "min_kgc": 0,
  "categoria": "",
  "vendita": "",
  })
# Aggiungi Pod myblu intense tabaggo 18mg
elenco['lista_sigarette'].append({
  "nome": "my blu intense tobacco 18mg",
  "codice_aams": 4853,
  "prezzo": "Chiedere per sicurezza: 9,00",
  "prezzo_conv": 45,
  "alias": ["myblu intense tabacco 18mg - V4853", "myblu intense", "my blu intense", "intense tabacco", "V4853", ""],
  "barcode": 000,
  "barcode_stecca": 000,
  "min_kgc": "",
  "categoria": "",
  "vendita": "",
  })

with open(path, "r+") as jsonFile:
  json.dump(elenco, jsonFile)

print("-- FINE --")